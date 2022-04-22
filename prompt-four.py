#write a python program that declares a class
#describing your favorite animal. Have the data
#members of the class represent the following 
#physical parameters of the animal: length of 
#the arms(float), length of the legs(float), 
#number of eyes(int), does it have a tail? (bool),
#is it furry? (bool). Write an intialization
#function that sets the alues of the data members
#when an instance of the calss is created. Write
#a member function fo the class to print out and 
#describe the data members representing the 
#physical characteristics of the animal


#creating dog class for maltipoo
class dog:

        #creating the attributes
        def __init__(self, arm_length, eyes, tail, furry):
                self.arm_length = arm_length
                self.eyes= eyes 
                self.tail = "yes"
                self.furry = "yes"
                
        #This will print all the information
        def print_description(self):
               print(f'arm length = {self.arm_length}\n eyes = {self.eyes}\n tail = {self.tail}\n fur = {self.furry}')

#instantation

dog = dog(4.0, 2, True, True)
dog.print_description()
