# CMakeList.txt : Top-level CMake project file, do global configuration
# and include sub-projects here.
#
# Fixing console warning on suboptimal version 
cmake_minimum_required (VERSION 3.21)

project ("hash-service-app")

if(NOT DEFINED BINARY_NAME)
  set(BINARY_NAME cli_app)
endif()

enable_testing()

# Include sub-projects.
add_subdirectory ("cpp")
