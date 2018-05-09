import enum


class CurrencyEnum(enum.Enum):
    USD = 1
    UAH = 2
    EUR = 3


class DayEnum(enum.Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7


class LanguageEnum(enum.Enum):
    RUS = 'rus'
    ENG = 'eng'


class ComfortEnum(enum.Enum):
    #Tourism
    Socket = 1
    WelcomeTourists = 2
    #Visitors
    ForChildren = 3
    AnimalAccess = 4
    #Service
    RentBikes = 5
    Polygraph = 6
    #Section of inclusiveness
    Ramp = 7
    SpecialToilet = 8
    SpecialService = 9


class PaymentMethodEnum(enum.Enum):
    DebitCard = 1
    CreditCard = 2
    ElectronicPayment = 3
