# 구구단 (중첩 for문 + if문)

for i in range(2, 10):       # 2단부터 9단까지
    print(f"--- {i}단 ---")
    for j in range(1, 10):
        result = i * j
        if result % 2 == 0:
            print(f"{i} x {j} = {result} (짝수)")
        else:
            print(f"{i} x {j} = {result} (홀수)")
