numbers = [int(n) for n in input()]
running_total = []
total = 0

for num in numbers:
    total += num
    running_total.append(total)

print(running_total)
