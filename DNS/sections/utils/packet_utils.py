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
