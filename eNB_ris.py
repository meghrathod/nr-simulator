import math
import random
from typing import List

import environment
import utils
import utils.misc
from eNB import eNB
from ris import ris


class eNB_ris:
    """
    This class defines properties of a base station.
    It has a location, id, type and wavelength.
    """

    def __init__(self, x, ut, bs_type):
        self.util = ut
        self.ris = None
        self.free_elems = 10
        self.id = random.randint(0, 1000)
        self.location = x
        self.bs_type = bs_type  # "bs" or "bs-rs"
        self.wavelength = utils.misc.freq_to_wavelength(environment.FREQ_NR)

    def __str__(self):
        return "eNB located at %s of type: %s" % (self.location, self.bs_type)

    def get_location(self):
        return self.location

    def get_id(self):
        return self.id

    def get_type(self):
        return self.bs_type

    def set_location(self, x):
        self.location = x

    def set_ris(self, ris: ris):
        self.ris = ris

    def power_received(self, ueLocation):
        pt = utils.misc.calc_power_in_dbm(environment.PTX)
        pr_nr = pt
        if math.fabs(ueLocation - self.location) > 1:
            pr_nr /= math.fabs(ueLocation - self.location)
        return pr_nr

    def P_ris(self, ueLocation):
        ris = self.ris
        if ris is None:
            return Exception("BS not associated with ris")
        pt = utils.misc.calc_power_in_dbm(environment.PTX)
        pr_at_ris = pt
        if math.fabs(ris.get_location() - self.location) > 1:
            pr_at_ris /= math.fabs(ris.get_location() - self.location)

        pr_ris = 0.7 * pr_at_ris

        return self.power_received(ueLocation) + pr_ris
