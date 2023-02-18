import os
import random
import threading
from typing import List

import utils.Result
from eNB import eNB
from ris import ris
from Simulate_UE import Simulate_UE
from Simulate_UE_ris import Simulate_UE_ris
from UE import UE
from utils.Ticker import Ticker

# def main(enbs : List[eNB]) -> utils.Result.Result:

#     u1 = UE(0)
#     ticker = Ticker()
#     S = Simulate_UE(u1, enbs)
#     res = S.run(ticker, time=10000000)
#     file_name = "Results/results_corrected.xlsx"
#     file_name = os.path.join(os.path.dirname(__file__), file_name)
#     return res

# Define the number of threads to run


def main_ris(
    lock_mutex: threading.Lock,
    enbs: List[eNB],
    ris: List[ris],
    ttt,
    hys,
    u1: UE,
    bs: str,
) -> utils.Result.Result:
    # print("ue: %s",u1.get_id())
    enb2 = eNB(50000, random.randint(0, 100), "nr")
    ticker = Ticker()
    S = Simulate_UE_ris(u1, enbs, ris)
    res = S.run(ticker, time=10000000)
    lock_mutex.acquire()
    # try:
    #     file_name = "Results/results_corrected.xlsx"
    #     file_name = os.path.join(os.path.dirname(__file__), file_name)
    #     utils.Result.Result.save_to_file(res, file_name, "nr", ttt, hys, u1.get_eNB().location, bs)
    # finally:
    #     lock_mutex.release()
    return res


# # Define the number of threads to run
def run_threads_ris(
    enbs: List[eNB],
    ris: List[ris],
    time_to_trigger: int,
    hysteresis: int,
    ue: UE,
    bs: type,
):
    """
    This function runs the main function in multiple threads
    """
    # Create a lock to synchronize access to the file
    lock = threading.Lock()

    # Create a list of threads
    num_threads = 1
    threads = []
    for i in range(num_threads):
        # Create a new UE and eNBs object for each thread
        thread = threading.Thread(target=main_ris,
                                  args=(lock, enbs, ris, time_to_trigger,
                                        hysteresis, ue, bs))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish

    for thread in threads:
        thread.join()


def main(lock_mutex: threading.Lock, enbs: List[eNB], ttt, hys, u1: UE,
         bs: str) -> utils.Result.Result:
    # print("ue: %s",u1.get_id())
    enb2 = eNB(50000, random.randint(0, 100), "nr")
    ticker = Ticker()
    S = Simulate_UE(u1, enbs)
    res = S.run(ticker, time=10000000)
    lock_mutex.acquire()
    # try:
    #     file_name = "Results/results_corrected.xlsx"
    #     file_name = os.path.join(os.path.dirname(__file__), file_name)
    #     utils.Result.Result.save_to_file(res, file_name, "nr", ttt, hys, u1.get_eNB().location, bs)
    # finally:
    #     lock_mutex.release()
    return res


# # Define the number of threads to run
def run_threads(enbs: List[eNB], time_to_trigger: int, hysteresis: int, ue: UE,
                bs: type):
    """
    This function runs the main function in multiple threads
    """
    # Create a lock to synchronize access to the file
    lock = threading.Lock()

    # Create a list of threads
    num_threads = 1
    threads = []
    for i in range(num_threads):
        # Create a new UE and eNBs object for each thread
        thread = threading.Thread(target=main,
                                  args=(lock, enbs, time_to_trigger,
                                        hysteresis, ue, bs))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish

    for thread in threads:
        thread.join()
