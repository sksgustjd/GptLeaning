# 리스트에서 양수만 골라내기

numbers = [-3, 0, 7, -1, 5, -9, 8]

positive_nums = []  # 양수를 담을 리스트

for n in numbers:
    if n > 0:
        positive_nums.append(n)
    else:
        print(f"{n}은(는) 양수가 아닙니다.")

print("양수만 모은 리스트:", positive_nums)
