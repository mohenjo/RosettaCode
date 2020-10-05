def main():
    flt_num = 23.34375
    bin_num = 1011.11101
    print(f"실수 {flt_num} => 이진수 {float2bin(flt_num)}")
    print(f"이진수 {bin_num} => 실수 {bin2float(bin_num)}")


def float2bin(afloat: float):
    """소수점 이하의 값이 있는 실수를 이진수로 변환

    Args:
        afloat: 이진수로 변환할 실수

    Returns:
        이진수 ('0b' prefix가 없는 실수의 형태)
    """
    integer_part = int(afloat)  # 정수부분
    decimal_part = afloat - integer_part  # 소수부분
    decimal_bin = "."  # 소수부문에 대한 이진표현
    while decimal_part != 0.0:
        foo = decimal_part * 2
        bar = int(foo)
        decimal_bin += str(bar)
        decimal_part = foo - bar
    return float(bin(integer_part)[2:] + decimal_bin)


def bin2float(abin: float):
    """소수점 이하의 값이 있는 이진수를 실수로 변환

    Args:
        abin: 실수로 변환할 이진수 ('0b' prefix가 없는 실수의 형태)

    Returns:
        실수
    """
    abin_str = str(abin)
    loc = abin_str.find(".")
    float_value = 0
    for i, v in enumerate(abin_str[:loc]):
        float_value += int(v) * 2 ** (loc - i - 1)
    for i, v in enumerate(abin_str[loc + 1:]):
        float_value += int(v) * 2 ** (-(i + 1))
    return float_value


if __name__ == '__main__':
    main()
