class Animal:
    def __init__(self, name, walk, eat):
        self.__name = name 
        self.__walk = walk
        self.__eat = eat
        print("hello, I am", self.__name)

    def talk(self):
        print(self.__name, "hi")

    def walk(self):
        print(self.__name, "is walking", self.__walk)

    def eat(self):
        print(self.__name, "is eating", self.__eat)

