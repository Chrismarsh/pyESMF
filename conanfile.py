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

    # options = {"verbose_cmake":[True,False], "build_tests":[True,False] }

    # default_options = {"gperftools:heapprof":True,
    #                    "verbose_cmake":False,
    #                    "build_tests":True}


    # def source(self):
    #     git = tools.Git()
    #     git.clone("https://github.com/Chrismarsh/mesher.git",branch=branch)


    def requirements(self):
        self.requires( "esmf/8.1.0@CHM/stable" )

      

    # def _configure_cmake(self):
    #     cmake = CMake(self)

    #     cmake.configure(source_folder=self.source_folder)

    #     return cmake

    # def build(self):
    #     cmake = self._configure_cmake()
    #     cmake.build()
    #     cmake.test(target="check")

    # def package(self):
    #     cmake = self._configure_cmake()
    #     cmake.install()


    def imports(self):
        self.copy("*",src="",dst="", folder=True)  # From bin to bin
        # self.copy("*.dylib*", dst="lib", src="lib")  # From lib to bin
