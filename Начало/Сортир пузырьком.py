#сортировка в порядке не возрастания. Если элементы не одинаковые не переставляем
#если элемент слева больше чем с права меняем их местами
#cсамый большой элемент всплывет как пузырёк в конце


# for i in range(len(mas) - 1)

n = 10
mas = [39, 78, 56, 36, 24, 25, 15, 15, 89, 71]

#n = int(input())                      #число которое вводится с клавиатуры
#mas = list(map(int, input().split()))    #считываем списк. вводим значения в одну строчку
count = 0                               #переменная считает замены

for run in range(n-1):      #добавляем внешний цикл (он отвечает за кол-во обходов сколько обходов столько повтторяем цикл ниже)
    for i in range(n-1-run):                   #не берем последний элемент тк у него нет соседа с права
        #print(f"сейчас сравниваем {mas[i]} c {mas[i + 1]}")
        if mas[i]>mas[i+1]:
            count += 1
            mas[i], mas[i+1] = mas[i+1], mas[i]            #меняем позиционно
    #print(mas)                            #видим массив после каждого обхода
print(*mas)          #для того чтобы норм вывелось оператор(*) делает распоковку представляет элементы по отдельности
print(count)

#for i in mas:                 #обходим элементы массива в цикле for
#    print(i, end=' ')         #выводим по элементно каждое значение end ставим равным побелу
#print()                       #count выводится в одной строчке поэтому еще один принт
#print(count)

#получается что обходов на 1 меньше чем кол-во элементов

#оптимизация: после каждого обхода находится один пузырек и уже конец массива сравнивать не надо ( в 11ю строку можно(f"сейчас сравниваем {mas[i]} c {mas[i+1]}") )
#поэтому можно в 10й строчке за счет переменной run уменьшать проход

#сложность реализаций внешний на внутренний цыкл (n-1)(n-1) == n**2
#наш оптимизированный код:  (n-1)**n/2 но по правилам вычисления сложости алгоритмов n**2



# temp = num[j]
# num[j] = num[j+1]
# num[j+1] = temp