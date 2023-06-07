#!/usr/bin/python3
def remove_char_at(s, n):
    result = ""

    for i in range(len(s)):
        if i == n:
            continue
        result += s[i]

    return (result)
