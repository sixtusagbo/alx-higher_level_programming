#!/usr/bin/python3
for letters in range(97, 123):
    if letters == ord('e') or letters == ord('q'):
        continue
    print("{:c}".format(letters), end="")
