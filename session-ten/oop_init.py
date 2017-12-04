class Person:
    def __init__(self, name="anonymous"):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)


if __name__ == "__main__":
    p = Person('Fred')
    p.say_hi()
    # The previous 2 lines can also be written as
    Person().say_hi()
