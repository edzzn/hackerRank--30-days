import os
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.

# Print the sum of the double variables on a new line.

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.

#!/bin/python3


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    i2 = int(input())

    d2 = float(input())
    s2 = str(input())
    fptr.write(str(i2 + i) + '\n')
    fptr.write(str(d + d2) + '\n')
    fptr.write(str(s + s2) + '\n')

    fptr.close()
