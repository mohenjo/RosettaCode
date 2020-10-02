def main():
    rst = bf_cal()
    print(rst)

def bf_cal():
    for x0 in range(1, 251):
        print(f"0..{x0}..251")
        for x1 in range(x0,251):
            for x2 in range(x1,251):
                for x3 in range(x2,251):
                    y = (x0 ** 5 + x1 ** 5 + x2 ** 5 + x3 ** 5) ** (1 / 5)
                    if y == int(y) and y > x3 and is_exclusive(x0, x1, x2, x3, y):
                       return x0, x1, x2, x3, y
                       

def is_exclusive(*args):
    """인수가 모두 다르며, [0, 250] 범위의 값을 갖는지 확인합니다."""
    if len(set(args)) == len(args) and all(map(lambda x: 0 < x < 250, args)):
        return True
    return False

if __name__ == "__main__":
    main()