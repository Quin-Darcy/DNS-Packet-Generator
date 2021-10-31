from DNS.sections.utils import packet_utils as pu

util = pu.Util()


class Answer:
    def __init__(self, ip):
        self.ip = ip
        self.sections = dict()
        self.bin_answer = ''
        self.hex_answer = ''

        self.set_answer()
        self.set_bin_answer()
        self.set_hex_answer()

    def set_answer(self):
        ip = self.ip.split('.')
        ip = [str(hex(int(a)))[2:] for a in ip]
        ip = [util.hex_to_bin(a) for a in ip]
        ip = ''.join(ip)
        self.sections = {"NAME": util.hex_to_bin('c00c'),
                         "TYPE": "0000000000000001",
                         "CLASS": "0000000000000001",
                         "TTL": "00000000000000000000000000010110",
                         "RDLENGTH": "0000000000000100",
                         "RDATA": ip}

    def set_bin_answer(self) -> None:
        for key in self.sections:
            self.bin_answer += self.sections[key]

    def set_hex_answer(self) -> None:
        self.hex_answer = util.bin_to_hex(self.bin_answer)

    def show_answer(self) -> None:
        print('{:>8}'.format(8 * ' ' + 'ANSWER:'))
        util.display(self.bin_answer, self.hex_answer, self.sections)
