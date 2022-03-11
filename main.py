def BMI(bmi):
    if(bmi < 18.5):
        return "Underweight"
    elif(bmi >= 18.5 and bmi < 25):
        return "Normal Weight"
    elif(bmi >= 25.1 and bmi < 30):
        return "Overweight"
    elif(bmi >= 30):
        return "Obese"
    return "Error"

def calcBMI(height ,weight):
    weight *= .45
    height *= .025
    height = height * height
    bmi = weight/height
    return (bmi)

def main():
    loop = True
    while(loop):
        try:
            height = input("What is your height in inches?")
            height = int(height)
            weight = input("What is your weight in pounds?")
            weight = int(weight)
            bmi = calcBMI(height, weight)
            print ("Your BMI is ", bmi, " : ", BMI(bmi))
        except:
            print("Error")
            continue
