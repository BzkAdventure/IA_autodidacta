

from multiprocessing import Value
from operator import is_, truediv


dicc = {}

with open ("programs/csv/students.csv", "r", encoding="UTF-8") as f:
    line = 0
    row_counter = 0
    for l in f:
        if line ==0:
            features = l.strip().split(",")
            for feature in features:    
                if feature == "ciudad":
                    dicc[feature] = {}
                else:
                    dicc[feature] = []
                row_counter+=1
        else: 
            stats = l.strip().split(",")
            counter = 0
            for f in features:
                if stats[counter] != "":
                        if f == "ciudad":
                            city = stats[counter]
                            if city in dicc[f]:
                                dicc[f][city] += 1
                            else:
                                dicc[f][city] = 1
                        else:
                            dicc[f].append(stats[counter])
                counter+=1
        line +=1

def is_numerical(feature)->bool:
    for k in dicc[feature]:
        try: 
            f = float(k)
        except ValueError:
            return False
    return True



print(dicc)
#count
for k,v in dicc.items():
    print(f"Count of {k}: {len(v)}")


#mean
def calculate_mean(feature:str):
    sum = 0
    if is_numerical(feature):
        for f in dicc[feature]:
            sum+=float(f)
        mean = sum / len(dicc[feature])
        print(f"mean {feature} is: {mean}")
    else:
        for v in dicc[feature].values():
            sum+=v
        mean = sum / len(list)

            

calculate_mean("edad")
calculate_mean("nota")
calculate_mean("horas_estudio")

#missing values
#1. Calculate the nº of columns
#2. n_columns - len(list)
for k,v in dicc.items():
    if k =="ciudad":
        lenght = 0
        for num in v.values():
            lenght += num
        print(f"Missing values in {k}: {row_counter - (lenght - 1)}")

    print(f"Missing values in {k}: {row_counter - (len(v) -1)}")

#calculate the mean
def calculate_median(feature:str) -> float:
    if is_numerical:
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


