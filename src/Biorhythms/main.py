import datetime
import math


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


def main():
    # inputstr = input("input birthday and targetday (eg. 1991-01-01 1999-12-31): ")
    # birthday, targetday = inputstr.split()
    birthday = "1943-03-09"
    targetday = "1972-07-11"
    birthday_dt = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    targetday_dt = datetime.datetime.strptime(targetday, "%Y-%m-%d")

    ### CL
    rst = calc_biorhythms(birthday_dt, targetday_dt)

    print(f"Day elapsed: {rst[0]}")
    phy, emo, men = (f"{v:.1%}" for v in rst[1])
    print(f"Physical: {phy}, Emotional: {emo}, Mental: {men} as of {targetday}")

    ### plot
    view_range = 30
    # elasped from birthday
    start_point = rst[0] - view_range // 2
    end_point = rst[0] + view_range // 2 + 1
    x_value = range(start_point, end_point)
    x_label = [(birthday_dt + datetime.timedelta(days=v)).strftime("%Y-%m-%d") for v in x_value]
    print(x_label)

    # x_value = range(rst[0] - view_range // 2, rst[0] + view_range // 2 + 1)  # elapsed days
    # x_label = [(birthday_dt + datetime.timedelta(days=v)).strftime("%Y-%m-%d") for v in x_value]
    # x_value = []
    # x_label = []

    # for x in range(- view_range // 2, view_range // 2 + 1):
    #     x_day = birthday_dt + datetime.timedelta(days=rst[0] + x)

    # for eday in x_value:
    #     cur_day = birthday_dt + datetime.timedelta(days = eday)
    #     print(cur_day)

    # elapsed_td = targetday_dt - birthday_dt
    # x_series = []
    # y_series = []
    # for day in range(-20, 21):
    #     cur_day = birthday_dt + datetime.timedelta(days=day)
    #     # x_series.append(cur_day.strftime("%Y-%m-%d"))
    #     x_series.append(cur_day)
    #     y_series.append(1.2)
    #
    # plt.title("Biorhythms")
    # plt.xlabel('Date')
    # plt.ylabel('Value')
    # plt.plot(x_series, y_series)
    # plt.grid(True)
    # plt.xticks(rotation=45)
    #
    # plt.show()


if __name__ == '__main__':
    # birthday = "1943-03-09"
    # targetday = "1972-07-11"
    # rst = calc_biorhythms(birthday, targetday)
    # print(rst)
    main()
