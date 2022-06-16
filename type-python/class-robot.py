class Robot:
    count = 0

    def __init__(self, name, code):
        self.name = name
        self.code = code
        Robot.count += 1

    def greeting(self):
        print(f"greetings, my master call me {self.name}({self.code}).")

    def add_number(self, a, b):
        return a + b

    def destroy(self):
        print(f"{self.name} is being destroyed.")

    @classmethod
    def how_many(cls):
        print(f"We have {cls.count} robots.")

    def __str__(self):
        return f"magic method str {self.name} !!"

    def __call__(self):
        print("magic method call")
        return f"magic method call {self.name} !!"


print(Robot.count)

siri = Robot("siri", 11451)
siri.greeting()
bixby = Robot("bixby", 11452)
bixby.greeting()

Robot.how_many()

print(bixby)
print(bixby())