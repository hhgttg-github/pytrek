import random
import base as bs

########################################
### CLASS
########################################

class Enterprise():
    def __init__(self):
        self.xy     = bs.rand_pos()
        self.sxy    = bs.rand_pos()
        self.energy = bs.ENERGY_INIT

