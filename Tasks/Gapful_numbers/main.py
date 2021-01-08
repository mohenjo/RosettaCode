def is_gapful(num: int):
    divider: int = int(str(num)[0] + str(num)[-1])
    return num % divider == 0


def get_first_n_gapfuls(start_num: int, n: int):
    if start_num < 100:
        start_num = 100

    gapfuls = []
    curnum = start_num
    while len(gapfuls) < n:
        if is_gapful(curnum):
            gapfuls.append(curnum)
        curnum += 1

    return gapfuls


def do_task(start_num: int, numcount: int):
    print(f"First {numcount} gapful numbers ≥ {start_num}:")
    print(get_first_n_gapfuls(start_num, numcount))


def main():
    do_task(start_num=100, numcount=30)
    do_task(start_num=1_000_000, numcount=15)
    do_task(start_num=1_000_000_000, numcount=10)


if __name__ == '__main__':
    main()
