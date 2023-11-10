from dataclasses import dataclass
from enum import Enum


@dataclass
class Contact:
    mobile: str = None
    office: str = None
    email: str = None
    web: str = None
    telegram: str = None
    
    # декоратор автоматически создаёт конструктор по типу:
    # def __init__(
    #         self, 
    #         mobile: str
    #         office: str
    #         email: str
    #         web: str
    #         telegram: str
    # ):
    #     self.mobile = mobile
    #     self.office = office
    #     self.email = email
    #     self.web = web
    #     self.telegram = telegram:


# >>> Contact(mobile='+79991234567')
# Contact(mobile='+79991234567', office=None, email=None, web=None, telegram=None)


class Degree(Enum):
    CANDIDATE = 'кандидат'
    DOCTOR = 'доктор'


# >>> doctor = Degree('доктор')
# >>> doctor.__class__
# <enum 'Degree'>
# >>>
# >>> doctor2 = Degree('доктор')
# >>>
# >>> doctor is doctor2
# True
# >>>
# >>> doctor is Degree('кандидат')
# False
# >>>
# >>> Degree('кандидат') is Degree('кандидат')
# True
# >>>
# >>> Degree.DOCTOR
# <Degree.DOCTOR: 'доктор'>
# >>>
# >>> doctor is Degree.DOCTOR is doctor2
# True

# >>> list(Degree)
# [<Degree.CANDIDATE: 'кандидат'>, <Degree.DOCTOR: 'доктор'>]
# >>>
# >>> for obj in Degree:
# ...     print(obj)
# ...
# Degree.CANDIDATE
# Degree.DOCTOR
