def tinh_bmi(weight: float, height: float) -> tuple[float, str]:
    bmi = round(weight / (height ** 2), 2)
    if bmi < 18.5:
        type = "Gầy (Thiếu cân)"
    elif bmi < 24.9:
        type = "Bình thường (Lý tưởng)"
    elif bmi < 29.9:
        type = "Thừa cân"
    else:
        type = "Béo phì"
    return bmi, type

bmi, result = tinh_bmi(55, 1.65)
print(f"[Bài 2] Cân nặng 55kg, Cao 1.65m -> BMI: {bmi} ({result})")



