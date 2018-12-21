#!/usr/local/bin/python3

run_env = "prod"  # test or prod

if run_env == "test":
    input = "day3inputtest.txt"
else:
    input = "day3input.txt"

with open(input) as blockstream:
    total_width = 0
    total_height = 0

    w, h = 1000, 1000
    matrix = [[0 for x in range(w)] for y in range(h)]
    overlaps = 0
    for row in blockstream:
        item = row.rstrip('\r\n').split(" ")
        id = item[0].strip("#")
        from_left = int(item[2].split(",")[0])
        from_top = int(item[2].split(",")[1].rstrip(':'))
        width = int(item[3].split("x")[0])
        height = int(item[3].split("x")[1])

        if (from_left + width) > total_width:
            total_width = from_left + width

        if (from_top + height) > total_height:
            total_height = from_top + height

        for y in range(from_top, from_top + height):
            for x in range(from_left, from_left + width):
                if matrix[y][x] != 0:
                    if matrix[y][x] != 'x':
                        matrix[y][x] = 'x'
                        overlaps += 1
                else:
                    matrix[y][x] = id

print("Size of grid is: " + str(total_height) + "x" + str(total_width))
print("Overlaps: " + str(overlaps))  # Part 1 answer

with open(input) as blockstream:
    total_width = 0
    total_height = 0

    for row in blockstream:
        item = row.rstrip('\r\n').split(" ")
        id = item[0].strip("#")
        from_left = int(item[2].split(",")[0])
        from_top = int(item[2].split(",")[1].rstrip(':'))
        width = int(item[3].split("x")[0])
        height = int(item[3].split("x")[1])

        if (from_left + width) > total_width:
            total_width = from_left + width

        if (from_top + height) > total_height:
            total_height = from_top + height

        area_patch = height * width

        for y in range(from_top, from_top + height):
            for x in range(from_left, from_left + width):
                if matrix[y][x] != 'x':
                    area_patch -= 1

        if area_patch == 0:
            print("Non-overlapping patch: " + str(id))  # Part 2 answer
