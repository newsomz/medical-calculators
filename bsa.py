import math

'''Have user input patient's height and weight'''
height = input("Please enter your height (cm): ")
weight = input("Please enter your weight (kg): ")

'''Convert user input from str -> float'''
height_num = float(height)
weight_num = float(weight)

def mosteller_bsa(height_num, weight_num):
    '''
    float, float -> (float)

    Computes a patient's body surface area from height (cm) and weight (kg)
    based on the Mosteller formula

    >>> mosteller_bsa(162.0, 50.0)
    1.5
    '''

    return math.sqrt((height_num * weight_num)/3600)

def dubois_bsa(height_num, weight_num):
    '''
    float, float -> (float)

    Computes a patient's body surface area from height (cm) and weight (kg)
    based on the Dubois formula

    >>> dubois_bsa(162.0, 50.0)
    1.514681
    '''

    return 0.20247*(math.pow((height_num/100),0.725))*(math.pow(weight_num,0.425))

print("Mosteller:",  mosteller_bsa(height_num, weight_num))
print("DuBois:", dubois_bsa(height_num, weight_num))
