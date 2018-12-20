#!/usr/local/bin/python3

run_env = "prod"  # test or prod

total_width = 0
total_height = 0

w, h = 2000, 2000;
matrix = [[0 for x in range(w)] for y in range(h)]
overlaps = 0

if run_env == "test":
    input = "day3inputtest.txt"
else:
    input = "day3input.txt"

with open(input) as blockstream:
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
print("Overlaps: " + str(overlaps))
