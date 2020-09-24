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


def get_biorhythms(birthday: str, targetday: str):
    birthday_dt = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    targetday_dt = datetime.datetime.strptime(targetday, "%Y-%m-%d")


if __name__ == '__main__':
    birthday = "1943-03-09"
    targetday = "1972-07-11"
    rst = calc_biorhythms(birthday, targetday)
    print(rst)
