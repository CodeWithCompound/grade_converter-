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
                        percent = int(x)
                        return percent
                except ValueError:
                        print("Error - NaN")

def convert_percent():
        while True:
                


while True:
        percent = 0
        points = 0
        max_points = 0                        
        choice = input("please choose between entering a percent of right awnsers (enter 1) or if you want to enter the point you got and the maximum you could have gotten\n").strip()

        try:
                choice = int(choice)
        except ValueError:
                print("fucking enter 1 or 2 you dumbass")
        
        if choice == 1:
                percent = input(f"please enter the % you got")
                percent = check_int(percent)
                
        elif choice == 2:
                input(f"")
        
        else: 
                print("Error- Enter either 1 or 2")
                break
        
        german_grade = 1
        cambridge_grade = 1



        for grade in valueGerm:
                if percent >= grade.value:
                        german_grade = grade.name
                        break
        
        for grade in valueCambridge:
                if percent >= grade.value:
                        cambridge_grade = grade.name
                        break


        print(f"\nWith your {percent}% you would be getting a {german_grade} in germany or a {cambridge_grade} in Cambridge!")