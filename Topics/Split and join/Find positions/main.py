# put your python code here
sequence = input().split()
x = input()
output = [str(i) for i in range(len(sequence)) if sequence[i] == x]
if not output:
    print("not found")
else:
    print(" ".join(output))
