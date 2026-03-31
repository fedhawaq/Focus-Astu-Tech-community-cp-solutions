S, T = map(int, input().split())
count = 0
for i in range(S+1):
    for j in range(S - a + 1):
        for k in range(S - a - b + 1):
            if a * b * c <= T:
                count += 1

print(count)
