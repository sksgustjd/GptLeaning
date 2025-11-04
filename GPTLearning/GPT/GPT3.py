# 1부터 100 사이의 합 중 짝수만 더하기

total = 0

for i in range(1, 101):  # 1 ~ 100
    if i % 2 == 0:
        total += i        # 짝수만 더하기

print("1부터 100까지 짝수의 합 =", total)
