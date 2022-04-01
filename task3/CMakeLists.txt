cmake_minimum_required(VERSION 3.0)

set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")
set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)

if(${ARM_BUILD})

	if("${TOOLCHAIN}" STREQUAL "")
        	message(FATAL_ERROR "Need toolchain for compiling")
    	endif()
    	
	set(CMAKE_SYSTEM_PROCESSOR arm)

	set(CMAKE_C_COMPILER ${TOOLCHAIN}/"aarch64-linux-gnu-gcc")
	set(CMAKE_CXX_COMPILER ${TOOLCHAIN}/"aarch64-linux-gnu-c++")
	
	set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${SimpleLibrary_SOURCE_DIR}/bin-arm)
	set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${SimpleLibrary_SOURCE_DIR}/lib-arm)
else()
	set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${SimpleLibrary_SOURCE_DIR}/bin)
	set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${SimpleLibrary_SOURCE_DIR}/lib)
	
endif()

project(SimpleLibrary)

include_directories(include)

add_subdirectory(src)
add_executable(Main main.cpp)
add_executable(MainLib main_lib.cpp)

target_link_libraries(MainLib buffer)

install(TARGETS Main MainLib
	RUNTIME DESTINATION bin
	LIBRARY DESTINATION lib
	PUBLIC_HEADER DESTINATION include)
