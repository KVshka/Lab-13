import csv

with open('titanic.csv', newline='', encoding='utf-8') as f: #открываем файл
    max_alive_passengers = 0
    max_passengers = 0
    min_alive_passengers = 0
    min_passengers = 0    
    max=-1
    min = 999
    reader = csv.DictReader(f) #читаем строку
    for row in reader:
        if row['Age'] != '' and row['Sex'] == 'male' and row['Embarked'] == 'Q': #проверяем выполнение условия
            if max < float(row['Age']): #определяем, является ли возраст пассажира больше максимального
                max = float(row['Age'])
                max_passengers = 1
                if row['Survived'] == '1':
                    max_alive_passengers = 1
            elif max == float(row['Age']): #определяем, является ли возраст пассажира максимальным
                max_passengers += 1
                if row['Survived'] == '1':
                    max_alive_passengers = +1

            if min > float(row['Age']): #определяем, является ли возраст пассажира меньше минимального
                min = float(row['Age'])
                min_passengers = 1
                if row['Survived'] == '1':
                    min_alive_passengers = 1
            elif min == float(row['Age']): #определяем, является ли возраст пассажира минимальным
                min_passengers += 1
                if row['Survived'] == '1':
                    min_alive_passengers += 1
            print(row)

print("Всего в порту Квинстаун село " + str(min_passengers+max_passengers) + " мужчин минимального и максимального возраста")
print("Из них выжило " + str(min_alive_passengers+max_alive_passengers))
