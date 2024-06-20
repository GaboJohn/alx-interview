#!/usr/bin/python3

""" script that reads stdin line by line and computes metrics """

import sys


def printStats(length, size):
    """ Prints accumulated metrics """
    print("File size: {:d}".format(size))
    for n in sorted(length.keys()):
        if length[n] != 0:
            print("{}: {:d}".format(n, length[n]))


statusCodes_count = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                     "404": 0, "405": 0, "500": 0}

codes_count = 0
size = 0

try:
    for line in sys.stdin:
        if codes_count != 0 and codes_count % 10 == 0:
            printStats(statusCodes_count, size)

        total_list = line.split()
        codes_count += 1

        try:
            size += int(total_list[-1])
        except Exception:
            pass

        try:
            if total_list[-2] in statusCodes_count:
                statusCodes_count[total_list[-2]] += 1
        except Exception:
            pass
    printStats(statusCodes_count, size)


except KeyboardInterrupt:
    printStats(statusCodes_count, size)
    raise
