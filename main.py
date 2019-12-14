import bubble_sort
from random import randint


def main():
    a = []
    N = input("Введите длину списка для сортировки:")
    try:
        Val = int(N)
    except (TypeError, ValueError):
        print("Введено неверное значение!")
    else:
        N = Val
        if N > 1:
            for i in range(N):
                a.append(randint(1, 99))
            print(a)
            bubble_sort.bubble_sort(a)
        else:
            print("Для сортировки списка укажите длину списка больше 1.")
            #     assert bubble_sort.bubble_sort([12]) == [12]
            #     assert bubble_sort.bubble_sort([56, 56, 47]) == [47, 56, 56]
            #     assert bubble_sort.bubble_sort([17, 25, -67, 74, -89]) == [-89, -67, 17, 25, 74]
            #     assert bubble_sort.bubble_sort([56, 9, 48, 99, 13, 67]) == [9, 13, 48, 56, 67, 99]