import random
import matplotlib.pyplot as plt
import math
import decimal
from numpy.random import choice

def main():
    initCap = float(input("Enter initial capital: "))
    target = float(input("Enter target capital: "))
    prob = float(input("Enter probability of win in %: "))/100


    # Calculating probability of success and number of bets before bankruptcy or success

    if prob != 0.5:
        Pr = (((1-prob/prob)**initCap - 1)/((1-prob/prob)**target - 1))
        Ex = (((((1-prob/prob)**initCap - 1)/((1-prob/prob)**target - 1))*target - 100)/(prob-(1-prob)))
    else:
        Pr = initCap / target
        Ex = initCap*(target - initCap)

    print("Probability of success  — ", Pr)
    print("Approximate number of bets — ", Ex)


    # Simulating random walk with step equal to 5% of initial cap

    xposition = [initCap]
    bets = [initCap*(-0.05), initCap*0.05]
    random_walk = random.choices(bets, weights=[1-prob, prob], k=365)
    for i in random_walk:
        initCap += i
        if initCap <= 0:
            break
        xposition.append(initCap)

    plt.plot(xposition)
    plt.xlabel('Number of bets', fontsize=18)
    plt.ylabel('Capital', fontsize=16)
    plt.show()

if __name__ == "__main__":
    main()