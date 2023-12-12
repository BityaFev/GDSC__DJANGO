Student_List = []
def Add_newstudent():
    Name = input ("Enter name: ")
    Age = input ("Enter student's age: ")
    School = input ("Enter the school: ")
    Grade = input ("Enter the year of study: ")
    List_of_students = {'Student_name' : Name, 'Student_age': Age, 'Student_school': School, 'Student_year_of_study' : Grade}
    Student_List.append(List_of_students)
def Show_list():
    print(List_of_students)
    for List_of_students in Student_List:
        print(f"Name: {Student_List['Student_name']}")
        print(f"Age: {Student_List['Student_age']}")
        print(f"School: {Student_List['Student_school']}") 
        print(f"Grade: {Student_List['Student_year_of_study']}")
def pick_a_student():
    name_searched = input('Student to be picked: ')
    for List_of_students in Student_List:
        if List_of_students['Student_name'] == name_searched:
            print(f"Name: {Student_List['Student_name']}")
            print(f"Age: {Student_List['Student_age']}")
            print(f"School: {Student_List['Student_school']}") 
            print(f"Grade: {Student_List['Student_year_of_study']}")
def update():
    name_searched = input('Student to be picked: ')
    for List_of_students in Student_List:
       if List_of_students['Student_name'] == name_searched:
         new_Name = input ("Enter name: ")
         List_of_students['Name'] =new_Name
         new_Age = input ("Enter students age: ")
         List_of_students['Age'] = new_Age
         new_School = input ("Enter the school: ")
         List_of_students['School'] = new_School
         new_Grade = input ("Enter the year of study: ")
         List_of_students['Grade'] = new_Grade
def delete():
 for List_of_students in Student_List:
        if List_of_students['Student_name'] == name_searched:
         Student_List.remove(List_of_students)
def main():
    while True:
        print("Student Database")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            Add_newstudent()
        elif choice == '2':
            Show_list()
        elif choice == '3':
            update()
        elif choice == '4':
            delete()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
Student_List = []
main()