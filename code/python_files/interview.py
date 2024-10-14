# Create a class "Populate" having a default constructor to initialize two data frames with data mentioned below

# id 	name	gender 	marks
# 10	Abhijit	M	20
# 20	Neha	F	40
# 30	Rahul	M	60
# 40	Sneha	F	80

# id 	name	gender 	marks
# 10	Abhijit	M	20
# 20	Neha	F	40
# 50	Amit	M	100
# 60	Laxmi	F	120

# 1. Perform merge operation using each function for inner and outer
# 2. All variable considered must be private variables
# 3. In main function create an object of this class and call each function

import pandas as pd


class Populate:
    def __init__(self):
        self.__df1 = pd.DataFrame({
            "id": [10, 20, 30, 40],
            "name": ["Abhijit", "Neha", "Rahul", "Sneha"],
            "gender": ["male", "female", "male", "female"],
            "marks": [20, 40, 60, 80]
        })

        self.__df2 = pd.DataFrame({
            "id": [10, 20, 50, 60],
            "name": ["Abhijit", "Neha", "Amit", "Laxmi"],
            "gender": ["male", "female", "male", "female"],
            "marks": [20, 40, 60, 80]
        })

    def merge_operation_inner(self):
        self.__dfrmi = pd.merge(self.__df1, self.__df2, on='id')

    def merge_operation_outer(self):
        self.__dfrmo = pd.merge(self.__df1, self.__df2, on='id', how="outer")

    def display(self):
        print(self.__df1)
        print(self.__df2)
        print(self.__dfrmi)
        print(self.__dfrmo)


p = Populate()
p.merge_operation_inner()
p.merge_operation_outer()
p.display()
