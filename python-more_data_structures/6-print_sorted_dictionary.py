#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for keygen in sorted(a_dictionary):
        print(f"{keygen}: {a_dictionary[keygen]}")
