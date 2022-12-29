#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):  # A function to create a Pascal's triangle of size n
  triangle = []  # Creating an empty list

  if n <= 0:  # Check if value of n is less than or equal to 0
    return triangle  # If so, return the empty list

  for row in range(1, n+1):  # Iterate over rows from 1 to n
    current_row = []  # Create an empty row

    for col in range(1, row+1):   # Iterate over columns from 1 to row
      if col == 1 or col == row:   # Check if column is first or last in the row
        current_row.append(1)   # If so, append 1
      else:   # Otherwise...
        above_left = triangle[row-2][col-2]   # Get the number above and left of the current cell
        above_right = triangle[row-2][col-1]   # Get the number above and right of the current cell

        current_row.append(above_left + above_right)   # Sum the numbers and append it to the current row

    triangle.append(current_row)   # Append current row to Pascal's triangle

  return triangle
