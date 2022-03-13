cmake_minimum_required(VERSION 3.10)
project(libr)
include_directories(.) 
add_library(libr SHARED lib.cpp)
