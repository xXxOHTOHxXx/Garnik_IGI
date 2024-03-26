import random

def random_list(n: int, min_val: int = -100, max_val: int = 100):
    return [random.randint(min_val, max_val) for _ in range(n)]

def GetIntNumber(msg:str) -> int:
    while True:
        print(f"{msg}")
        input_string = input()
        try:
            return int(input_string)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    

def GetFloatNumber(msg:str) -> float:
    while True:
        print(f"{msg}")
        input_string = input()
        try:
            return float(input_string)
        except ValueError:
            print("Invalid input. Please enter a float number.")
    