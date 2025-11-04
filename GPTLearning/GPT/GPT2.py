# 점수에 따라 학점 매기기

scores = [95, 82, 67, 58, 73]

for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"점수: {score} → 학점: {grade}")
