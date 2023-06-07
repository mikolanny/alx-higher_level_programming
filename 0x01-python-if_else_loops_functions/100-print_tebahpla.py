#!/usr/bin/python3
i = 0
for i in range(90, 64, -1):
    print("{:c}".format(i + 32) if i % 2 == 0 else "{:c}".format(i), end="")
