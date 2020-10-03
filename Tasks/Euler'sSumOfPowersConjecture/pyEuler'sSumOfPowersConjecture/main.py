def main():
    rst = bf_cal()
    print(f"{rst[0]}^5 + {rst[1]}^5 + {rst[2]}^5 + {rst[3]}^5 = {rst[4]}^5")

def bf_cal():
    max_n = 250
    pwr_pool = [n ** 5 for n in range(max_n)]
    y_pwr_pool = {n ** 5 : n for n in range(max_n)}
    for x0 in range(1, max_n):
        print(f"processing {x0} in (0..250)")
        for x1 in range(x0, max_n):
            for x2 in range(x1, max_n):
                for x3 in range(x2, max_n):
                    y_pwr5 = sum(pwr_pool[i] for i in (x0, x1, x2, x3))
                    if y_pwr5 in y_pwr_pool:
                        y = y_pwr_pool[y_pwr5]
                        if y not in (x0, x1, x2, x3):
                            return x0, x1, x2, x3, y
                       
if __name__ == "__main__":
    main()
    # 27^5 + 84^5 + 110^5 + 133^5 = 144^5