from utils.misc import gigahertz_to_megahertz

# DEFINE constants for the environment
FREQ_NR = gigahertz_to_megahertz(25)  # MHz
FREQ_LTE = gigahertz_to_megahertz(2.5)  # MHz
TTT = 25  # ms
HYSTERESIS = 20  # dB
PTX = 10  # mW
TICKER_INTERVAL = 10  # ms
A3_OFFSET = 0  # dB
MIN_SPEED = 0.1  # m/ms
MAX_SPEED = 0.5  # m/ms
MIN_PAUSE = 10  # ms
MAX_PAUSE = 100  # ms
