import os

from conans import ConanFile, CMake, tools


class pyESMF(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake" 

    name = "pyESMF"
    version = "8.1.0"
    license = ""
    author = "Chris Marsh"
    url = "https://github.com/Chrismarsh/pyESMF"
    description = "pyeSMF"
    generators = "cmake_find_package"


    def requirements(self):
        self.requires( "esmf/8.1.0@CHM/stable" )


    def imports(self):
        self.copy("*",src="",dst="", folder=True)  # From bin to bin
        # self.copy("*.dylib*", dst="lib", src="lib")  # From lib to bin
