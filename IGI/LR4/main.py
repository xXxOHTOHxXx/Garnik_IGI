#Гарник Антон Павлович
#253502
#Вариант 7
#16.03.2024
import task1, task2, task3, task4, task5
import misc


#main menu function that asks for task pick through console input and calls appropriate func
def main_menu():
    flag =int(misc.GetIntNumber("Write a task number from 1 to 5 or -1 to end:\n"))
    if flag==1:#fin
        runreq:float = int(misc.GetIntNumber("Enter qualifying running time\n"))
        jumpreq:float = float(misc.GetFloatNumber("Enter qualifying jump length\n"))
        students = task1.StudentDictionaryGenerator()

        for student in students:
            print(str(student))

        task1.serialize_to_csv(students, "csvtask1.csv")
        studentscsv = task1.deserialize_from_csv("csvtask1.csv")

        print("students from csv: ")
        for student in studentscsv:
            print(str(student))

        task1.serialize_with_pickle(students, "pickletask1.json")
        studentscsv = task1.deserialize_with_pickle("pickletask1.json")
   
    if flag==2:#fin
        task2.task2sum()
        return 0
    if flag==3:#fin
        x:int = int(misc.GetIntNumber("Enter x\n"))
        eps:float = float(misc.GetFloatNumber("Enter eps\n"))
        task1.powseq(x, eps)
        input()
        return 0
    if flag==4:#fin
        task4.process_text()
        return 0
    if flag==5:
        choice = int(misc.GetIntNumber("Generate list(1) or enter manually(2)?"))
        list = []
        if choice==1:
            n = int(misc.GetIntNumber("Enter list length"))
            list =misc.random_list(n)
            for num in list:
                print(f"{num} ")
        elif choice==2:
            input_string = input("Enter list: ")
            list = [int(i) for i in input_string.split()]
        C = float(misc.GetFloatNumber("Enter number C: "))
        task5.calculate_elements(list,C)
        return 0
    if flag==-1:
        return -1
    else:
        print("Incorrect input!")
        return 0

    


while True:
    if main_menu()==-1:
        exit()