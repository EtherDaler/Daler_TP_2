cmake_minimum_required(VERSION 3.10)
project(task2 LANGUAGES CXX)


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

add_custom_target(
  run ALL
  BYPRODUCTS ${PROJECT_SOURCE_DIR}/A/index.h
  COMMAND python3 ${PROJECT_SOURCE_DIR}/A/preparing.py ${PROJECT_SOURCE_DIR}/A/index.h
  COMMENT "Generating header file index.h"
)

add_dependencies(C run)
add_subdirectory(B)
target_link_libraries(C mainlib)

add_executable(CTest C/main_test.cpp C/test.cpp)
add_dependencies(CTest run)
target_link_libraries(CTest mainlib)
target_link_libraries(CTest ${GTEST_LIBRARIES} pthread)


enable_testing()
