import datetime
import math


def _get_daydetla(date1str: str, date2str: str):
    """두 날짜의 차이(일)를 반환합니다.

    Args:
        date1str: 날짜를 나타내는 문자열 (년월일 순  eg. "1999-06-08")
        date2str: 날짜를 나타내는 문자열 (년월일 순  eg. "2000-12-31")

    Returns:
        int: 두 날짜의 차이(일)
    """
    dt1obj = datetime.datetime.strptime(date1str, "%Y-%m-%d")
    dt2obj = datetime.datetime.strptime(date2str, "%Y-%m-%d")
    td: datetime.timedelta = dt2obj - dt1obj
    return td.days


def get_biorhythms(birthday: str, targetday: str):
    day_elapsed = _get_daydetla(birthday, targetday)

    def biovalue(circle, elaspeddays):
        return math.sin(2 * math.pi * elaspeddays / circle)

    physical = biovalue(23, day_elapsed)
    emotional = biovalue(28, day_elapsed)
    mental = biovalue(33, day_elapsed)

    return day_elapsed, physical, emotional, mental


if __name__ == '__main__':
    birthday = "1943-03-09"
    targetday = "1972-07-11"
    rst = get_biorhythms(birthday, targetday)
    print(rst)
