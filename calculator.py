logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
my_dict={"+":add,"-":sub,"*":multiply,"/":divide}
print(my_dict["*"](4,8))


def calculator():
    print(logo)
    num1 = float(input("Enter the first number"))
    should_continue=True
    while should_continue:
        for i in my_dict:
            print(i)
        symbol=input("enter a symbol: ")
        num2=float(input("Enter the second number"))
        ans=my_dict[symbol](num1,num2)
        print(f"{num1}{symbol}{num2}= {ans}")
        choice =input("do you wanna continue y/n").lower
        if choice=="y":

            option=input("wanna continue with same ans or start new type y/n").lower()
            if option=="y":
                num1=ans
            else:
                print("/n"*100)
                calculator()
        else:
            should_continue=False
calculator()
