from DNS.sections.utils import packet_utils as pu
import random

# Number of sections
SEC_NUM = 3
# List of section names
SEC_NAMES = ['QNAME', 'QTYPE', 'QCLASS']
# List containing length (in bits) of each section
SEC_LENS = [0, 16, 16]
# Flags indicating whether section will be default (0) or random (1)
SEC_DEFAULTS = [0, 0, 0]
# Default values for each section
SEC_DEFAULT_VALS = [0, 1, 1]    # explain meaning of these defaults
# Utility instance
util = pu.Util()


class Question:
    def __init__(self, domain) -> None:
        self.domain = domain
        self.sections = dict()
        self.bin_question = []
        self.hex_question = []

    def create_question(self) -> None:
        self.set_qname()
        self.set_qtype()
        self.set_qclass()
        self.set_bin_question()
        self.set_hex_question()

    def set_qname(self) -> None:
        split_domain = self.domain.split('.')
        char_counts = [len(ch) for ch in split_domain]
        qname = ''
        for i in range(len(char_counts)):
            qname += util.int_to_bin(char_counts[i])
            qname += util.str_to_bin(split_domain[i])
        qname += 8 * '0'
        self.sections['QNAME'] = qname

    def set_qtype(self) -> None:
        qtype = []
        if SEC_DEFAULTS[1] == 0:
            for i in range(SEC_LENS[1]):
                qtype.append('0')
            qtype[-1] = str(SEC_DEFAULT_VALS[1])
            self.sections['QTYPE'] = ''.join(qtype)
        else:
            qtype = ''
            for i in range(SEC_LENS[1]):
                qtype += str(random.randint(0, 1))
            self.sections['QTYPE'] = qtype

    def set_qclass(self) -> None:
        qclass = []
        if SEC_DEFAULTS[2] == 0:
            for i in range(SEC_LENS[2]):
                qclass.append('0')
            qclass[-1] = str(SEC_DEFAULT_VALS[1])
            self.sections['QCLASS'] = ''.join(qclass)
        else:
            qclass = ''
            for i in range(SEC_LENS[1]):
                qclass += str(random.randint(0, 1))
            self.sections['QCLASS'] = qclass

    def set_bin_question(self) -> None:
        for key in self.sections:
            self.bin_question += self.sections[key]
        self.bin_question = ''.join(self.bin_question)

    def set_hex_question(self) -> None:
        self.hex_question = util.bin_to_hex(self.bin_question)

    def show_question(self) -> None:
        print('{:>8}'.format(8 * ' ' + 'QUESTION:'))
        util.display(self.bin_question, self.hex_question, self.sections)

