

operators = ['+','-','/','x','*']

def main():
    user_input = input("Enter whatever you want to calculate")

    for num in user_input:
        n = num.strip()
        for operator in operators:
            if operator==n:
                print("opearator")

if (__name__ == "__main__"):
    main()