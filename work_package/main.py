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
        if N > 1:
            for i in range(N):
                a.append(randint(1, 99))
            print(a)
            bubble_sort.bubble_sort(a)
        else:
            print("Для сортировки списка укажите длину списка больше 1.")


if __name__ == "__main__":
    main()
