#Group members:
#Sena Foli-Mensah
#Ama Abrampah
#Alexis Addo

calculations = list()
# the code below prints the introductory menu
print("*****PYTHON CALCULATOR*****".center(40))
print("To enter your own calculation, enter: 1")
print("To view the menu, enter: 2")
print("To exit, enter: 0")
print("------------------------------------------------------")

#function for the calculator menu if user enters 2
def menu():
  print("To perform addition, enter: +")
  print("To perform subtraction, enter: -")
  print("To perform multiplication, enter: *")
  print("To perform division, enter: /")
  print("To perfom modulo operation, enter: %") 
  print("------------------------------------------------------")

#addition function
def add(calculations):
    result = sum(calculations)
    return round(result,2)

#subtraction function
def minus(calculations):
    result = calculations[0]
    calculations.pop(0)

    for num in calculations:
      result =  result - num

    return round(result,2)

#multiplication function
def multiply(calculations):
    result = 1
    for num in calculations:
      result *= num
    return round(result,2)

#division function
def division(calculations):
    result = 1
    for num in calculations:
      result = num / result
    return round(result,4)

#modulo function
def mod(calculations):
    result = calculations[0]
    calculations.pop(0)

    for num in calculations:
      result = result % num
    return round(result,4)
    


#list of user options
operations = ["+", "-", "*", "/", "%","1","2"]
user_choice = input("Enter 1 or 2 to continue or 0 to exit: ")

#the loop below executes when the user's choice is either 2 or 1.
while True:
  for option in operations:
    if user_choice == "2":
      menu()
      
      operation = str(input("Enter the sign for the operation you want to perform: "))
      no_of_numbers = int(input("How many numbers do you want to calculate? "))

      for count in range(no_of_numbers):
        number = float(input("Enter a number: "))
        calculations.append(number)


      for sign in operation:
        if operation == "+":
          print(add(calculations))
        elif operation == "-":
          print(minus(calculations))
        elif operation == "*":
          print(multiply(calculations))
        elif operation == "/":
          print(division(calculations))
        elif operation == "%":
          print(mod(calculations))
        else:
          print("I cannot perform this operation")
      calculations.clear()
      user_choice = input("Enter 1 or 2 to continue or 0 to exit: ")

    elif user_choice == "1":
       user_calc = input("Enter your desired input:  ")
       if "+" in user_calc:
         calc_list = user_calc.split("+")
         calc_list = [float(i) for i in calc_list]
         print(add(calc_list))
       elif "-" in user_calc:
         calc_list = user_calc.split("-")
         calc_list = [float(i) for i in calc_list]
         print(minus(calc_list))
       elif "*" in user_calc:
         calc_list = user_calc.split("*")
         calc_list = [float(i) for i in calc_list]
         print(multiply(calc_list))
       elif "/" in user_calc:
         calc_list = user_calc.split("/")
         calc_list = [float(i) for i in calc_list]
         print(division(calc_list))
       elif "%" in user_calc:
         calc_list = user_calc.split("%")
         calc_list = [float(i) for i in calc_list]
         print(mod(calc_list))
       else:
         print("I cannot perfom this operation")
         break
       user_choice = input("Enter 1 or 2 to continue or 0 to exit: ")
       
    elif user_choice == "0":
       break
 

    
    



