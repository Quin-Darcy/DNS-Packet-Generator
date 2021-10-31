import packet


def main():
    domain = 'www.testing.com'
    p = packet.Packet(0, domain)
    p.create_packet()
    p.show_packet()


if __name__ == '__main__':
    main()
