#Exercice 1 
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        return self.amount + other

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        else:
            self.amount += other
        return self

# Example usage
if __name__ == "__main__":
    c1 = Currency('dollar', 5)
    c2 = Currency('dollar', 10)
    c3 = Currency('shekel', 1)
    c4 = Currency('shekel', 10)

    print(str(c1))  
    print(int(c1)) 
    print(repr(c1))  

    print(c1 + 5)  
    print(c1 + c2)  

    print(c1)  

    c1 += 5
    print(c1)  

    c1 += c2
    print(c1)  

    try:
        print(c1 + c3)  # Expected TypeError: Cannot add between Currency type <dollar> and <shekel>
    except TypeError as e:
        print(f"TypeError: {e}")

#Exrcice 3


import string
import random

def generate_random_string(length=5):
    letters = string.ascii_letters  
    return ''.join(random.choice(letters) for _ in range(length))

random_string = generate_random_string()
print(f"Random String: {random_string}")

#Exercice 4
from datetime import datetime

def display_current_date():
    current_date = datetime.now().date()
    print(f"Today's date: {current_date}")

display_current_date()

#Exercise 5

from datetime import datetime

def time_left_until_january_1st():
    current_date = datetime.now()
    next_year = current_date.year + 1
    january_1st_next_year = datetime(next_year, 1, 1)
    time_left = january_1st_next_year - current_date

    days_left = time_left.days
    hours_left = time_left.seconds // 3600
    minutes_left = (time_left.seconds % 3600) // 60

    print(f"Time left until January 1st of next year: {days_left} days, {hours_left} hours, {minutes_left} minutes")

time_left_until_january_1st()

#Exercice 6

from datetime import datetime

def minutes_lived_since_birth(birthdate):
    birthdate = datetime.strptime(birthdate, "2000-04-20")  
    current_time = datetime.now()
    time_lived = current_time - birthdate
    minutes_lived = time_lived.total_seconds() / 60
    
    print(f"You have lived approximately {int(minutes_lived)} minutes.")

birthdate_input = "2000-04-20"  # Replace this with the user's birthdate in "YYYY-MM-DD" format
minutes_lived_since_birth(birthdate_input)


#Daily Challenge

from math import pi

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = radius * 2
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("Please provide either radius or diameter")

    @property
    def area(self):
        return pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius: {self.radius} and diameter: {self.diameter}"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

# Example usage:
circle1 = Circle(radius=4)
circle2 = Circle(diameter=6)

print(circle1)  
print(circle2)

print(f"Area of circle 1: {circle1.area}")  
print(f"Area of circle 2: {circle2.area}")

circle3 = circle1 + circle2  
print(f"Circle 3 after addition: {circle3}")

print(f"Is circle 1 bigger than circle 2? {circle1 > circle2}")  
print(f"Are circle 1 and circle 2 equal? {circle1 == circle2}")

circles = [Circle(radius=5), Circle(radius=2), Circle(radius=7)]
sorted_circles = sorted(circles)


print("Sorted circles:")
for circle in sorted_circles:
    print(circle)
