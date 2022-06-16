from datetime import datetime


class Robot:
    count = 0

    def __init__(self, name, code):
        self.__name = name
        self.code = code
        Robot.count += 1

    def greeting(self):
        print(f"greetings, my master call me {self.name}({self.code}).")

    def add_number(self, a, b):
        return a + b

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) == 0:
            raise TypeError("invalid length")
        else:
            self.__name = new_name

    def destroy(self):
        print(f"{self.name} is being destroyed.")

    @classmethod
    def how_many(cls):
        print(f"We have {cls.count} robots.")


class Siri(Robot):

    def __init__(self, name, code, birth):
        super().__init__(name, code)
        self.__birth = birth

    def hello_apple(self):
        print(f"apple {self.name}, {self.code}, {self.__birth}")

    def greeting(self):
        print(f"greetings, my master call me {self.name}({self.code}, {self.__birth}).")

    def get_age(self):
        birth = datetime.strptime(self.__birth, '%Y-%m-%d').date()
        today = datetime.now().date()
        year = today.year - birth.year

        if today.month < birth.month or (today.month == birth.month and today.day < birth.day):
            return year - 1

        return year

    def say_age(self):
        print(f"Siri is {self.get_age()} years old")


siri = Siri("siri", 11451, "1988-08-10")
siri.greeting()
siri.hello_apple()
siri.say_age()

siri.name = 'siri2'
siri.greeting()
