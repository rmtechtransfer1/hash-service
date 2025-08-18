#include <gtest/gtest.h>
#include <regex>
#include <string>
#include "picosha2.h"
#include "cli_lib.h"   

TEST(HashTest, HappyPath_KnownVector_test123) {
    // SHA-256("test123")
    const std::string expected =
        "b822f1cd2dcfc685b47e83e3980289fd5d8e3ff3a82def24d7d1d68bb272eb32";
    const std::string msg = "test123";
    EXPECT_EQ(sha256_hex(msg), expected);
}

TEST(HashTest, FailurePath_WrongHash) {
    const std::string wrongHash = "simplywronghash";
    const std::string msg = "abc";
    EXPECT_NE(sha256_hex(msg), wrongHash);
}

TEST(TimeTest, UtcFormat) {
    const std::string ts = getUtcTimestamp();
    std::regex re(R"(^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]$)");
    EXPECT_TRUE(std::regex_match(ts, re)) << "ts=" << ts;
}