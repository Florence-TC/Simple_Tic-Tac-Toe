number = input()
print([(int(number[i]) + int(number[i + 1])) / 2 for i in range(len(number) - 1)])
