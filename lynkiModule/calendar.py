"""
MON TUE WED THU FRI SAT SUN
1   2   3   4   5   6   0
"""

def isLeepYear(year: int):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False

def getYearList(year: int):
    february: int = 28 + (1 if isLeepYear(year) else 0)
    return [31, february, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def getYearStart(year: int):
    initYear = {
        "year": 0,
        "yearStartDay": 6
    }

    day = initYear["yearStartDay"]

    for i in range(year - initYear["year"]):
        day += 2 if isLeepYear(initYear["year"] + i) else 1

    return day % 7

def getMonthStart(year: int, month: int):
    day = sum(getYearList(year)[:month - 1]) + getYearStart(year)
    return day % 7

def getDay(year: int, month: int, date: int):
    return (getMonthStart(year, month) + date - 1) % 7
        
def draw(year: int, month: int):
    startDay = getMonthStart(year, month)
    max = getYearList(year)[month - 1]
    
    print("\t" * 3 + "\b" + f"{year}.{month}")
    print("MON.\tTUE.\tWED.\tTHU.\tFRI.\tSAT.\tSUN.")
    print("\t" * ((7 if startDay == 0 else startDay) - 1), end="")

    for i in range(max):
        print(f" {i+1}\t", end="")
        if (startDay + i) % 7 == 0:
            print("")

if __name__ == "__main__":
    draw(2007, 7)