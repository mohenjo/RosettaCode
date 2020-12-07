# region easy approach for basic task
def main():
    numberset = [n for n in range(1, 11)]
    print(numberset)
    for n in numberset:
        rst = find_minmul(n)
        print(f"{n}  {rst[0]}  {n} x {rst[1]}")


def find_minmul(num: int):
    """B10이 0과 1로만 이루어진 경우 B10, 및 곱수 반환"""
    mulnum = 1
    while not isok(num * mulnum):
        mulnum += 1
    b10 = num * mulnum
    return b10, mulnum


def isok(num: int):
    """주어진 인수가 0과 1로만 이루어져 있을 경우 참 반환"""
    cnv = set(int(n) for n in str(num))
    return all(e in {0, 1} for e in cnv)


# endregion


# region altenative approach for stretch goal
def main_alt():
    # basic task
    numberset = [n for n in range(1, 11)]
    numberset.extend(range(95, 106))
    numberset.extend((297, 576, 594, 891, 909, 999))
    # optional task
    numberset.extend((1998, 2079, 2251, 2277))
    # stretch goal
    numberset.extend((2439, 2997, 4878))

    def bin2b10(anum: int):
        return int(bin(anum)[2:])

    for num in numberset:
        checkval = 1
        while bin2b10(checkval) % num:
            checkval += 1
        rst = bin2b10(checkval)
        print(f"{num}: {rst} = {num} x {rst // num}")


# endregion

if __name__ == '__main__':
    main()
    main_alt()

'''
1: 1 = 1 x 1
2: 10 = 2 x 5
3: 111 = 3 x 37
4: 100 = 4 x 25
5: 10 = 5 x 2
6: 1110 = 6 x 185
7: 1001 = 7 x 143
8: 1000 = 8 x 125
9: 111111111 = 9 x 12345679
10: 10 = 10 x 1
95: 110010 = 95 x 1158
96: 11100000 = 96 x 115625
97: 11100001 = 97 x 114433
98: 11000010 = 98 x 112245
99: 111111111111111111 = 99 x 1122334455667789
100: 100 = 100 x 1
101: 101 = 101 x 1
102: 1000110 = 102 x 9805
103: 11100001 = 103 x 107767
104: 1001000 = 104 x 9625
105: 101010 = 105 x 962
297: 1111011111111111111 = 297 x 3740778151889263
576: 111111111000000 = 576 x 192901234375
594: 11110111111111111110 = 594 x 18703890759446315
891: 1111111111111111011 = 891 x 1247038284075321
909: 1011111111111111111 = 909 x 1112333455567779
999: 111111111111111111111111111 = 999 x 111222333444555666777889
1998: 1111111111111111111111111110 = 1998 x 556111667222778333889445
2079: 1001101101111111111111 = 2079 x 481530111164555609
2251: 101101101111 = 2251 x 44913861
2277: 11110111111111111011 = 2277 x 4879275850290343
2439: 10000101011110111101111111 = 2439 x 4100082415379299344449
2997: 1111110111111111111111111111 = 2997 x 370740777814851888925963
4878: 100001010111101111011111110 = 4878 x 20500412076896496722245
'''
