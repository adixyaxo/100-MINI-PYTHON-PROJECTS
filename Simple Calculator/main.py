# This is a simple calculator made to do operation on two numbers

def main():
    while True:
            try:
                user_input = input("DO THE OPERATIONS BELOW :: ")
                if user_input == "quit":
                    break
                user_i = user_input.strip()
                number1 = 0
                for value in user_i:
                    if value != '+' or value != '-' or value != '*' or value != '/' or value != 'x' or value != ' ':
                        number1 = number1*10 + int(value)
                    else:
                        break
                print(number1)
            except ValueError:
                print("Please Enter numbers only")
            except ZeroDivisionError:
                print("You cannot perform division by zero")
                

if __name__ == "__main__":
    main()