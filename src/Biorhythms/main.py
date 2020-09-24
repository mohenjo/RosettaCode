import datetime
import math
import matplotlib.pyplot as plt


def calc_biorhythms(birthday: datetime.datetime, targetday: datetime.datetime):
    """바이오리듬을 구합니다.

    Args:
        birthday: 시작 날짜를 나타내는 datetime 객체
        targetday: 바이오리듬 확인 날짜를 나타내는 datetime 객체

    Returns:
        경과 일 수, 바이오리듬(신체, 감성, 정신)으로 구성된 튜플
    """
    day_elapsed = (targetday - birthday).days

    def biovalue(circle, elaspeddays):
        return math.sin(2 * math.pi * elaspeddays / circle)

    physical = biovalue(23, day_elapsed)
    emotional = biovalue(28, day_elapsed)
    mental = biovalue(33, day_elapsed)

    return day_elapsed, (physical, emotional, mental)


def get_biorhythms(birthday: str, targetday: str):
    birthday_dt = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    targetday_dt = datetime.datetime.strptime(targetday, "%Y-%m-%d")


def main():
    birthday_dt = datetime.datetime.strptime("1943-03-09", "%Y-%m-%d")
    targetday_dt = datetime.datetime.strptime("1972-07-11", "%Y-%m-%d")
    elapsed_td = targetday_dt - birthday_dt
    x_series = []
    y_series = []
    for day in range(-20, 21):
        cur_day = birthday_dt + datetime.timedelta(days=day)
        # x_series.append(cur_day.strftime("%Y-%m-%d"))
        x_series.append(cur_day)
        y_series.append(1.2)

    plt.title("Biorhythms")
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.plot(x_series, y_series)
    plt.grid(True)
    plt.xticks(rotation=45)

    plt.show()


if __name__ == '__main__':
    # birthday = "1943-03-09"
    # targetday = "1972-07-11"
    # rst = calc_biorhythms(birthday, targetday)
    # print(rst)
    main()
