from random import random

def randomise(a):
    N = len(a)
    for i in range(N):
        j = int(random() * (N - i) + i)
        t = a[i]
        a[i] = a[j]
        a[j] = t
# randomise

if __name__ == "__main__":
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    randomise(a)
    print a

