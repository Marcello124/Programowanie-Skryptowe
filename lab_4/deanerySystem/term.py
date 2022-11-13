from day import Day
from enum import Enum
from TimetableWithoutBreaks import TimetableWithoutBreaks


class Action(Enum):
    DAY_EARLIER = 0
    DAY_LATER = 1
    TIME_EARLIER = 2
    TIME_LATER = 3


class Term:
    def __init__(self, day: Day, hour: int, minute: int, time: int =90):
        '''Dane o terminie zajęć'''
        self.__day = None
        self.__hour = None
        self.__minute = None
        self.__duration = None
        self.__time = None
        self.__beginning = None
        self.__ending = None

    @property
    def day(self):
        return self.__day
    
    @day.setter
    def day(self, day):
        self.__day = day

    @property
    def hour(self):
        return self.__hour
    
    @hour.setter
    def hour(self, hour):
        self.__hour = hour

    @property
    def minute(self):
        return self.__minute
    
    @minute.setter
    def minute(self, minute):
        self.__minute = minute

    @property
    def duration(self):
        return self.__duration
    
    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    @property
    def _time(self):
        return self.__time
    
    @_time.setter
    def _time(self, day, hour, minute):
        self.__time = (day.value - 1) * 24 * 60 + hour * 60 + minute

    @property
    def _beginning(self):
        return self.__beginning
    
    @_beginning.setter
    def _beginning(self, _time):
        self.__beginning = _time % (24 * 60)

    @property
    def _ending(self):
        return self.__ending

    @_ending.setter
    def _ending(self, _time):
        self.__ending = self.term._time % (24 * 60) + self.term.duration
    
    def __str__(self) -> str:
        return f"{self.date(self.day.value - 1)}, {self.hour}:{self.minute} [{self.duration}]"

    def validate(self):
        if self.fullTime:
            if self.term.day.value in [6, 7]:
                print("Wrong term! Change it")
            elif self.term.day.value == 5:
                if self._beginning < 8 * 60 or self._ending > 17 * 60:
                    print("Wrong term! Change it")

        elif not self.fullTime:
            if self.term.day.value in [1, 2, 3, 4]:
                print("Wrong term! Change it")
            elif self.term.day.value == 5:
                if self._beginning < 17 * 60 or self._ending > 20 * 60:
                    print("Wrong term! Change it")

    def change(self, duration, time=True, beginning=True, ending=True):
        if time:
            self._time += duration
        if beginning:
            self._beginning += duration
        if ending:
            self._ending += duration

    def __lt__(self, termin):
        return self.earlierThan(termin)

    def __le__(self, termin):
        return self.earlierThan(termin) or self.equals(termin)

    def __gt__(self, termin):
        return self.laterThan(termin)

    def __ge__(self, termin):
        return self.laterThan(termin) or self.equals(termin)

    def __eq__(self, termin ):
        if self.duration == termin.duration:
            return self.equals(termin)
        return False

    def __sub__(self, termin):
        differece = self._time - termin._time
        return Term(termin.day, termin.hour, termin.minute, differece)

    @staticmethod
    def date(day):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[day]

    def earlierThan(self, termin):
        if self.day._time < termin._time:
            return True
        return False
    
    def laterThan(self, termin):
        if self.day._time > termin._time:
            return True
        return False

    def equals(self, termin):
        if self._time == termin._time:
            return True
        return False


class Lesson(Term):
    def __init__(self, timetable: TimetableWithoutBreaks, term: Term, name: str, teacherName: str, year: str, fullTime: bool = True):
        self.__timetable = None
        self.__term = None
        self.__name = None
        self.__teacherName = None
        self.__year = None
        self.__fullTime = None

    @property
    def timetable(self):
        return self.__timetable

    @timetable.setter
    def timetable(self, timetable):
        self.__timetable = timetable

    @property
    def term(self):
        return self.__term
    
    @term.setter
    def term(self, term):
        self.__term = term

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def teacherName(self):
        return self.__teacherName
    
    @teacherName.setter
    def teacherName(self, teacherName):
        self.__teacherName = teacherName

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def fullTime(self):
        return self.__fullTime
    
    @fullTime.setter
    def fullTime(self, fullTime):
        self.__fullTime = fullTime

    def __str__(self):
        return f"{self.name} ({self.term.day} {self.term.hour}:{self.term.minute}-{(self.term._time + self.term.duration) % (24 * 60) // 60}:{(self.term._time + self.term.duration) % 60})\n{self.year} rok studiów {self.fullTime}\nProwadzący: {self.teacherName}"

    def earlierDay(self) -> bool:
        if not self.timetable.can_be_transferred_to(Term(self.term.day.change(-1), self.term.hour, self.term.minute), self.term.fullTime):
            return False
        if self.timetable.busy(self.term):
            return False
        self.term.day = self.term.day.change(-1)
        self.term.change(-24*60)
        return True

    def laterDay(self) -> bool:
        if self.timetable.can_be_transferred_to(Term(self.term.day.change(1), self.term.hour, self.term.minute), self.term.fullTime):
            return False
        if self.timetable.busy(self.term):
            return False
        self.term.day = self.term.day.change(1)
        self.term.change(24*60)
        return True

    def earlierTime(self) -> bool:
        if self.timetable.can_be_transferred_to(Term(self.term.day, self.term.hour - self.term.duration // 60, self.term.minute - self.term.duration % 60), self.term.fullTime):
            return False
        if self.timetable.busy(self.term):
            return False
        self.term.hour -= self.term.duration // 60
        self.term.minute -= self.term.duration % 60
        self.term.change(-self.term.duration)
        return True

    def laterTime(self) -> bool:
        if self.timetable.can_be_transferred_to(Term(self.term.day, self.term.hour + self.term.duration // 60, self.term.minute + self.term.duration % 60), self.term.fullTime):
            return False
        if self.timetable.busy(self.term):
            return False
        self.term.hour += self.term.duration // 60
        self.term.minute += self.term.duration % 60
        self.term.change(self.term.duration)
        return True
