name1='tumelo'
height_m1=5
weight_kg1=80

name2='arthur'
height_m2=4
weight_kg2=55

name3='thapelo'
height_m3=2
weight_kg3=30

def bmi_calculator(name,height_m,weight_kg):
    bmi =weight_kg/ height_m **2
    print('bmi: ')
    print(bmi)
    if bmi < 25:
        return name + 'not overweight'
    else:
        return name + 'is overweight'
results1=bmi_calculator(name1,height_m1,weight_kg1)
results2=bmi_calculator(name2,height_m2,weight_kg2)
results3=bmi_calculator(name3,height_m3,weight_kg3)

