class Person:
    def __init__(self, first_name: str, last_name: str, age: int, height: float,) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.is_happy = True

def introduce_yourself(self) -> None:
    happiness_status = 'happy' if self.is_happy else 'not feeling happy right now'
    print(f'Hi, my name is {self.first_name}{self.last_name}. '
          f'I am {self.age} years old, {self.height} meters tall, and I\'m {happiness_status}.')

# Create a Person: 
# my_friend = Person('John', 'Doe', 30, 1.75)

