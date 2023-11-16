#-*- coding: utf-8 -*-

"""
Copyright (c) 2023 LG Electronics Inc.
SPDX-License-Identifier: MIT
"""

import os
import pytest
import subprocess

@pytest.fixture(scope="session")
def unity(request):
    def cleanup():
        """
        if os.path.exists("report.out"):
            os.remove("report.out")
        if os.path.exists("report.xml"):
            os.remove("report.xml")
"""

    request.addfinalizer(cleanup)

    subprocess.check_call('gcc -DUNITY_INCLUDE_CONFIG_H -I. main.c ../src/unity.c -o report.out', shell=True)
    stdout = subprocess.check_output("./report.out", stderr=subprocess.STDOUT, shell=True).decode("utf-8")
    with open("report.xml", "r") as file:
        report = file.readlines()

    return stdout, report


def test_report_format(unity):
    stdout, report = unity
    assert '<?xml version="1.0" encoding="UTF-8"?>\n' in report
    assert '<testsuites>\n' in report
    assert '<testsuite>\n' in report
    assert '</testsuite>\n' in report
    assert '</testsuites>\n' in report

def test_with_message(unity):
    stdout, report = unity
    assert 'testWithMessage:INFO: TEST_MESSAGE' in stdout
    assert '<testcase classname="main.c" name="testWithMessage" />\n' in report

def test_passed_with_message(unity):
    stdout, report = unity
    assert 'testPassedWithMessage:INFO: TEST_PASS_MESSAGE' in stdout
    assert '<testcase classname="main.c" name="testPassedWithMessage" />\n' in report

def test_failed(unity):
    stdout, report = unity
    assert 'testFailed:FAIL' in stdout
    assert '<testcase classname="main.c" name="testFailed">\n' in report

def test_failed_with_message(unity):
    stdout, report = unity
    assert 'testFailedWithMessage:FAIL: TEST_FAIL_MESSAGE' in stdout
    assert '<testcase classname="main.c" name="testFailedWithMessage">\n' in report
    assert ' TEST_FAIL_MESSAGE\n' in report

def test_ignored(unity):
    stdout, report = unity
    assert 'testIgnored:IGNORE' in stdout
    assert '<testcase classname="main.c" name="testIgnored">\n' in report

def test_ignored_with_message(unity):
    stdout, report = unity
    assert 'testIgnoredWithMessage:IGNORE: TEST_IGNORE_MESSAGE' in stdout
    assert '<testcase classname="main.c" name="testIgnoredWithMessage">\n' in report
    assert ' TEST_IGNORE_MESSAGE\n' in report

def test_assert_boolean_failed(unity):
    stdout, report = unity
    assert 'testAssertBooleanFailed:FAIL: Expression Evaluated To FALSE' in stdout
    assert '<testcase classname="main.c" name="testAssertBooleanFailed">\n' in report
    assert ' Expression Evaluated To FALSE\n' in report

def test_assert_equal_failed(unity):
    stdout, report = unity
    assert 'testAssertEqualFailed:FAIL: Expected -1 Was 2' in stdout
    assert '<testcase classname="main.c" name="testAssertEqualFailed">\n' in report
    assert ' Expected -1 Was 2\n' in report

def test_assert_not_equal_failed(unity):
    stdout, report = unity
    assert 'testAssertNotEqualFailed:FAIL: Expected 1 to be not equal to 1' in stdout
    assert '<testcase classname="main.c" name="testAssertNotEqualFailed">\n' in report
    assert ' Expected 1 to be not equal to 1\n' in report

def test_assert_greater_than_failed(unity):
    stdout, report = unity
    assert 'testAssertGreaterThanFailed:FAIL: Expected 1 to be greater than 1' in stdout
    assert '<testcase classname="main.c" name="testAssertGreaterThanFailed">\n' in report
    assert ' Expected 1 to be greater than 1\n' in report

def test_assert_less_than_failed(unity):
    stdout, report = unity
    assert 'testAssertLessThanFailed:FAIL: Expected 1 to be less than 1' in stdout
    assert '<testcase classname="main.c" name="testAssertLessThanFailed">\n' in report
    assert ' Expected 1 to be less than 1\n' in report

def test_assert_greater_or_equal_failed(unity):
    stdout, report = unity
    assert 'testAssertGreaterOrEqualFailed:FAIL: Expected 1 to be greater than or equal to 2' in stdout
    assert '<testcase classname="main.c" name="testAssertGreaterOrEqualFailed">\n' in report
    assert ' Expected 1 to be greater than or equal to 2\n' in report

def test_assert_less_or_equal_failed(unity):
    stdout, report = unity
    assert 'testAssertLessOrEqualFailed:FAIL: Expected 2 to be less than or equal to 1' in stdout
    assert '<testcase classname="main.c" name="testAssertLessOrEqualFailed">\n' in report
    assert ' Expected 2 to be less than or equal to 1\n' in report

def test_assert_within_failed(unity):
    stdout, report = unity
    assert 'testAssertWithinFailed:FAIL: Values Not Within Delta 0 Expected 1 Was 2' in stdout
    assert '<testcase classname="main.c" name="testAssertWithinFailed">\n' in report
    assert ' Values Not Within Delta 0 Expected 1 Was 2\n' in report

