def calculate(num1, num2, op):
  """
  Performs the chosen arithmetic operation on two numbers.

  """
  if op == "+":
    return num1 + num2
  elif op == "-":
    return num1 - num2
  elif op == "*":
    return num1 * num2
  elif op == "/":
    if num2 == 0:
      return "Error: Division by zero!"
    else:
      return num1 / num2
  else:
    return "Invalid operator!"

def main():
  """
  Prompts the user for input, performs calculations, and displays the result.
  """
  while True:
    try:
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      op = input("Choose operation (+, -, *, /): ")
      result = calculate(num1, num2, op)
      print(f"The result is: {result}")

      # Ask to continue or end
      choice = input("Do you want to perform another calculation? (y/n): ")
      if choice.lower() != "y":
        break
    except ValueError:
      print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
  main()
