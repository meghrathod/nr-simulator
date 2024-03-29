import math
import random

import environment
import utils
import utils.misc


class eNB:
    """
    This class defines properties of a base station.
    It has a location, id, type and wavelength.
    """

    def __init__(self, x, bs_type):
        self.id = random.randint(0, 1000)
        self.location = x
        self.bs_type = bs_type  # "nr" or "lte"
        if self.bs_type == "nr":
            self.wavelength = utils.misc.freq_to_wavelength(
                environment.FREQ_NR)
        elif self.bs_type == "lte":
            self.wavelength = utils.misc.freq_to_wavelength(
                environment.FREQ_LTE)

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

    def calc_RSRP(self, ueLocation):
        """
        This function calculates the Received Signal Strength of the base station in dB
        This value is calculated using the Friis equation, i.e. RSS = Ptx - Gtx - Grx - L
        :param ueLocation: Location of the UE
        :return: RSRP(Reference Signal Received Power ) in dBm

        Here it is assumed that Gtx = Grx = 0 dB (Gains of the transmitter and receiver)
        """
        pt = utils.misc.calc_power_in_dbm(environment.PTX)

        if self.location != ueLocation:
            rsrp = pt - (
                20
                * math.log10(
                    4
                    * math.pi
                    * math.fabs(self.location - ueLocation)
                    / self.wavelength
                )
            )
        else:
            rsrp = 0
        return rsrp
