from skbuild import setup

import skbuild
from skbuild.cmaker import get_cmake_version
from packaging.version import LegacyVersion

from setuptools.command.install import install as Install
from setuptools import find_packages

import os
import shutil
import re

ESMF_VERSION = open('ESMF_VERSION', 'r').read().strip()


class install(Install):
  def run(self):

    #This needs to happen before we call install so we can patch the file before it's copied out. 
    #Doing it with the install libbase after self.install() doesn't work for some reason. I'm guessing a strange conan interaction w/ cmake install
    root = skbuild.constants.CMAKE_INSTALL_DIR()

    gen_path = os.listdir(root+'/esmf/lib/libO')[0]
    mkfile = root+'/esmf/lib/libO/'+gen_path+'/esmf.mk'

    
    with open(mkfile,'r') as infile:
      with open(mkfile+'.tmp','w') as outfile:
        content = infile.read()

        content_new = re.sub(r'([=\-L\-I])(/.+?[0-9A-Za-z]{40}/)', r'\1'+self.install_base+'/esmf/', content, flags = re.M)
        content_new = re.sub(r'(ESMF_INTERNAL_DIR=)(/.+?[0-9A-Za-z]{40})', r'\1'+self.install_base+'/esmf/', content_new, flags = re.M)
        outfile.write(content_new)

    os.rename(mkfile,mkfile+'.old')
    os.rename(mkfile+'.tmp',mkfile)

    #Do the main install
    Install.run(self)

    # write the esmf.mk path directly to the install folder
    with open(os.path.join(self.install_libbase, 'ESMF', 'interface', 'esmfmkfile.py'), 'w') as f:
      mkfile = self.install_base+'/esmf/lib/libO/'+gen_path+'/esmf.mk'
      f.write('ESMFMKFILE = "%s"' % mkfile)

class uninstall(Install):
  def run(self):
    Install.run(self)

    # ensure we nuke the conan esmf binaries
    root = self.install_base+'/esmf'
    print('removing ' +root)
    shutil.rmtree(root,ignore_errors=True)
  

# Add CMake as a build requirement if cmake is not installed or is too low a version
# https://scikit-build.readthedocs.io/en/latest/usage.html#adding-cmake-as-building-requirement-only-if-not-installed-or-too-low-a-version
setup_requires = []
try:
    if LegacyVersion(get_cmake_version()) < LegacyVersion("3.16"):
        setup_requires.append('cmake')
except SKBuildError:
    setup_requires.append('cmake')



setup(name='pyESMF',
      version=ESMF_VERSION,
      description='Python bindings for ESMF',
      long_description="""
      This is an unofficial packaging of the ESMF Python interface that is compaitible with pip and with virtual environments.
      """,
      author='Chris Marsh',
      author_email='chris.marsh@usask.ca',
      url="https://github.com/Chrismarsh/pyESMF",
      cmake_args=['-DESMF_VERSION:STRING='+ESMF_VERSION],
      install_requires=['numpy'],
      setup_requires=setup_requires,
      packages=find_packages(),

      python_requires='>=3.6',
      cmdclass={'install':install,
          'uninstall': uninstall}
     )






