########################################
### CONSTANT
########################################

FIELD_WIDTH = 10
FIELD_SIZE  = FIELD_WIDTH * FIELD_WIDTH
FIELD_LAST  = FIELD_SIZE - 1

STAR_MAX    = 9
BASE_MAX    = 9
KLINGON_MAX = 20

ENERGY_INIT = 1000

########################################
### FUNCTION
########################################

def to_1d(x,y):
    return(y*FIELD_SIZE+x)

def to_2d(i):
    return(divmod(i, FIELD_SIZE))

def rand_pos():
    return(random.randint(0,FIELD_LAST))