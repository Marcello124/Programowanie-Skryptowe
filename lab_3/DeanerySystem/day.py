from enum import Enum


class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

    def change(self, n):
        for day in Day:
            shift = ((day.value) + n) % 7
            if shift == 0:
                shift = 7
            if day.value == shift:
                return day
        

    def difference(self, day):
        difference = day.value - self.value

        if difference < 4 and difference > -4:
            return difference

        elif difference >= 4:
             return difference - 7
        
        else:
            return difference + 7

def nthDayFrom(n, day):
    shift = ((day.value) + n) % 7
    if shift == 0:
        shift = 7
    for i in Day:

        if i.value == shift:
            return i
