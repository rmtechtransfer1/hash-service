#include "cli_lib.h"
#include <ctime>
#include <string>
#include "picosha2.h"

// Get the current timestamp and convert to UTC time
std::string getUtcTimestamp() {
    time_t timestamp = time(NULL);
    struct tm datetime = *gmtime(&timestamp); // To-Do: Fix warning C4996

    // Prepare space for timestamp, format, and print
    char output[35];
    (void)strftime(output, sizeof(output), "[%Y-%m-%d %H:%M:%S UTC]", &datetime);

    return std::string(output);

}

std::string sha256_hex(const std::string& s) {
    return picosha2::hash256_hex_string(s);
}