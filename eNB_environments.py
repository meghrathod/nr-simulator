import random
from eNB import eNB
from ris import ris
from eNB_ris import eNB_ris
from utils.grapher import graph_rsrp
# Mix Environment
def util():
    return random.randint(0,100)


# NR Environment
en2_1 = eNB(2000,util(), "nr")
en2_2 = eNB(3000,util(), "nr")
en2_3 = eNB(5000, util(),"nr")
en2_4 = eNB(15000,util(), "nr")
en2_5 = eNB(25000,util(), "nr")
en2_6 = eNB(20000,util(), "nr")
en2_7 = eNB(16000,util(), "nr")
en2_8 = eNB(45000,util(), "nr")
en2_9 = eNB(10000,util(), "nr")
en2_10 = eNB(12000,util(), "nr")
eNBs_nr = ("NR", [en2_1, en2_2, en2_3, en2_4, en2_5, en2_6, en2_7, en2_8, en2_9, en2_10])



en1_1 = ris(3000)
en1_2 = ris(8000)
en1_3 = ris(17000)

# eNBs_mix1 = ("NR", [en1_1, en1_10])
ris = ("ris", [en1_1,  en1_2, en1_3])
# eNBs_mix1 = ("Ris", [en1_1, en1_2, en1_3, en1_4, en1_5, en1_6, en1_7, en1_8, en1_9])


en3_1 = eNB_ris(1000, util(), "nr")
en3_2 = eNB_ris(2000, util(), "nr")
en3_3 = eNB_ris(5000, util(), "nr")
en3_4 = eNB_ris(15000, util(), "nr")
en3_5 = eNB_ris(25000, util(), "nr")
en3_6 = eNB_ris(20000, util(), "nr")
en3_7 = eNB_ris(16000, util(), "nr")
en3_8 = eNB_ris(45000, util(), "nr")
en3_9 = eNB_ris(10000, util(), "nr")
en3_10 = eNB_ris(12000, util(), "nr")
eNBs_nr_ris = ("NR", [en3_1, en3_2, en3_3, en3_4, en3_5,
               en3_6, en3_7, en3_8, en3_9, en3_10])
# eNBs_nr = ("NR", [en2_1, en2_10])
# graph_rsrp(eNBs_nr)