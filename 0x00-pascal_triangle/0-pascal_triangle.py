#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    if n <= 0:
        return []
    final_list = [[1]]
     for x in range(n-1):
         temp = [0] + final_list[-1] + [0]
         new_list = []
         for y in range(len(final_list[-1]) + 1):
            new_list.append(temp[y] + temp[y+1])
        final_list.append(new_list)
    return final_list

