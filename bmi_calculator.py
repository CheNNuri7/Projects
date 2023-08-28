'''Psuedocode:
weight - person's weight
height - person's height

calculate bmi

conditionals to check the bmi range using this website 
(https://www.cdc.gov/healthyweight/assessing/index.html#:~:text=If%20your%20BMI%20is%20less,falls%20within%20the%20obese%20range.)
'''

print("Hello, welcome to the BMI Calculator. Please enter your height and weight when prompted, and your results will be displayed.")

weight = int(input("Please enter your weight: "))
weight_type = input("Please indicate if you entered your weight in kg or lbs: ")
height = int(input("Please enter your weight: "))
height_type = input("Please indicate if you enter your height in inches or meters: ")

if weight_type == 'kgs':
    if height_type == 'meters':
        bmi = round(weight/(height**2))

if weight_type == 'lbs':
    if height_type == 'inches':
        new_weight = round(weight/2.20)
        new_height = round(height/39.4)
        bmi = round(weight/(height**2))

print(bmi)
