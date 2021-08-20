def bubble_sort(a):
    n = len(a)

    for i in range(n):
        print(a)
        for j in range(n-i-1):
            if a[j] >= a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


def main():
    a = [1, 7, 4, 7, 4, 3, 2, 6, 9]
    bubble_sort(a)


if __name__ == "__main__":
    main()
