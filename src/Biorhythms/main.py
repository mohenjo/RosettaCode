import datetime


def get_daydetla(date1str: str, date2str: str):
    """두 날짜의 차이(일)를 반환합니다.

    Args:
        date1str: 날짜를 나타내는 문자열 (년월일 순  eg. "19990608")
        date2str: 날짜를 나타내는 문자열 (년월일 순  eg. "20001231")

    Returns:
        int: 두 날짜의 차이(일)
    """
    dt1obj = datetime.datetime.strptime(date1str, "%Y%m%d")
    dt2obj = datetime.datetime.strptime(date2str, "%Y%m%d")
    td: datetime.timedelta = dt2obj - dt1obj
    return td.days


def main():
    pass


if __name__ == '__main__':
    date1 = "20200101"
    date2 = "20200110"
    get_daydetla(date1, date2)
