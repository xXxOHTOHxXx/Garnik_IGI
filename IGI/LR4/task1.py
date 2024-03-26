import csv
import pickle
import random


class Student:
    def __init__(self, name, result_run:int, result_jump:int):
        self.__name = name
        self.__result_run = result_run
        self.__result_jump = result_jump

    @property    
    def name(self):
        return self.__name
    
    @property    
    def result_run(self):
        return self.result_run
    
    @result_run.setter
    def result_run(self,result):
        if 0 < result:
            self.result_run = result
        else:
            print("Inadmissible value")

    @property    
    def result_jump(self):
        return self.result_jump
    
    @result_jump.setter
    def result_jump(self,result):
        if 0 < result:
            self.result_jump = result
        else:
            print("Inadmissible value")

    def __str__(self):
        return f"{self.__name} result_run: {self.__result_run}  result_jumo: {self.__result_jump}"


def GetTop3(students):
    # Sort the students list in descending order of their results
    students.sort(key=lambda student: student.result, reverse=True)
    
    # Return the top 3 students
    return students[:3]

def GetExamPassed(result_run:int, result_jump:int, studentlist):
    passed_students = []
    for student in studentlist:
        if student.result_run >= result_run and student.result_jump >= result_jump:
            passed_students.append(student)
    return passed_students

        

def serialize_to_csv(data:dict, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['name', 'result_run', 'result_jump']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for person in data:
            writer.writerow({'name': person.name, 'result_run': person.result_run, 'result_jump': person.result_jump})

# Serializing with pickle
def serialize_with_pickle(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

# Deserialize from CSV
def deserialize_from_csv(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(Person(row['name'], row['result_run'], row['result_jump']))
    return data

# Deserialize with pickle
def deserialize_with_pickle(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

def StudentDictionaryGenerator(num_students: int = 10, min_result=0, max_result=20) -> dict:
    """
    Generates a dictionary of students with random results for testing.

    Args:
        num_students (int, optional): The number of students to generate. Defaults to 10.
        min_result (int, optional): The minimum possible result for run and jump. Defaults to 0.
        max_result (int, optional): The maximum possible result for run and jump (exclusive). Defaults to 20.

    Returns:
        dict: A dictionary where keys are student names and values are Student objects.
    """
    student_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Isabel", "Jack"]
    students = {}
    for _ in range(num_students):
        # Pick a random name from the list
        name = random.choice(student_names)
        student_names.remove(name)  # Avoid duplicates
        # Generate random results within the specified range
        result_run = random.randint(min_result, max_result - 1)
        result_jump = random.randint(min_result, max_result - 1)
        students[name] = Student(name, result_run, result_jump)
    return students