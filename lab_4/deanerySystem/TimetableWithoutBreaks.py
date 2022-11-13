from __future__ import annotations
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from term import Term, Lesson, Action


class TimetableWithoutBreaks:
    """ Class containing a set of operations to manage the timetable """
    def __init__(self):
        self.lessons = []

    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:
        """
Informs whether a lesson can be transferred to the given term

Parameters
----------
term : Term
    The term checked for the transferability
fullTime : bool
    Full-time or part-time studies

Returns
-------
bool
    **True** if the lesson can be transferred to this term
"""

        if fullTime:
            if term.day.value in [6, 7]:
                return False
            elif term.day.value == 5:
                if term._beginning >= 8 * 60 and term._ending <= 17 * 60:
                    return True
            elif term.day.value in [1, 2, 3, 4]:
                if term._ending <= 20 * 60 and term._beginning >= 8 * 60:
                    return True
        else:
            if term.day.value in [1, 2, 3, 4]:
                return False
            elif term.day.value == 5:
                if term._beginning >= 17 * 60 and term._ending <= 20 * 60:
                    return True
            elif term.day.value in [6, 7]:
                if term._ending <= 20 * 60 and term._beginning >= 8 * 60:
                    return True

    def busy(self, term: Term) -> bool:
        """
Informs whether the given term is busy.  Should not be confused with ``can_be_transfered_to()``
since there might be free term where the lesson cannot be transferred.

Parameters
----------
term : Term
    Checked term

Returns
-------
bool
    **True** if the term is busy
        """
        if not term in self.lessons:
            return False
        return True
        

    def put(self, lesson: Lesson) -> bool:
        """
Add the given lesson to the timetable.

Parameters
----------
lesson : Lesson
    The added  lesson

Returns
-------
bool
    **True**  if the lesson was added.  The lesson cannot be placed if the timetable slot is already occupied.
        """
        if self.busy(lesson.term):
            return False
        self.lessons.append(lesson)

    def parse(self, actions: List[str]) -> List[Action]:
        """
Converts an array of strings to an array of 'Action' objects.

Parameters
----------
actions:  List[str]
    A list containing the strings: "d-", "d+", "t-" or "t+"

Returns
-------
    List[Action]
        A list containing the values:  DAY_EARLIER, DAY_LATER, TIME_EARLIER or TIME_LATER
        """

        pass

    def perform(self, actions: List[Action]):
        """
Transfer the lessons included in the timetable as described in the list of actions. N-th action should be sent the n-th lesson in the timetable.

Parameters
----------
actions : List[Action]
    Actions to be performed
        """

        pass

    def get(self, term: Term) -> Lesson:
        """
Get object (lesson) indicated by the given term.

Parameters
----------
term: Term
    Lesson date

Returns
-------
lesson: Lesson
    The lesson object or None if the term is free
        """

        pass