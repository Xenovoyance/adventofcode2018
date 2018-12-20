run_env = "prod"  # test or prod

if run_env == "test":
    input = "day2inputtest.txt"
else:
    input = "day2input.txt"

twos = 0
threes = 0

with open(input) as blockstream:
    for stream in blockstream:
        stream = stream.rstrip('\r\n')

        uniquevaluesinstream = []
        for x in stream:
            if x not in uniquevaluesinstream:
                uniquevaluesinstream.append(x)

        if run_env == "test":  # debugging, set flag at top
            print(stream)
            print(uniquevaluesinstream)

        updateTwos = False
        updateThrees = False

        for letter in uniquevaluesinstream:
            if stream.count(letter) == 2:
                updateTwos = True
            if stream.count(letter) == 3:
                updateThrees = True

        if updateTwos:
            twos += 1

        if updateThrees:
            threes += 1

        if run_env == "test":  # debugging, set flag at top
            print("Twos: " + str(twos))
            print("Threes: " + str(threes))

    print("Checksum: " + str(twos * threes))
