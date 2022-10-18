choice = int(input("Which system do you want to use? 1) Standard (Weight in pounds, height in feet) 2) Metric(Weight in KG and height in cm"))
weight = float(input("Enter your weight"))
height = float(input("Enter your height"))
if (choice==1):
    weight = weight/2.205
    height = height/3.281
else:
    height = height/100
    
def cal_BMI(weight,height):
    BMI = (weight)/(height**2)
    return BMI
    
print(float(cal_BMI(weight,height)))
