

dicc = {}

with open ("programs/csv/students.csv", "r", encoding="UTF-8") as f:
    line = 0
    for l in f:
        if line ==0:
            features = l.strip().split(",")
            for feature in features:     
                dicc[feature] = []

        else: 
            stats = l.strip().split(",")
            counter = 0
            for f in features:
                if stats[counter] != "":
                    dicc[f].append(stats[counter])
                counter+=1
        line +=1

print(dicc)
#count
for k,v in dicc.items():
    print(f"Count of {k}: {len(v)}")


#mean
def calculate_mean(feature:str):
    sum = 0
    for f in dicc[feature]:
        sum+=float(f)
    mean = sum / len(dicc[feature])
    print(f"mean {feature} is: {mean}")

calculate_mean("edad")
calculate_mean("nota")
calculate_mean("horas_estudio")

#missing values
#1. Calculate the nº of columns
n_columns = 6
#2. n_columns - len(list)
for k,v in dicc.items():
    print(f"Missing values in {k}: {n_columns - (len(v))}")

#calculate the mean
def calculate_median(feature:str) -> float:
    numbers = sorted(float(x) for x in dicc[feature])
    if len(numbers) % 2 != 0: 
        median = numbers[len(numbers) // 2]
        print(median)
        return median
    else: 
        value_1 = numbers[len(numbers) // 2]
        value_2 = numbers[(len(numbers) // 2) - 1]
        median = ((value_1) + (value_2)) / 2
        print(median)
        return median

calculate_median("edad")
calculate_median("horas_estudio")
calculate_median("nota")


#min and max:
def get_min_max(feature) ->tuple:
    numbers = sorted(float(x) for x in dicc[feature])
    return numbers[0], numbers[-1]

print(get_min_max("edad"))
print(get_min_max("nota"))
print(get_min_max("horas_estudio"))


