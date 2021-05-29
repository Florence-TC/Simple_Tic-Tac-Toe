height = int(input())
drawing = []
for i in range(height):
    drawing.append((height - i - 1) * " " + (2 * i + 1) * "#" + (height - i - 1) * " ")
print("\n".join(drawing))
