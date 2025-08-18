# CMakeList.txt : CMake project for cpp, include source and define
# project specific logic here.
#
cmake_minimum_required(VERSION 3.21)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Put all runtime binaries in <build>/bin for Docker access
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Allow -DBINARY_NAME=... (default to cli_app)
if(NOT DEFINED BINARY_NAME)
  set(BINARY_NAME cli_app)
endif()       

# Includes pichosha2 / other 3rd party
set(THIRDPARTY_DIR ${CMAKE_SOURCE_DIR}/thirdparty)
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

## Create libray target containing reusable helper functions (e.g.timestamp), shared across targets
add_library(cli_lib cli_lib.cpp)
target_include_directories(cli_lib
  PUBLIC  ${CMAKE_CURRENT_SOURCE_DIR}
  PRIVATE ${THIRDPARTY_DIR}
)

# Executable named from BINARY_NAME
add_executable(${BINARY_NAME} cpp.cpp)
target_link_libraries(${BINARY_NAME} PRIVATE cli_lib)
target_include_directories(${BINARY_NAME} PRIVATE
  ${THIRDPARTY_DIR}
  ${CMAKE_CURRENT_SOURCE_DIR}
)
install(TARGETS ${BINARY_NAME} RUNTIME DESTINATION bin)
## Link with cli_lib to get access to helper functions (e.g. timestamp), dependency for cli_app and nothing further
target_link_libraries(cli_app PRIVATE cli_lib)
## Include picosha2 headers in cli_app target, gets path only
target_include_directories(cli_app PRIVATE ${picosha2_include_dir})

# Google Test Framework setup
include(FetchContent)

FetchContent_Declare(
  googletest
    URL https://github.com/google/googletest/archive/refs/tags/v1.17.0.tar.gz
)

# For Windows: prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()

# GoogleTest executable target (cli_tests)
add_executable(cli_tests tests/cli_tests.cpp)
## Link with cli_lib to get access to helper functions 
target_link_libraries(cli_tests
  PRIVATE
    GTest::gtest_main
    cli_lib
)
## Link with cli_lib to get access to picosha2
target_include_directories(cli_tests
  PRIVATE
    ${CMAKE_SOURCE_DIR}/thirdparty
    ${CMAKE_CURRENT_SOURCE_DIR}  
)

include(GoogleTest)
gtest_discover_tests(cli_tests)
