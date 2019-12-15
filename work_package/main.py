from work_package import bubble_sort
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
        for i in range(N):  # Создание списка длинной N
            a.append(randint(1, 99))  # из случайных значений диапазона
        print(a)  # отображаем исходный список
        bubble_sort.bubble_sort(a)  # выполняем сортировку
        print(a)  # отображаем отсортированный список


if __name__ == "__main__":
    main()
