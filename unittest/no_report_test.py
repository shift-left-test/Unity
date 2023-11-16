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
        if os.path.exists("no-report.out"):
            os.remove("no-report.out")
        if os.path.exists("no-report.xml"):
            os.remove("no-report.xml")

    request.addfinalizer(cleanup)

    subprocess.check_call('gcc -DUNITY_XML_REPORT=\\"no-report.xml\\" -I. main.c ../src/unity.c -o no-report.out', shell=True)
    subprocess.check_output("./no-report.out", stderr=subprocess.STDOUT, shell=True).decode("utf-8")

def test_no_report(unity):
    assert not os.path.exists("no-report.xml")
