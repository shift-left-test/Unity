/*
 * Copyright (c) 2023 LG Electronics Inc.
 * SPDX-License-Identifier: MIT
 */

#include <math.h>
#include "../src/unity.h"

void setUp(void) {
}

void tearDown(void) {
}

void testWithMessage() {
  TEST_MESSAGE("TEST_MESSAGE");
}

void testPassedWithMessage() {
  TEST_PASS_MESSAGE("TEST_PASS_MESSAGE");
}

void testFailed() {
  TEST_FAIL();
}

void testFailedWithMessage() {
  TEST_FAIL_MESSAGE("TEST_FAIL_MESSAGE");
}

void testIgnored() {
  TEST_IGNORE();
}

void testIgnoredWithMessage() {
  TEST_IGNORE_MESSAGE("TEST_IGNORE_MESSAGE");
}

void testAssertBooleanFailed() {
  TEST_ASSERT(1 == 2);
}

void testAssertEqualFailed() {
  TEST_ASSERT_EQUAL_INT(-1, 2);
}

void testAssertNotEqualFailed() {
  TEST_ASSERT_NOT_EQUAL_INT(1, 1);
}

void testAssertGreaterThanFailed() {
  TEST_ASSERT_GREATER_THAN_INT(1, 1);
}

void testAssertLessThanFailed() {
  TEST_ASSERT_LESS_THAN_INT(1, 1);
}

void testAssertGreaterOrEqualFailed() {
  TEST_ASSERT_GREATER_OR_EQUAL_INT(2, 1);
}

void testAssertLessOrEqualFailed() {
  TEST_ASSERT_LESS_OR_EQUAL_INT(1, 2);
}

void testAssertWithinFailed() {
  TEST_ASSERT_INT_WITHIN(0, 1, 2);
}

void testAssertArrayWithinFailed() {
  int expected[] = {1, -1};
  int actual[] = {1, -2};
  TEST_ASSERT_INT_ARRAY_WITHIN(0, expected, actual, 2);
}

void testAssertFloatArrayWithinFailed() {
  float expected[] = {0.1, -0.1};
  float actual[] = {0.1, -0.2};
  TEST_ASSERT_FLOAT_ARRAY_WITHIN(0, expected, actual, 2);
}

void testAssertEqualStringFailed() {
  TEST_ASSERT_EQUAL_STRING("hello", "world");
}

void testAssertEqualStringLenFailed() {
  TEST_ASSERT_EQUAL_STRING_LEN("hello", "world", 1);
}

void testAssertEqualStringArrayFailed() {
  char* expected[] = {"hello", "hello"};
  char* actual[] = {"hello", "world"};
  TEST_ASSERT_EQUAL_STRING_ARRAY(expected, actual, 2);
}

void testAssertEqualArrayFailed() {
  int expected[] = {1, -1};
  int actual[] = {1, -2};
  TEST_ASSERT_EQUAL_INT_ARRAY(expected, actual, 2);
}

void testAssertEachEqualFailed() {
  int expected = 1;
  int actual[] = {1, -1};
  TEST_ASSERT_EACH_EQUAL_INT(expected, actual, 2);
}

void testAssertEqualFloatFailed() {
  TEST_ASSERT_EQUAL_FLOAT(-1.23, 4.56);
}

void testAssertEqualFloatSpecialFailed() {
  TEST_ASSERT_EQUAL_FLOAT(NAN, INFINITY);
}

void testAssertFloatNotWithinFailed() {
  TEST_ASSERT_FLOAT_NOT_WITHIN(1.0, -0.1, 0.1);
}

void testAssertEqualHex8Failed() {
  TEST_ASSERT_EQUAL_HEX8(5, 1);
}

void testAssertEqualUInt16Failed() {
  TEST_ASSERT_EQUAL_UINT16(0x8000, 0x0001);
}

void testAssertBitsFailed() {
  TEST_ASSERT_BITS(0x01, 1, 0);
}

void testAssertEqualMemoryFailed() {
  char expected = 'a';
  char actual = 'b';
  TEST_ASSERT_EQUAL_MEMORY(&expected, &actual, sizeof(char));
}

void testAssertNotNullFailed() {
  TEST_ASSERT_NOT_NULL(NULL);
}

int main(int argc, char* argv[]) {
  UNITY_BEGIN();

  RUN_TEST(testWithMessage);
  RUN_TEST(testPassedWithMessage);
  RUN_TEST(testFailed);
  RUN_TEST(testFailedWithMessage);
  RUN_TEST(testIgnored);
  RUN_TEST(testIgnoredWithMessage);

  RUN_TEST(testAssertBooleanFailed);
  RUN_TEST(testAssertEqualFailed);
  RUN_TEST(testAssertNotEqualFailed);
  RUN_TEST(testAssertGreaterThanFailed);
  RUN_TEST(testAssertLessThanFailed);
  RUN_TEST(testAssertGreaterOrEqualFailed);
  RUN_TEST(testAssertLessOrEqualFailed);
  RUN_TEST(testAssertWithinFailed);
  RUN_TEST(testAssertArrayWithinFailed);
  RUN_TEST(testAssertFloatArrayWithinFailed);
  RUN_TEST(testAssertEqualStringFailed);
  RUN_TEST(testAssertEqualStringLenFailed);
  RUN_TEST(testAssertEqualStringArrayFailed);
  RUN_TEST(testAssertEqualArrayFailed);
  RUN_TEST(testAssertEachEqualFailed);
  RUN_TEST(testAssertEqualFloatFailed);
  RUN_TEST(testAssertEqualFloatSpecialFailed);
  RUN_TEST(testAssertFloatNotWithinFailed);
  RUN_TEST(testAssertEqualHex8Failed);
  RUN_TEST(testAssertEqualUInt16Failed);
  RUN_TEST(testAssertBitsFailed);
  RUN_TEST(testAssertEqualMemoryFailed);
  RUN_TEST(testAssertNotNullFailed);

  UNITY_END();

  return 0;
}