def test_assert_array_within_failed(unity):
    stdout, report = unity
    assert 'testAssertArrayWithinFailed:FAIL: Values Not Within Delta 0 Element 1 Expected -1 Was -2' in stdout
    assert '<testcase classname="main.c" name="testAssertArrayWithinFailed">\n' in report
    assert ' Values Not Within Delta 0 Element 1 Expected -1 Was -2\n' in report

def test_assert_float_array_within_failed(unity):
    stdout, report = unity
    assert 'testAssertFloatArrayWithinFailed:FAIL: Element 1 Expected -0.1 Was -0.2' in stdout
    assert '<testcase classname="main.c" name="testAssertFloatArrayWithinFailed">\n' in report
    assert ' Element 1 Expected -0.1 Was -0.2\n' in report

def test_assert_equal_string_failed(unity):
    stdout, report = unity
    assert "testAssertEqualStringFailed:FAIL: Expected 'hello' Was 'world'" in stdout
    assert '<testcase classname="main.c" name="testAssertEqualStringFailed">\n' in report
    assert " Expected 'hello' Was 'world'\n" in report

def test_assert_equal_string_len_failed(unity):
    stdout, report = unity
    assert "testAssertEqualStringLenFailed:FAIL: Expected 'h' Was 'w'" in stdout
    assert '<testcase classname="main.c" name="testAssertEqualStringLenFailed">\n' in report
    assert " Expected 'h' Was 'w'\n" in report

def test_assert_equal_string_array_failed(unity):
    stdout, report = unity
    assert "testAssertEqualStringArrayFailed:FAIL: Element 1 Expected 'hello' Was 'world'" in stdout
    assert '<testcase classname="main.c" name="testAssertEqualStringArrayFailed">\n' in report
    assert " Element 1 Expected 'hello' Was 'world'\n" in report

def test_assert_equal_array_failed(unity):
    stdout, report = unity
    assert 'testAssertEqualArrayFailed:FAIL: Element 1 Expected -1 Was -2' in stdout
    assert '<testcase classname="main.c" name="testAssertEqualArrayFailed">\n' in report
    assert ' Element 1 Expected -1 Was -2\n' in report

def test_assert_each_equal_failed(unity):
    stdout, report = unity
    assert 'testAssertEachEqualFailed:FAIL: Element 1 Expected 1 Was -1' in stdout
    assert '<testcase classname="main.c" name="testAssertEachEqualFailed">\n' in report
    assert ' Element 1 Expected 1 Was -1\n' in report

def test_assert_equal_float_failed(unity):
    stdout, report = unity
    assert 'testAssertEqualFloatFailed:FAIL: Expected -1.23 Was 4.56' in stdout
    assert '<testcase classname="main.c" name="testAssertEqualFloatFailed">\n' in report
    assert ' Expected -1.23 Was 4.56\n' in report

def test_assert_equal_float_special_failed(unity):
    stdout, report = unity
    assert 'main.c:114:testAssertEqualFloatSpecialFailed:FAIL: Expected nan Was inf' in stdout
    assert '<testcase classname="main.c" name="testAssertEqualFloatSpecialFailed">\n' in report
    assert ' Expected nan Was inf\n' in report

def test_assert_float_not_within_failed(unity):
    stdout, report = unity
    assert 'testAssertFloatNotWithinFailed:FAIL: Expected -0.1 to be not equal to 0.1' in stdout
    assert '<testcase classname="main.c" name="testAssertFloatNotWithinFailed">\n' in report
    assert ' Expected -0.1 to be not equal to 0.1\n' in report

def test_assert_equal_hex8_failed(unity):
    stdout, report = unity
    assert 'testAssertEqualHex8Failed:FAIL: Expected 0x05 Was 0x01' in stdout
    assert '<testcase classname="main.c" name="testAssertEqualHex8Failed">\n' in report
    assert ' Expected 0x05 Was 0x01\n' in report

def test_assert_equal_uint16_failed(unity):
    stdout, report = unity
    assert 'testAssertEqualUInt16Failed:FAIL: Expected 32768 Was 1' in stdout
    assert '<testcase classname="main.c" name="testAssertEqualUInt16Failed">\n' in report
    assert ' Expected 32768 Was 1\n' in report

def test_assert_bits_failed(unity):
    stdout, report = unity
    assert 'testAssertBitsFailed:FAIL: Expected XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1 Was XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0' in stdout
    assert '<testcase classname="main.c" name="testAssertBitsFailed">\n' in report
    assert ' Expected XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1 Was XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0\n' in report

def test_assert_equal_memory_failed(unity):
    stdout, report = unity
    assert 'testAssertEqualMemoryFailed:FAIL: Memory Mismatch. Byte 0 Expected 0x61 Was 0x62' in stdout
    assert '<testcase classname="main.c" name="testAssertEqualMemoryFailed">\n' in report
    assert ' Memory Mismatch. Byte 0 Expected 0x61 Was 0x62\n' in report

def test_assert_not_null_failed(unity):
    stdout, report = unity
    assert 'testAssertNotNullFailed:FAIL: Expected Non-NULL' in stdout
    assert '<testcase classname="main.c" name="testAssertNotNullFailed">\n' in report
    assert ' Expected Non-NULL\n' in report
