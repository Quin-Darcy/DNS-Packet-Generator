from sections import header, question
from sections.utils import packet_utils as pu

# Utility instance
util = pu.Util()


class Packet:
    def __init__(self, p_type=0, domain='www.emoryward.com') -> None:
        self.header = header.Header(p_type)
        self.question = question.Question(domain)
        self.answer = None
        self.authority = None
        self.additional = None
        self.hex_stream = ''

    def create_packet(self) -> None:
        self.header.create_header()
        self.question.create_question()
        self.get_hex_stream()

    def get_hex_stream(self) -> None:
        self.hex_stream = self.header.hex_header + self.question.hex_question

    def show_packet(self) -> None:
        print('{:<8}'.format('FULL PACKET:'))

        split_str = util.get_split_str(self.hex_stream)
        print('{:>8} {} {:<8}'.format(8 * ' ' + 'HEX STREAM', ': ', split_str[0]))
        for i in range(1, len(split_str)):
            print('{:>16}'.format(22 * ' ' + split_str[i]))

        print('{:<8}'.format('PACKET COMPONENTS:'))
        self.header.show_header()
        self.question.show_question()
