#len - кол-во элементов в нашем списке

mas = list(map(int, input().split()))
#count = 0

for i in range(len(mas) - 1):
    for j in range(len(mas) - 1 - i):
        if mas[j] > mas[j + 1]:
            # count += 1
            mas[j], mas[j + 1] = mas[j + 1], mas[j]


print(*mas)
# print(count)