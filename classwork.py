def main():
    user_input1 = userNum()
    user_input2 = userNum()
    calculator(user_input1, user_input2)


def userNum():
    return int(input("Enter a number: "))


def calculator(num1, num2):
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)


main()