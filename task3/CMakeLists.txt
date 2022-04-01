cmake_minimum_required(VERSION 3.0)
project(SimpleLibrary)

if("${ARM_BUILD}" STREQUAL "ON")
	set(CMAKE_SYSTEM_PROCESSOR arm)

	set(CMAKE_C_COMPILER ${TOOLCHAIN}/"aarch64-linux-gnu-gcc")
	set(CMAKE_CXX_COMPILER ${TOOLCHAIN}/"aarch64-linux-gnu-g++")
	
	set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)
	set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")

include_directories(include)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${SimpleLibrary_SOURCE_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${SimpleLibrary_SOURCE_DIR}/lib)
add_subdirectory(src)
add_executable(Main main.cpp)
add_executable(MainLib main_lib.cpp)

target_link_libraries(MainLib buffer)
