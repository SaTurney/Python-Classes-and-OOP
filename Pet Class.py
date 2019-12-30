#Sabrina Turney
#November 12, 2018
#Pet Class
#In this program, we create an object of the class for "Pet" with specific 
#fields for pet name, type of animal, and age. We also have methods in the class
#to store values in each of the class fields, which will reture to the user once
#the user inputs their information responding to each class method.
#After we store the user input info in our object, the object accessor allows
#us to retrieve the data just entered and return it to display to the user.


#First of all, we create a class as required by the exercise.
#I changed the required "type" variable because in python, it is an operator.
class Pet():

    #Using python's init method to create the class, I pass all the required
    #variable names as arguments, along with "self", which is used throughout
    #the class.
    def __init__(self, name, petType, age):
        self.__name = name
        self.__petType = petType
        self.__age = age
        #to make things simpler, the class variables are minimized.


    #These are the methods that allow us to store the user input inside the
    #class instance. Each one is also reduced to a usable variable.
    def setName(self, name):
        self.__name = name
    def setType(self, petType):
        self.__petType = petType   
    def setAge(self, age):
        self.__age = age


    #These are the methods that return values to display to the user. Each one
    #is names by the exercise, but the accessing is the same.
    def getName(self):
        return self.__name
    def getType(self):
        return self.__petType
    def getAge(self):
        return self.__age

    
#This is our main function, where all the magic doesn't happen (that's all in
#the class above!) Here, we just print out our introduction, ask for our input,
#and return values stored in the class above.
def main():
    #Here's the intro, explaining what the program does for the user:
    print("Welcome to my Pet Class program!")
    print("Please enter your pet's name, the type of pet it is, and it's age,")
    print("And using class methods, I'll display that information to you!")

    #I use the reduced variables from the class to get input from the user.
    name = input("\nWhat is the name of your pet? ")
    petType = input("What type of pet do you own? ")
    age = input("And last but not least, how old is your pet? ")
    
    #Create an object of the class by calling the "userPet" variables to it.
    userPet = Pet(name, petType, age)

    #Here, the information is repeated back to the user from it's storage inside
    #the Pet class object variable. --------------------------------------------
    print("\n\nWow! So your pet's name is a", userPet.getName(), "!") 
    print("And the type of pet they are is a", userPet.getType(), ".")
    print("Lastly, your input says they're", userPet.getAge(), "years old! Wow!")
    #A simple goodbye after displaying relevant info:
    print("\nThank you for using my class program! Goodbye!")

#Last but not least, we call the main function for the user.    
main()
