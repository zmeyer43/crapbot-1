cmake_minimum_required(VERSION 3.5)
project(crapbot)

include_directories(
  "./include"
  "/usr/local/include"
  "./cc")

set(CMAKE_CXX_FLAGS "-pthread -std=c++11 -Wall -O2 -g")

add_subdirectory(cc)
