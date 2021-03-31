num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
for i in range(num1, num2 + 1):
    string = str(i)
    for j in range(32, 100 + 1):
        if i == j * j:

            if int(string[0]) % 2 == 0 and int(string[1]) % 2 == 0 and int(string[2]) % 2 == 0 and int(
                    string[3]) % 2 == 0:
                print(i)
