cmake_minimum_required(VERSION 3.10)
project(task2 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")


set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/lib)
set(FILES C/main.h C/main.cpp)
include_directories(${PROJECT_SOURCE_DIR})

find_package(GTest REQUIRED)

if(NOT GTest_FOUND)
  message(SEND_ERROR "Failed to find gtest library")
  return()
else()
  include_directories(${GTEST_INCLUDE_DIRS})
endif()

add_executable(C ${FILES})

execute_process(
	COMMAND python3 ${PROJECT_SOURCE_DIR}/A/preparing.py ${PROJECT_SOURCE_DIR}/A/index.h
	WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/A
	)

add_subdirectory(B)
target_link_libraries(C mainlib)

add_executable(CTest C/main_test.cpp)
target_link_libraries(CTest Threads::Threads gtest gtest_main)


enable_testing()
