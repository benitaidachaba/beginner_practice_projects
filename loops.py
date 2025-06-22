num_rows = 5

for i in range(1, num_rows + 1):
  print(" " * (num_rows - i), end="")  # Print spaces for left alignment
  # Outer loop controls the number of rows
  for asterisk_count in range(1, i + 1):
    # Inner loop prints asterisks for each row
    print("*" * i, end="")  # Print asterisks for the current row
  print()  # Print an empty line to move to the next row after printing all asterisks in the current row