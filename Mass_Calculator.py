import math

# Female Body Fat Calculator
def body_fat_female(age, height_in, weight_kg, neck, waist, hip):
    bf_percent = (
        163.205 * math.log10(waist + hip - neck)
        - 97.684 * math.log10(height_in)
        - 78.387
    )
    fat_mass_kg = weight_kg * (bf_percent / 100)
    lean_mass_kg = weight_kg - fat_mass_kg
    
    return bf_percent, fat_mass_kg, lean_mass_kg


# Male Body Fat Calculator
def body_fat_male(age, height_in, weight_kg, neck, waist):
    bf_percent = (
        86.010 * math.log10(waist - neck)
        - 70.041 * math.log10(height_in)
        + 36.76
    )
    fat_mass_kg = weight_kg * (bf_percent / 100)
    lean_mass_kg = weight_kg - fat_mass_kg
    
    return bf_percent, fat_mass_kg, lean_mass_kg


# Interactive Program
def main():
    print("""
    ——————————————————————————————————————————————
        Body Fat Calculator (U.S. Navy Method)  
    ——————————————————————————————————————————————
    """)
    gender = input("Enter your Gender (Male/Female): ").strip().lower()
    
    if (gender != "female") and (gender != "male"):
        print("Invalid Gender Input!🫤 \nPlease Enter 'male' or 'female'.")
    
    age = int(input("Enter your Age: "))
    height_ft = int(input("Enter your Height (feet): "))
    height_in_extra = float(input("Enter extra inches if any: "))
    height_in = height_ft * 12 + height_in_extra
    weight_kg = float(input("Enter your Weight (Kg): "))
    neck = float(input("Enter your Neck Circumference (inches): "))
    waist = float(input("Enter your Waist Circumference (inches): "))

    if gender == "female":
        hip = float(input("Enter your Hip Circumference (inches): "))
        bf, fat, lean = body_fat_female(age, height_in, weight_kg, neck, waist, hip)
    elif gender == "male":
        bf, fat, lean = body_fat_male(age, height_in, weight_kg, neck, waist)
    
    print("""
    —————————————————————————————
        Results for your Body
    —————————————————————————————
    """)
    print(f"Body Fat Percentage: {bf:.2f}%")
    print(f"Fat Mass: {fat:.2f} Kg")
    print(f"Lean Mass: {lean:.2f} Kg")


if __name__ == "__main__":
    main()
