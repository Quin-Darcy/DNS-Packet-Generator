from sections import header, question, answer
from sections.utils import packet_utils as pu

# Utility instance
util = pu.Util()


class Packet:
    def __init__(self) -> None:
        self.header = None
        self.question = None
        self.answer = None
        self.hex_stream = ''
        self.ip = ''

    def create_random_packet(self, domain) -> None:
        self.header = header.Header()
        self.question = question.Question(domain)
        self.header.create_header()
        self.question.create_question()
        self.get_hex_stream()

    def create_response_from_stream(self, in_stream, ip) -> None:
        self.ip = ip
        self.hex_stream = in_stream
        bin_stream = util.hex_to_bin(in_stream)
        bin_head = bin_stream[:96]
        bin_qstn = bin_stream[96:]

        self.header = util.make_header_from_stream(bin_head)
        self.question = util.make_question_from_stream(bin_qstn)
        self.answer = answer.Answer(self.ip)

    def get_hex_stream(self) -> None:
        self.hex_stream = self.header.hex_header + self.question.hex_question
        if self.answer:
            self.hex_stream += self.answer.hex_answer

    def show_packet(self) -> None:
        print('{:<8}'.format('FULL PACKET:'))

        split_str = util.get_split_str(self.hex_stream)
        print('{:>8} {} {:<8}'.format(8 * ' ' + 'HEX STREAM', ': ', split_str[0]))
        for i in range(1, len(split_str)):
            print('{:>16}'.format(22 * ' ' + split_str[i]))

        print('{:<8}'.format('PACKET COMPONENTS:'))
        self.header.show_header()
        self.question.show_question()
        if self.answer:
            self.answer.show_answer()
