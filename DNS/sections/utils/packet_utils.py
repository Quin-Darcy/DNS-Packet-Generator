from .. import *


class Util:
    @staticmethod
    def get_split_str(in_str) -> list:
        split = []
        temp_byte = ''
        for i in range(len(in_str)):
            if i != 0 and i % 16 == 0:
                split.append(temp_byte)
                temp_byte = ''
            temp_byte += in_str[i]
        split.append(temp_byte)
        return split

    @staticmethod
    def bin_to_hex(bin_str) -> str:
        return '%0*x' % ((len(bin_str) + 3) // 4, int(bin_str, 2))

    @staticmethod
    def hex_to_bin(hex_str) -> str:
        return bin(int('1'+hex_str, 16))[3:]

    @staticmethod
    def make_header_from_stream(head_str):
        temp_head = header.Header()
        current_bit = 0
        for i in range(temp_head.sec_num):
            key = temp_head.sec_names[i]
            temp_sec = head_str[current_bit:current_bit+temp_head.sec_lens[i]]
            current_bit += temp_head.sec_lens[i]
            temp_head.sections[key] = ''.join(temp_sec)

        temp_head.sections["QR"] = '1'
        temp_head.sections["TC"] = '0'
        temp_head.sections["RA"] = '1'
        temp_head.sections["ANCOUNT"] = '0000000000000001'

        temp_head.set_bin_header()
        temp_head.set_hex_header()

        return temp_head

    def make_question_from_stream(self, qstn_str):
        temp_qstn = question.Question()
        hex_head = self.bin_to_hex(qstn_str)
        null_byte = False
        index = 0
        while not null_byte and index != len(hex_head):
            if hex_head[index] == '0' and hex_head[index+1] == '0':
                null_byte = True
                index += 1
            else:
                index += 1

        temp_qstn.sections = {"QNAME": self.hex_to_bin(qstn_str[:index]),
                              "QTYPE": self.hex_to_bin(qstn_str[index:index + 16]),
                              "QCLASS": self.hex_to_bin(qstn_str[index + 16:index + 32])}

        temp_qstn.set_bin_question()
        temp_qstn.hex_question = self.bin_to_hex(qstn_str)

        return temp_qstn

    @staticmethod
    def str_to_bin(reg_str) -> str:
        l, m = [], []
        for i in reg_str:
            l.append(ord(i))
        for i in l:
            m.append(str(int(bin(i)[2:])))
        for i in range(len(m)):
            if len(m[i]) < 8:
                padding = 8 - len(m[i])
                m[i] = padding * '0' + m[i]
        m = ''.join(m)

        return m

    @staticmethod
    def int_to_bin(num) -> str:
        bin_num = format(num, "b")
        if len(bin_num) < 8:
            pad = 8 - len(bin_num)
            bin_num = pad * '0' + bin_num

        return bin_num

    def display(self, bin_str, hex_str, secs) -> None:
        print('{:<24}'.format(16 * ' ' + 28 * '-'))
        split_str = self.get_split_str(bin_str)
        print('{:<24} {} {:<24}'.format(16 * ' ' + 'BINARY', ': ', split_str[0]))
        for i in range(1, len(split_str)):
            print('{:>28}'.format(28 * ' ' + split_str[i]))

        print('')
        split_str = self.get_split_str(hex_str)
        print('{:<24} {} {:<24}'.format(16 * ' ' + 'HEX', ': ', split_str[0]))
        for i in range(1, len(split_str)):
            print('{:>28}'.format(28 * ' ' + split_str[i]))

        print('{:<24}'.format(16 * ' ' + 28 * '-'))
        for key in secs:
            split_str = self.get_split_str(secs[key])
            print('{:<24} {} {:<24}'.format(16 * ' ' + key, ': ', split_str[0]))
            for i in range(1, len(split_str)):
                print('{:>28}'.format(28 * ' ' + split_str[i]))
        print('{:<24}'.format(16 * ' ' + 28 * '-'))
