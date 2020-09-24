import datetime
import math
import matplotlib.pyplot as plt


def get_biorhythms(days_elapsed: int):
    """바이오리듬을 반환합니다.

    Args:
        days_elapsed: 출생일로부터의 경과일

    Returns:
        바이오리듬(신체, 감성, 정신)의 튜플
    """

    def biovalue(circle, elaspeddays):
        """바이오리듬 값(%)"""
        return math.sin(2 * math.pi * elaspeddays / circle) * 100

    physical = biovalue(23, days_elapsed)
    emotional = biovalue(28, days_elapsed)
    mental = biovalue(33, days_elapsed)

    return physical, emotional, mental


def main():
    date_format = "%Y-%m-%d"
    inputstr = input("input birthday and check day (eg. 1991-01-01 1999-12-31): ")
    birthday, checkday = inputstr.split()
    # birthday = "1943-03-09"  # Rosetta Code Ex
    # checkday = "1972-07-11"  # Rosetta Code Ex
    birthday_obj = datetime.datetime.strptime(birthday, date_format)
    checkday_obj = datetime.datetime.strptime(checkday, date_format)
    days_elapsed = (checkday_obj - birthday_obj).days

    ### CL
    rst = get_biorhythms(days_elapsed)
    print(f"Days elapsed: {days_elapsed:,}")
    phy, emo, men = (round(v) for v in rst)
    print(f"Physical: {phy}%, Emotional: {emo}%, Mental: {men}% as of {checkday}")

    ### PLOT
    view_range = 30  # days
    x_value = [days_elapsed + v for v in range(- view_range // 2, view_range // 2 + 1)]
    x_label = [(birthday_obj + datetime.timedelta(days=v)).strftime(date_format) for v in x_value]
    bio_value = [get_biorhythms(v) for v in x_value]
    phys = [bv[0] for bv in bio_value]
    emos = [bv[1] for bv in bio_value]
    mens = [bv[2] for bv in bio_value]

    plt.plot(x_label, phys, label="PHYSICAL")
    plt.plot(x_label, emos, label="EMOTIONAL")
    plt.plot(x_label, mens, label="MENTAL")

    plt.axvline(checkday, -100, 100, color="r", linewidth=1, linestyle="--")

    plt.title("Biorhythms")
    plt.xlabel('Date')
    plt.ylabel('Status(%)')
    plt.xlim(x_label[0], x_label[-1])
    plt.ylim(-100, 100)
    plt.grid(True)
    plt.xticks(x_label, rotation=90)
    plt.tight_layout()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
