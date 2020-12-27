def main():
    maxlength = 0
    maxlength_seq = None
    maxseed = None
    for testnum in range(0, 1_000_000 + 1):
        foo = SummarizeAndSaySeq(testnum)
        if foo.sequence_length > maxlength:
            maxseed = testnum
            maxlength = foo.sequence_length
            maxlength_seq = foo.sequence
            print(f"{maxseed} has length {maxlength}.")
    print()
    print(f"{maxseed} has the longest sequence length {maxlength}:")
    for e in maxlength_seq:
        print(e)


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
