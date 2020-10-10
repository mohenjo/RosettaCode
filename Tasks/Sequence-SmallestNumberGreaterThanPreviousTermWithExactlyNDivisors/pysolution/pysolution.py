def main():
    rst = generate_series()
    for _ in range(15):
        print(next(rst))

def generate_series():
    cur_idx = 1
    cur_val = 1
    while True:
        if get_num_divisors(cur_val) == cur_idx:
            cur_idx += 1
            yield cur_val
        cur_val +=1

def get_num_divisors(anum:int):
    divisors = set()
    for n in range(1, int(anum ** 0.5) + 1):
        if anum % n == 0:
            divisors.add(n)
            divisors.add(anum // n)
    return len(divisors)

if __name__ == "__main__":
    main()
