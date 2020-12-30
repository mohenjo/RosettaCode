def main():
    nth = 30
    print(f"value at {nth}th is {get_thue_morse_value_at(nth)}")

    print("first 100 sequence:")
    seq = thue_morse_seq()
    for _ in range(100):
        print(next(seq), end="")


def get_thue_morse_value_at(nth: int) -> int:
    # https://en.wikipedia.org/wiki/Thue%E2%80%93Morse_sequence
    # Direct definitin 참조
    return bin(nth)[2:].count("1") % 2


def thue_morse_seq():
    nth = 0
    while True:
        yield get_thue_morse_value_at(nth)
        nth += 1


if __name__ == '__main__':
    main()
