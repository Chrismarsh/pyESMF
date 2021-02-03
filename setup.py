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

pkg_version = "5" # pyESMF sub-version
pip_esmfpy_version = ESMF_VERSION
CONAN_ESMF_VERSION = ESMF_VERSION

if 'beta' in ESMF_VERSION:
  # this is a beta snapshop, normalize the name for pip deployed as per PEP440 
  # https://www.python.org/dev/peps/pep-0440/#pre-release-separators

  #suppose we have 8.1.0_beta_snapshot_36'
  beta_version = ESMF_VERSION[ESMF_VERSION.rfind('_')+1:]  #get the beta number, eg 36
  rel_ver = ESMF_VERSION[:ESMF_VERSION.find('_')]  # get the primary release version eg 8.0.1

  pip_esmfpy_version = f'{rel_ver}.{pkg_version}b{beta_version}'
  CONAN_ESMF_VERSION=f'{rel_ver}.{beta_version}-beta'

else:
  pip_esmfpy_version = f'{ESMF_VERSION}.{pkg_version}'


force_build = os.environ.get( 'FORCE_BUILD', None )

build_opt='-DFORCE_BUILD:BOOL=OFF'
if force_build:
  build_opt = '-DFORCE_BUILD:BOOL=ON'

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
      version=pip_esmfpy_version,
      description='Python bindings for ESMF',
      long_description="""
      This is an unofficial packaging of the ESMF Python interface that is compaitible with pip and with virtual environments.
      """,
      author='Chris Marsh',
      author_email='chris.marsh@usask.ca',
      url="https://github.com/Chrismarsh/pyESMF",
      cmake_args=['-DESMF_VERSION:STRING='+CONAN_ESMF_VERSION,build_opt],
      install_requires=['numpy'],
      setup_requires=setup_requires,
      packages=find_packages(),

      python_requires='>=3.6',
      cmdclass={'install':install,
          'uninstall': uninstall}
     )






