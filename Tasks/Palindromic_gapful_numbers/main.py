import math


def _is_gapful(anumber: int) -> bool:
    divider = int(str(anumber)[0] + str(anumber)[-1])
    return anumber % divider == 0


def _is_palindromic(anumber: int) -> bool:
    return str(anumber) == str(anumber)[::-1]


def _is_gapful_and_palindromic(anumber: int) -> bool:
    return _is_palindromic(anumber) and _is_gapful(anumber)


def generate_series(series_length: int, endwith: int) -> list[int]:
    curnum = 100 + endwith
    rst = []
    while len(rst) < series_length:
        if _is_gapful_and_palindromic(curnum):
            rst.append(curnum)
        curnum += 10
    return rst


def main():
    length = 20
    print(f"The first {length} palindromic gapful numbers (>= 100) end with:")
    for endwith in range(1, 10):
        rst = generate_series(length, endwith)
        print(f"{endwith}: {rst}")

    print()
    length = 100
    last = 15
    print(f"The last {last} palindromic gapful numbers (>= 100) out of {length} end with:")
    for endwith in range(1, 10):
        rst = generate_series(length, endwith)
        print(f"{endwith}: {rst[-last:]}")


if __name__ == '__main__':
    main()

#
