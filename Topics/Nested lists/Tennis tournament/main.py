n = int(input())
results = [input().split() for _ in range(n)]
print([player[0] for player in results if player[1] == "win"])
print(len([player[1] for player in results if player[1] == "win"]))
