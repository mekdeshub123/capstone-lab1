class Student:
    def __init__(self, name, college_id, gpa):
        self.name = name
        self.college_id = college_id
        self.gpa = gpa
    def __str__(self): 
        return f'Name: {self.name}, id: {self.college_id}, gpa: {self.gpa}'

def main():
    mekdes = Student('Mekdes', '4567', '3.00,') 
    urgessa = Student('Urgessa', '3213', '4.00')
    peter = Student('Peter', '00998', '3.5')

    print(mekdes)
    print(urgessa)
    print(peter)
main()
 