#challenge 1

def sum_to(n):
  nums = []
  for num in range(n):
    nums.append(num)
  nums.append(n)
  print(sum(nums))

sum_to(6)
sum_to(10)

#challenge 2

def largest(list):
  largest_num = max(list)
  print(largest_num)

largest([1,2,3,4,0])
largest([10,4,2,231,91,54])

#challenge3

def occurrences(string, char):
  num_chars = string.count(char)
  print(num_chars)

occurrences('fleep floop', 'e')
occurrences('fleep floop', 'p')
occurrences('fleep floop', 'ee')
occurrences('fleep floop', 'fe')

#challenge4

def product(*args):
  prod = 1
  for arg in args:
    prod *= arg
  print(prod)

product(-1, 4)
product(2, 5, 5)
product(4, 0.5, 5)