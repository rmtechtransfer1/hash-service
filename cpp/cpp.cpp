// cpp.cpp : Defines the entry point for the application.
//
// Usage: CMAKE
// {repo root}/cmake -S . -B build -G Ninja
// {repo root}/cmake --build build --target cli_app -j
// {repo root}/build/bin/cli_app --message testing123
// Expected output: [INFO] [2025-08-09 23:49:13 UTC] b822f1cd2dcfc685b47e83e3980289fd5d8e3ff3a82def24d7d1d68bb272eb32
//
// To-Dos:
// Fix the warning C4996: 'gmtime': This function or variable may be unsafe.
// Validate CLI input is non-numerical, currently accepts numbers

#include <iostream>
#include <ctime>
#include <string>
#include "picosha2.h"
#include "cli_lib.h"  // declares getUtcTimestamp()

using namespace std;

// Main function to get user input and print the UTC timestamp
int main(int argc, char* argv[])
{
    // Validate input has exactly 3 inputs fail non-zero and return error code
    // To-Do: Validate input is non-numerical
    if (argc != 3 || std::string(argv[1]) != "--message") {
        std::cerr << "[ERROR] Usage: --message <text>\n";
        return 1;
    }

    // Get the msg from user input as well as UTC timestamp
    std::string message = argv[2];
    std::string timestamp = getUtcTimestamp();

    // SHA-256 with picoSHA2
    const std::string hash_hex = picosha2::hash256_hex_string(message);

    // Print the message, hash, and timestamp
    std::cout << "[INFO] " << timestamp << " " << hash_hex << '\n';
    return 0;
}
