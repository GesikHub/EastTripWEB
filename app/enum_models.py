from enum import Enum


class RoleEnum(Enum):
    USER = 1
    ADMIN = 2


class CategoryEnum(Enum):
    CAFE = 'Cafe'
    COFFEESHOP = 'CoffeeShop'
    RESTAURANT = 'Restaurant'
    HOTEL = 'Hotel'
    HOSTEL = 'Hostel'
    CLUB = 'Club'
    PUB = 'Pub'
