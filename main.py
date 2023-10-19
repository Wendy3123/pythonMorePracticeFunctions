#Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a,b,c):
    max = 0
    nums = [a,b,c]
    for x in nums : 
        if x > max:
            max = x
    print(max)
max_num(3,6,2)

#Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(*args):
    num = 1
    for x in args: 
        num = x*num
    return num
print(mult_list(2,10,10))

#Write a Python function called rev_string() to reverse a string.
def reverse(str):
    if len(str) == 0:           #base case
        return str
    else:
        return reverse(str[1:]) + str[0]        #recursive statement
print(reverse('wendy'))

#Write a Python function called num_within() to check whether a number falls in a given range.
#The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
#Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(num, start, end):
    result = False
    if num >= start and num <= end:
        result = True
    return result
print(num_within(3,2,4))
print(num_within(4,2,4))
print(num_within(13,2,4))
print(num_within(7,2,9))

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
#The function accepts the number n, the number of rows to print
#Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:                                 #base case
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)