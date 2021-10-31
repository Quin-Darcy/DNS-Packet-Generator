from DNS.sections.utils import packet_utils as pu
import random

# Number of sections
SEC_NUM = 6
# List of section names
SEC_NAMES = ['NAME', 'TYPE', 'CLASS', 'TTL', 'RDLENGTH', 'RDATA']
# List contains length (in bits) of each section in the answer
SEC_LENS = [32, 16, 16, 32, 16, 128]
# Flags indicating whether section will be default (0) or random(1)
SEC_DEFAULTS = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# List containing the default values of each section
SEC_DEFAULT_VALS = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] # explain meaning of these defaults
# Utility instance
util = pu.Util()

class Answer:
    def __init__(self):
