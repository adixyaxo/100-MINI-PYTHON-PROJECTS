# This is a simple calculator made to do operation on two numbers

def main():
    while True:
            try:
                number_1 = int(input("PLEASE ENTER THE FIRST NUMBER  ::  "))
                number_2 = int(input("PLEASE ENTER THE SECOND NUMBER  ::  "))
                operation = input("ENTER THE OPERATION YOU WANT TO PERFORM\n1.Addition :: +\n2.Subtraction :: -\n3.Multiplication :: x or *\n4.Division :: /\nENTER exit TO LEAVE/EXIT THE PROGRAMME")
                operation = operation.strip().lower()
                if operation == '+' or operation == '1' or operation == 'add' or operation == 'addition':
                    print(number_1+number_2)
                elif operation == '-' or operation == '2' or operation == 'subract' or operation == 'sub' or operation == 'subtraction':
                    print(number_1-number_2)
                elif operation == '*' or operation == '2' or operation == 'x' or operation == 'mul' or operation == 'multiplication' or operation == 'multiply':
                    print(number_1*number_2)
                elif operation == '/' or operation == '2' or operation == 'division' or operation == 'div' or operation == 'divide':
                    print(number_1/number_2)
                elif operation == 'exit' or operation == 'leave':
                    break
                else :
                    print("WRONG CHOICE PLEASE ENTER AGAIN")
            except ValueError:
                print("Please Enter numbers only")
            except ZeroDivisionError:
                print("You cannot perform division by zero")
                

if __name__ == "__main__":
    main()