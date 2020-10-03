def main():
    rst = bf_cal()
    print(rst)

def bf_cal():
    max_n = 250
    pwr_pool = [n ** 5 for n in range(max_n)]
    for x0 in range(1, max_n):
        print(f"processing {x0} in (0..250)")
        for x1 in range(1,x0):
            for x2 in range(1,x1):
                for x3 in range(1 ,x2):
                    y_pwr5 = sum(pwr_pool[i] for i in (x0, x1, x2, x3))
                    y = y_pwr5 ** (1/5)
                    if y_pwr5 in pwr_pool and y == int(y) and y not in (x0, x1, x2, x3):
                        return x0, x1, x2, x3, y
                       

def is_exclusive(*args):
    """인수가 모두 다르며, [0, 250] 범위의 값을 갖는지 확인합니다."""
    if len(set(args)) == len(args) and all(map(lambda x: 0 < x < 250, args)):
        return True
    return False

if __name__ == "__main__":
    main()