#!/usr/bin/python3
import sys

total_sum = 0

for i in range(1, len(sys.argv)):
    total_sum += int(sys.argv[i])

print("{}".format(total_sum))
