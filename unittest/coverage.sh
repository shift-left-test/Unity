#!/bin/bash

gcc -DUNITY_INCLUDE_CONFIG_H -I. main.c ../src/unity.c --coverage -o report.out
./report.out
gcovr --root ../ --print-summary --html-details index.html
