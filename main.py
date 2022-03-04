from art import logo

# number_1 = float(input("Whats first number: "))
# number_2 = float(input("Whats second number: "))
# print("+\n-\n*\n/ \n") 
# operators = input("Pick operation: ")
def add(n1, n2):
  """ adding two numbers"""
  return n1 + n2
def substract(n1,n2):
  return n1- n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2
operations = {"+": add,
             "-": substract,
             "*": multiply,
             "/": divide}
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  
  for key in operations:
    print(key)
  continue_calculation = True
  while continue_calculation:
    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    ask_another = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator: ")
    if ask_another == "y":
      num1 = answer
    else:
      continue_calculation = False
      calculator()

calculator()
