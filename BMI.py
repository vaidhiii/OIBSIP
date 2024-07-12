def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")

    try:
        weight = float(input("Please enter your weight in kilograms: "))
        height = float(input("Please enter your height in meters: "))

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive values.")

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"This is classified as: {category}")

    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
