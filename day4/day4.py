#!/usr/local/bin/python3

run_env = "test"  # test or prod

if run_env == "test":
    input = "day4inputtest.txt"
else:
    input = "day4input.txt"

with open(input) as blockstream:
    for row in blockstream:
        print(row.rstrip())
