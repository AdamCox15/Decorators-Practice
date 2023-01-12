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

# 3. Returning functions from functions
 
def get_math_function(operation): # + or - 
    def add(num1, num2):
        return num1 + num2
    def sub(num1 - num2):
        return num1 - num2
    
    if operation == '+':
       return add
    elif operation == '-':
         return sub
              
add_function = get_math_funtion('+')
sub_function = get_math_function('-')

# 4. Decorating a function
              
def title_decorator(print_name_function):
    def wrapper():
        print("Professor:")
        print_name_function()
    return wrapper
              
def print_my_name():
    print("Adam")
              
              
decorated_function = title_decorator(print_my_name) 
              
decorated_function()
              
              
              
              
              
              
              
              
              
              
              
              
