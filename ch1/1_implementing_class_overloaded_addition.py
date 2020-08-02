#!/usr/bin/python3
#
# By Islam (esl4m)
# 1 Aug 2020
#

class Dog:
    # This is the constructor for the class. It is called whenever a Dog
    # object is created. The reference called "self" is created by Python
    # and made to point to the space for the newly created object. Python
    # does this automatically for us but we have to have "self" as the first
    # parameter to the __init__ method (i.e. the constructor).

    def __init__(self, name, month, day, year, speakText):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText

    # This is an accessor method that returns the speakText stored in the object. 
    # Notice that "self" is a parameter. Every method has "self" as its first parameter. 
    # The "self" parameter is a reference to the current object. 
    # The current object appears on the left hand side of the dot (i.e. the .) when the method is called.
    def speak(self):
        return self.speakText

    # Here is an accessor method to get the name
    def get_name(self):
        return self.name
    
    # This is another accessor method that uses the birthday information to
    # return a string representing the date.
    def birth_date(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)
    
    # This is a mutator method that changes the speakText of the Dog object.
    def change_bark(self, bark):
        self.speakText = bark
    
    # When creating the new puppy we don’t know it’s birthday. Pick the first dog’s birthday plus one year. 
    # The speakText will be the concatenation of both dog’s text. The dog on the left side of the + 
    # operator is the object referenced by the "self" parameter.
    # The "other_dog" parameter is the dog on the right side of the + operator. 
    def __add__(self, other_dog):
        return Dog("Puppy of " + self.name + " and " + other_dog.name, self.month, self.day, self.year + 1, self.speakText + other_dog.speakText)

def main():
    boy_dog = Dog("Mesa", 5, 15, 2004, "WOOOOF") 
    girl_dog = Dog("Sequoia", 5, 6, 2004, "barkbark") 
    print(boy_dog.speak())
    print(girl_dog.speak())
    print(boy_dog.birth_date())
    print(girl_dog.birth_date())
    boy_dog.change_bark("woofywoofy")
    print(boy_dog.speak())
    puppy = boy_dog + girl_dog
    print(puppy.speak())
    print(puppy.get_name())
    print(puppy.birth_date())

if __name__ == "__main__":
    main()
