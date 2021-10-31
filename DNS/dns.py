import packet


def main():
    domain = 'www.testing.com'
    IP = '142.250.191.46'
    p = packet.Packet()
    p.create_random_packet(domain)
    p.show_packet()

    hex_stream = p.hex_stream
    q = packet.Packet()
    q.create_response_from_stream(hex_stream, IP)
    q.show_packet()


if __name__ == '__main__':
    main()
