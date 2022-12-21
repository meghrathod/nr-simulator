from random import seed

from environment import eNBs
from Simulator import Simulator
from UE import UE


def main():
    # Define the UEs
    u1 = UE(12000)

    seed(42)

    S = Simulator(u1, eNBs)
    S.run(time=10000)


main()
