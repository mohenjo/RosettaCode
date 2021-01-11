def is_divisible(anumber: int) -> bool:
    return anumber % sum(map(int, (s for s in str(anumber)))) == 0


class HarshadSeries:
    def __init__(self, startnum=1):
        self.start_num = 1
        if startnum > 1:
            self.start_num = startnum
        self.curnum = self.start_num - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.curnum += 1
        while not is_divisible(self.curnum):
            self.curnum += 1
        return self.curnum


def main():
    foo = HarshadSeries()
    rst = [next(foo) for _ in range(20)]
    print(rst)

    foo = HarshadSeries(1001)
    print(next(foo))


if __name__ == '__main__':
    main()
