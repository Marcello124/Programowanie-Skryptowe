class Term:
    def __init__(self, day, hour, minute):
      self._day = day
      self.hour = hour
      self.minute = minute
      self.duration = 90

    def __str__(self) -> str:
       return f"{self.date(self._day.value - 1)}, {self.hour}:{self.minute} [{self.duration}]"

    @staticmethod
    def date(day):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[day]

    def earlierThan(self, termin):
        if self._day.value < termin._day.value:
            if self.hour < termin.hour:
                return True
            else:
                if self.minute < termin.minute:
                    return True
        return False
    
    def laterThan(self, termin):
        if self._day.value > termin._day.value:
            if self.hour > termin.hour:
                return True
            else:
                if self.minute > termin.minute:
                    return True
        return False

    def equals(self, termin):
        if self._day == termin._day and self.hour == termin.hour and self.minute == termin.minute:
            return True
        return False