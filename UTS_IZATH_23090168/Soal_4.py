def calculate_bmi(berat, tinggi):
    bmi = berat / (tinggi ** 2)
    return bmi


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Keterangan: Berat badan kurang"
    elif 18.5 <= bmi < 24.9:
        return "Keterangan: Berat badan normal"
    elif 25 <= bmi < 29.9:
        return "Keterangan: Kelebihan berat badan"
    else:
        return "Keterangan: Obesitas"

