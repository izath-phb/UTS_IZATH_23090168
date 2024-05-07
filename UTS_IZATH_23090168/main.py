from bmi_calculator import calculate_bmi, get_bmi_category

def main():
    print("Selamat datang di Kalkulator BMI")
    weight = float(input("Masukkan berat badan (kg): "))
    height = float(input("Masukkan tinggi badan (m): "))
    
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    
    print(f"BMI Anda: {bmi:.2f}")
    print(category)

if __name__ == "__main__":
    main()

