from decimal import Decimal


def main():
    max_n = 18

    # is_almost_integer = lambda num: True if f"{num:0.5f}"[-5] in ("9", "0") else False
    def is_almost_integer(anum):
        return True if f"{anum:0.5f}"[-5] in ("9", "0") else False

    rst = get_hickerson_series(max_n)
    for n in range(1, max_n + 1):
        expr = f"h({n}) = {rst[n]:0.3f} : is almost integer? {is_almost_integer(rst[n])}"
        print(expr)


def get_hickerson_series(max_n: int):
    factorials = [1]
    series = [None]
    for n in range(1, max_n + 1):
        factorials.append(factorials[-1] * n)
        eq = factorials[n] / (2 * Decimal(2).ln() ** (n + 1))
        series.append(eq)
    return series


if __name__ == "__main__":
    main()
