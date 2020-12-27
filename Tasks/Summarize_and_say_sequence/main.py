def main():
    uptoval = 1_000_000
    len_lst = [0 for _ in range(0, uptoval + 1)]
    print("calculating...", end='')
    for testnum in range(0, uptoval + 1):
        foo = SummarizeAndSaySeq(testnum)
        len_lst[testnum] = foo.sequence_length
    maxlength = max(len_lst)
    print("ok.\n")
    for i, v in enumerate(len_lst):
        if v == maxlength:
            foo = SummarizeAndSaySeq(i)
            print(f"seed value with max sequence length {foo.sequence_length}: {i}")
            print("sequence:")
            for e in foo.sequence:
                print(e)
            print()


class SummarizeAndSaySeq:
    def __init__(self, seedvalue: int):
        self._seedvalue = seedvalue
        self._sequence = []
        self._seqlen = 0
        self._generate_seq()

    @property
    def sequence_length(self):
        return self._seqlen

    @property
    def sequence(self):
        return self._sequence

    def _generate_seq(self):
        # return summarize and say seq
        last_num = self._seedvalue
        self._sequence.append(last_num)
        next_num = summarize_and_say(last_num)
        while next_num not in self._sequence:
            self._sequence.append(next_num)
            last_num = next_num
            next_num = summarize_and_say(last_num)
        self._seqlen = len(self._sequence)


def summarize_and_say(anum: int) -> int:
    # count elements in decsending order
    anum_str = str(anum)
    foo: str = ""
    for num in range(10):
        cnt = anum_str.count(str(num))
        if cnt != 0:
            foo = f"{cnt}{num}" + foo
    return int(foo)


if __name__ == '__main__':
    main()
