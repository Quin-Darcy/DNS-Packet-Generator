import packet

DOMAIN = 'www.emoryward.com'
IP = '142.250.191.46'


def main():
    p = packet.Packet()
    p.create_random_packet(DOMAIN)
    p.show_packet()

    hex_stream = p.hex_stream
    q = packet.Packet()
    q.create_response_from_stream(hex_stream, IP)
    q.show_packet()


if __name__ == '__main__':
    main()
