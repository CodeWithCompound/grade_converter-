from dataclasses import dataclass
from typing import List

@dataclass
class Grade:
        name : str
        value: float

valueGerm: List[Grade] = [
        Grade("1", 91),
        Grade("2", 81),
        Grade("3", 66),
        Grade("4", 50),
        Grade("5", 49),
        Grade("6", 0),
]

valueCambridge: List[Grade] = [
        Grade("9", 95),
        Grade("8 / A*", 90),
        Grade("7 / A", 80),
        Grade("6 / B", 70),
        Grade("5 / C", 65),
        Grade("4 / C", 60),
        Grade("3 / D", 50),
        Grade("3 / E", 40),
        Grade("2 / F", 30),
        Grade("1 / G", 20),
        Grade("U", 0)
]

def check_int(x):
                try:
                        x = int(x)
                        return x
                except ValueError:
                        print("Error - NaN")

# -- Lets you choose between % or points/max_points --
def evaluate_choice():
        while True:
                choice = input(f"Enter either \n1: if you have the % of right questions \n\nor\n\n 2: if you have the amount of points you got AND the maximum points you could have gotten\n").strip()
                
                try:
                        choice = int(choice)
                except ValueError:
                        print("fucking enter 1 or 2 you dumbass")
                if choice == 1:
                        percent = convert_percent()
                        return percent
                elif choice == 2:
                        percent = convert_points()
                        return percent
                else:
                        print("Error- Enter either 1 or 2")
                        
        
def convert_percent():
        try:
                print(f"\nProceed with entering your % below: ")
                percent = int(input(f""))
                return percent
        except ValueError:
                print("\nError - NaN (Points!)") 
                

def convert_points():
        while True:
                print(f"\nPlease enter the amount of points you got")

                try:
                        points = int(input(f"Enter your points: "))
                except ValueError:
                        print("\nError - NaN (Points!)") 
                        break
                
                print(f"\nAlright! now we just need to know how many points in total you could have gotten!")
                try:
                        max_points = int(input(f"Enter max points: "))
                except ValueError:
                        print("\nError - NaN (MaxPoints!)") 
                        break

                if points > max_points:
                        print(f"\nYou can't have {points} when the maximum you can get is {max_points}!")
                
                percent = (points / max_points * 100)
                return percent
                
while True:
        percent = 0
        points = 0
        max_points = 0                        
        german_grade = 1
        cambridge_grade = 1

        percent = evaluate_choice()

        for grade in valueGerm:
                if percent >= grade.value:
                        german_grade = grade.name
                        break
        
        for grade in valueCambridge:
                if percent >= grade.value:
                        cambridge_grade = grade.name
                        break

        print(f"\nWith your {percent}% you would be getting a {german_grade} in germany or a {cambridge_grade} in Cambridge!")