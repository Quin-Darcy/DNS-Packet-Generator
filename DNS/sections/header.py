from DNS.sections.utils import packet_utils as pu
import random

# Number of sections
SEC_NUM = 13
# List of section names
SEC_NAMES = ['ID', 'QR', 'OPCODE', 'AA', 'TC', 'RD', 'RA', 'Z', 'RCODE', 'QDCOUNT', 'ANCOUNT', 'NSCOUNT', 'ARCOUNT']
# List contains length (in bits) of each section in the header
SEC_LENS = [16, 1, 4, 1, 1, 1, 1, 3, 4, 16, 16, 16, 16]
# Flags indicating whether section will be default (0) or random(1)
SEC_DEFAULTS = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# List containing the default values of each section
SEC_DEFAULT_VALS = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] # explain meaning of these defaults
# Utility instance
util = pu.Util()


class Header:
    def __init__(self) -> None:
        self.sections = dict()
        self.bin_header = []
        self.hex_header = []
        self.sec_num = SEC_NUM
        self.sec_names = SEC_NAMES
        self.sec_lens = SEC_LENS

    def create_header(self) -> None:
        self.set_section_vals()
        self.set_bin_header()
        self.set_hex_header()

    def set_section_vals(self) -> None:
        for i in range(SEC_NUM):
            temp_sec = []
            if SEC_DEFAULTS[i] == 0:
                for j in range(SEC_LENS[i]):
                    temp_sec.append(str(0))
                temp_sec[-1] = str(SEC_DEFAULT_VALS[i])
                self.sections[SEC_NAMES[i]] = ''.join(temp_sec)
            else:
                for j in range(SEC_LENS[i]):
                    temp_sec.append(str(random.randint(0, 1)))
                self.sections[SEC_NAMES[i]] = ''.join(temp_sec)

    def set_bin_header(self) -> None:
        for key in self.sections:
            self.bin_header += self.sections[key]
        self.bin_header = ''.join(self.bin_header)

    def set_hex_header(self) -> None:
        self.hex_header = util.bin_to_hex(self.bin_header)

    def show_header(self) -> None:
        print('{:>8}'.format(8 * ' ' + 'HEADER:'))
        util.display(self.bin_header, self.hex_header, self.sections)
