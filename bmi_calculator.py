# BMI Calculator - 

print("===== BMI CALCULATOR =====")

try:
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be greater than 0.")

    else:
        bmi = weight / (height ** 2)

        print(f"\nYour BMI is: {bmi:.2f}")

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print("Category:", category)

except ValueError:
    print("Please enter valid numbers.")