def main():
    gen = look_and_say(1)
    for _ in range(15):
        print(next(gen))


def look_and_say(startnum: int):
    lastnum = startnum
    while True:
        yield lastnum
        lastnum = _look_and_say(lastnum)


def _look_and_say(anum: int):
    # group elements in number
    anum_str = str(anum)
    foo: str = ""
    for idx in range(len(anum_str) - 1):
        foo += anum_str[idx]
        if anum_str[idx] != anum_str[idx + 1]:
            foo += ":"
    foo += anum_str[-1]
    # say
    bar = [str(len(e)) + e[0] for e in foo.split(":")]
    return int("".join(bar))


if __name__ == '__main__':
    main()
