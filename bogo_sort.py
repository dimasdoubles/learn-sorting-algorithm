import random

def is_sorted(a):
    n = len(a)
    for i in range(n-1):
        if (a[i] > a[i+1]):
            return False
    return True


def main():
    a = [3, 4, 2, 6, 5, 7, 10]

    while not(is_sorted(a)):
        random.shuffle(a)

    print(a)


if __name__ == "__main__":
    main()
