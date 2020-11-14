import openpyxl
import openpyxl.utils



def find_average():
    all_grades = [70.98, 76.87, 78.56, 66.32, 90.87, 98.34, 85.12, 56.25, 91.63, 87.81,90]
    count = -1
    total = 0
    for grade in all_grades:
        count +=1
        if type(grade) is str:
            continue
        total = total+grade
    average_grade = total/count
    print(f"The average grade for the class is {average_grade:.2f}")

find_average()
