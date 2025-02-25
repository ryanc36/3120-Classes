class Animal:
    def __init__(self, name, walk):
        self.__name = name 
        self.__walk = walk
        print("hello, I am", self.__name)

    def talk(self):
        print(self.__name, "hi")

    def walk(self):
        print(self.__name, "is walking", self.__walk)

    #def eat(self):
        #print(f"{self.__name} is eating.")

