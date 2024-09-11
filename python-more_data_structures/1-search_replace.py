#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for show in my_list:
        if show == search:
            new_list.append(replace)
        else:
            new_list.append(show)
    return new_list
