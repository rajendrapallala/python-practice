from datetime import time
from datetime import date
if __name__ == "__main__":
    t = time(6,30,0,0)
    print(t)
    t.microsecond
    print(time.min)
    print(time.max)
    print(time.resolution)

    today=date.today()
    print(today)
    print(today.day)

    d1= date(2005, 1, 30)
    print(d1)

    d2= d1.replace(year=2019)
    print(d2)
