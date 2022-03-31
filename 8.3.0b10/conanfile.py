import os

from conans import ConanFile, CMake, tools


class pyESMF(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake" 

    name = "pyESMF"
    license = ""
    author = "Chris Marsh"
    url = "https://github.com/Chrismarsh/pyESMF"
    description = "pyESMF"
    generators = "cmake_find_package"

    options = {"esmf_version":"ANY"}


    def requirements(self):
        self.requires(f"esmf/{self.options.esmf_version}@CHM/stable" )


    def imports(self):
        self.copy("*",src="",dst="", folder=True)
