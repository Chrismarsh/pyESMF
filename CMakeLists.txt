cmake_minimum_required(VERSION 3.16)
project(pyESMF)

if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")

    message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
    file(DOWNLOAD "https://raw.githubusercontent.com/conan-io/cmake-conan/develop/conan.cmake"
            "${CMAKE_BINARY_DIR}/conan.cmake")

    if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
        message(ERROR "Failed to download")
    endif()
endif()

include(${CMAKE_BINARY_DIR}/conan.cmake)

if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    set(CONAN_LIB_STD "libstdc++11")
    message(STATUS "Detected gnu compiler, setting compiler.libcxx=${CONAN_LIB_STD}")
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang" OR "${CMAKE_CXX_COMPILER_ID}" STREQUAL "AppleClang")
    set(CONAN_LIB_STD "libc++")
    message(STATUS "Detected clang compiler, setting compiler.libcxx=${CONAN_LIB_STD}")
endif ()

option(FORCE_BUILD "Build ESMF from source" OFF)
set(BUILD_POLICY "missing")

if(FORCE_BUILD)
    message(STATUS "Building ESMF from source...")
    set(BUILD_POLICY "all")
endif()

message(STATUS "Targetting ESMF version = ${ESMF_VERSION}")

conan_add_remote(NAME CHM
        URL https://api.bintray.com/conan/chrismarsh/CHM
        )
conan_cmake_run(CONANFILE conanfile.py
                OPTIONS pyESMF:esmf_version=${ESMF_VERSION}
                SETTINGS compiler.cppstd=14
                SETTINGS compiler.libcxx=${CONAN_LIB_STD}
                BASIC_SETUP
                CMAKE_TARGETS
                KEEP_RPATHS
                NO_OUTPUT_DIRS
                BUILD "${BUILD_POLICY}")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

install(DIRECTORY ${CMAKE_BINARY_DIR}/esmf
            DESTINATION ${CMAKE_INSTALL_PREFIX})


