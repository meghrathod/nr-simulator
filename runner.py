import environment,  eNB_environments
import main, matplotlib.pyplot as plt
import random
from UE import UE
from UE_ris import UE_ris
# TTT_range = [25, 50, 100, 200, 300, 400, 500]
# HYSTERESIS_range = [0, 3, 5, 7, 10, 12, 15, 17, 20]
HYSTERESIS_range = [2*x for x in range(10)]
TTT_range = [25]
# HYSTERESIS_range = [5]

x = []
h = []
p = []
# plt.plot(environment.h1, environment.x)

# fig, ax1 = plt.subplots()
# ax1.plot(h, x)
# ax2 = ax1.twinx()
# ax2.plot(h,p)
# # plt.xlabel("Hysteresis")
# # plt.ylabel("Handover Rate")


fig = plt.plot()
plt.ylabel("HO rate")
plt.xlabel("Hysteresis")
for i in range(100):
    TTT = 25
    environment.x = []
    print(i)
    print("RIS less...")
    for HYSTERESIS in HYSTERESIS_range:
        loc = random.randint(0,50000)
        # environment.TTT = TTT
        # environment.HYSTERESIS = HYSTERESIS
        # main.run_threads(TTT, HYSTERESIS)
        # environment.no_of_ho = 0
        # main.main(eNB_environments.eNBs_nr[1])
        # main.run_threads(eNB_environments.eNBs_nr[1], TTT, HYSTERESIS, UE(loc), eNB_environments.eNBs_nr[0])
        # print(environment.no_of_ho)
        # x.append(environment.no_of_ho)
        # h.append(HYSTERESIS)
        # p.append(environment.x)

        # plt.scatter(environment.no_of_ho, HYSTERESIS)
        # plt.scatter(environment.rsrp[-1], environment.ho_status[-1], marker=".", alpha=0.5)
        # print(len(environment.rsrp), len(environment.ho_status))
    # plt.plot(HYSTERESIS_range, environment.x, color="red")
    

    environment.x = []
    print("\nwith RIS")
    for HYSTERESIS in HYSTERESIS_range:
        environment.TTT = TTT
        environment.HYSTERESIS = HYSTERESIS
        environment.no_of_ho = 0
        main.run_threads_ris(eNB_environments.eNBs_nr_ris[1], eNB_environments.ris[1], TTT, HYSTERESIS, UE_ris(loc), "RIS")
    # plt.plot(HYSTERESIS_range, environment.x, color="blue")
        
        # print(environment.no_of_ho)
        # x.append(environment.no_of_ho)
        # h.append(HYSTERESIS)
        # p.append(environment.x)

        # plt.scatter(environment.no_of_ho, HYSTERESIS)
        # plt.scatter(environment.rsrp[-1], environment.ho_status[-1], marker=".", alpha=0.5)
        # print(len(environment.rsrp), len(environment.ho_status))



# # plt.plot(h, p)
# plt.show()

