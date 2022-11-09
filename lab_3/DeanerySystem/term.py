from day import *

class Term:
    def __init__(self, day, hour, minute, time=90):
      self.day = day
      self.hour = hour
      self.minute = minute
      self.duration = time

    def __str__(self) -> str:
       return f"{self.date(self.day.value - 1)}, {self.hour}:{self.minute} [{self.duration}]"

    def __lt__(self, termin):
        return self.earlierThan(termin)

    def __le__(self, termin):
        return self.earlierThan(termin) or self.equals(termin)

    def __gt__(self, termin):
        return self.laterThan(termin)

    def __ge__(self, termin):
        return self.laterThan(termin) or self.equals(termin)

    def __eq__(self, termin):
        if self.duration == termin.duration:
            return self.equals(termin)
        return False

    def __sub__(self, termin):
        differece = (self.day.value - termin.day.value) * 24 * 60
        differece += (self.hour - termin.hour) * 60
        differece += (self.minute - termin.minute) 
        differece += self.duration
        return Term(termin.day, termin.hour, termin.minute, differece)

    @staticmethod
    def date(day):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[day]

    def earlierThan(self, termin):
        if self.day.value < termin.day.value:
            if self.hour < termin.hour:
                return True
            else:
                if self.minute < termin.minute:
                    return True
        return False
    
    def laterThan(self, termin):
        if self.day.value > termin.day.value:
            if self.hour > termin.hour:
                return True
            else:
                if self.minute > termin.minute:
                    return True
        return False

    def equals(self, termin):
        if self.day != termin.day:
            return False
        if self.hour != termin.hour:
            return False
        if self.minute != termin.minute:
            return False
        return True


class Lesson(Term):
    def __init__(self, term, name, teacherName, year, fullTime=True):
        self.term = term
        self.name = name
        self.teacherName = teacherName
        self.year = year
        self.fullTime = fullTime

    def __str__(self):
        return f"{self.name} ({self.term.day} {self.term.hour}:{self.term.minute}-{(self.term.hour + (self.term.duration // 60) + ((self.term.minute + (self.term.duration % 60)) // 60))}:{(self.term.minute + self.term.duration) % 60})\n{self.year} rok studiów {self.fullTime}\nProwadzący: {self.teacherName}"

    def earlierDay(self) -> bool:
        if self.fullTime:
            if self.term.day.value - 1 in [6, 7]:
                return False
            elif self.term.day.value - 1 == 5:
                ending = self.term.hour * 60 + self.term.minute + self.term.duration
                if ending // 60 < 17 and ending // 60 >= 8 or ending == 17 * 60:
                    self.term.day = self.term.day.change(1)
                    return True
            self.term.day = self.term.day.change(1)
            return True

        elif not self.fullTime:
            if self.term.day.value - 1 in [1, 2, 3, 4]:
                return False
            elif self.term.day.value - 1 == 5:
                ending = self.term.hour * 60 + self.term.minute + self.term.duration
                if ending // 60 >= 17 and ending // 60 < 20 or ending == 20 * 60:
                    self.term.day = self.term.day.change(-1)
                    return True
            self.term.day = self.term.day.change(-1)
            return True
        return False

    def laterDay(self) -> bool:
        if self.fullTime:
            if self.term.day.value + 1 in [6, 7]:
                return False
            elif self.term.day.value + 1 == 5:
                ending = self.term.hour * 60 + self.term.minute + self.term.duration
                if ending // 60 < 17 and ending // 60 >= 8 or ending == 17 * 60:
                    self.term.day = self.term.day.change(1)
                    return True
            self.term.day = self.term.day.change(1)
            return True

        elif not self.fullTime:
            if self.term.day.value + 1 in [1, 2, 3, 4]:
                return False
            elif self.term.day.value + 1 == 5:
                ending = self.term.hour * 60 + self.term.minute + self.term.duration
                if ending // 60 >= 17 and ending // 60 < 20 or ending == 20 * 60:
                    self.term.day = self.term.day.change(1)
                    return True
            self.term.day = self.term.day.change(1)
            return True
        return False

    def earlierTime(self) -> bool:
        pass

    def laterTime(self) -> bool:
        pass
