# 1. Functions are objects

def add_five(num):
  print(num + 5)
  
add_five(2)

# 2. Functions within functions

def add_five(num):
  def add_two(num:
      return num +2
              
  num_plus_two = add_two(num)
  print(num_plus_two + 3)

# add_two(7) can't use function outside of add_five           
              
add_five(10)
