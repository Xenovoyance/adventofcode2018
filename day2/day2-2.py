#!/usr/local/bin/python3

run_env = "prod"  # test or prod

if run_env == "test":
    input = "day2inputtest.txt"
else:
    input = "day2input.txt"


def checksumCompare(_string1, _string2):  # return the number of differences between the string
    charposition = 0
    differences = 0
    for _letter in _string1:
        if _letter != _string2[charposition]:
            differences += 1
        charposition += 1
    if differences == 1:
        print(_string1 + "/" + _string2)
        return 1
    else:
        return 0



with open(input) as blockstream:
    for stream in blockstream:
        stream = stream.rstrip('\r\n')
        with open(input) as blockstream2:
            for stream2 in blockstream2:
                checksumCompare(stream, stream2.rstrip('\r\n'))

                # cvgywxqubnuaefmslkjdrpfzyi/cvgywxqubnuaefmsldjdrpfzyi -> cvgywxqubnuaefmsljdrpfzyi
