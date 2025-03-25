from common.imperial_conversions import ImperialConversion
import math

def get_user_age():
    age = input("Enter your age: ")
    return age

def get_user_gender():
    gender = input("Enter your gender (M or F): ").strip().upper()
    return gender

def get_user_activity_level():
    activity_level = (
        input(
            "Enter your activity level (sedentary, lightly_active, moderately_active, very_active, super_active): "
        )
        .strip()
        .lower()
    )
    activity_multipliers = {
        "sedentary": 1.2,
        "lightly_active": 1.375,
        "moderately_active": 1.55,
        "very_active": 1.725,
        "super_active": 1.9,
    }
    return activity_multipliers[activity_level]

def calculate_BMR(gender, weight, height, age):
    bmr = 0
    if gender == "M":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == "F":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return bmr

def calculate_TDEE(bmr):
    activity_level = get_user_activity_level()
    tdee = bmr * activity_level
    return tdee

def main():
    inches = input("Enter your height in inches: ")
    pounds = input("Enter weight in pounds: ")
    converter = ImperialConversion(inches, pounds)

    centimeters = converter.inches_to_centimeters()
    kilograms = converter.pounds_to_kilos()
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (M or F): ").strip().upper()
    bmr = calculate_BMR(gender, kilograms, centimeters, age)
    tdee = calculate_TDEE(bmr)
    deficit = tdee - bmr
    print("")
    print("--------------------------- YOUR RESULTS ---------------------------")
    print(f"Your BMR : {bmr:.2f} kcal/day")
    print(f"Your Total Daily Energy Expenditure (TDEE): {tdee:.2f} kcal/day.")
    print("+-----------+------------+")
    print("|    BMR    |    TDEE    |")
    print("+-----------+------------+")
    print(f"|  {bmr:.2f}  |  {tdee:.2f}   |")
    print("+-----------+------------+")
    print("")
    print(f"Achieving BMR will put you in a {deficit:.2f} calorie deficit.")

# This ensures that the main function only runs when the script is executed directly
if __name__ == "__main__":
    main()
