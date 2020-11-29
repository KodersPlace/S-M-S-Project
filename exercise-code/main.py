from os import system

# https://github.com/KodersPlace/S-M-S-Project/

# ------------------------ Global data dictionary ------------------
DATA = [
    {
        'roll_no': 1,
        'name': 'Ali',
        'father_name': 'Ahmad',
    },
    {
        'roll_no': 2,
        'name': 'Obaid',
        'father_name': 'Atif',
    },
    {
        'roll_no': 3,
        'name': 'Aslam',
        'father_name': 'Iftikhar',
    },
    {
        'roll_no': 5,
        'name': 'Babar',
        'father_name': 'Hasan',
    },
    {
        'roll_no': 6,
        'name': 'Amir',
        'father_name': 'Salman',
    },
]
# ------------------------------------------------------------------


def add_student():
    global DATA
    # roll number (automatic)
    # student name
    # father name
    name = input("Enter student's name: ").strip()
    father_name = input("Enter father's name: ").strip()

    # if name or father name is not provided
    if not name or not father_name:
        print('Please provide all the details.')
        input('Press enter to continue')
        system('clear')
        return add_student()

    rolls = []  # list of roll numbers of students
    for student in DATA:
        rolls.append(student['roll_no'])

    roll_no = max(rolls) + 1
    new_student = {
        'roll_no': roll_no,
        'name': name,
        'father_name': father_name
    }
    DATA.append(new_student)
    print('Student added successfully.')


def update_student():
    global DATA
    # roll number(from user)
    roll_no = int(input('Enter roll number of student you want to update: ').strip())

    rolls = []  # list of roll numbers of students
    for student in DATA:
        rolls.append(student['roll_no'])

    # invalid roll number
    if roll_no not in rolls:
        print('Enter valid roll number')
        return update_student()

    # name (from user)
    # father name (from user)
    updated_name = input('Enter updated name: ').strip()
    updated_father_name = input('Enter updated name: ').strip()

    # student data on which in DATA
    index = rolls.index(roll_no)

    # update the index (student data)
    if not updated_name:
        updated_name = DATA[index]['name']
    if not updated_father_name:
        updated_father_name = DATA[index]['father_name']

    updated_data = {
        'roll_no': roll_no,
        'name': updated_name,
        'father_name': updated_father_name
    }

    DATA[index] = updated_data
    print('Student updated successfully!')


def view_students():
    global DATA
    print("\t\t\t---- STUDENTS' DATA ----")
    for student in DATA:
        print(f'{student["roll_no"]}  {student["name"]} {student["father_name"]}')
    return


def delete_student():
    global DATA
    # roll number (user)
    roll_no = int(input('Enter roll number of student you want to delete: ').strip())

    # validity of roll number
    rolls = []  # list of roll numbers of students
    for student in DATA:
        rolls.append(student['roll_no'])

    # invalid roll number
    if roll_no not in rolls:
        print('Enter valid roll number')
        return delete_student()

    # index of student
    index = rolls.index(roll_no)

    # remove that index
    DATA.pop(index)
    print('Student data successfully deleted!')


def main():
    print('\t\t\t----WELCOME TO STUDENT MANAGEMENT SYSTEM-----')
    print('Choose what you want to do?')

    # CRUD <- Create(Add), Read(View), Update, Delete
    print('1- Add a student.')
    print('2- View students.')
    print('3- Update student data.')
    print('4- Delete student data.')
    print('5- Exit.')

    option = int(input("Enter option: ").strip())

    if option == 5:
        return

        # for invalid option value
    if option < 1 or option > 4:
        print('Please select a valid option.')
        input('Press enter key to continue...')
        system('clear')
        return main()

    # for valid options
    if option == 1:
        add_student()
    elif option == 2:
        view_students()
    elif option == 3:
        update_student()
    else:
        delete_student()

    input('Press enter to continue')
    return main()


main()
print('Good Bye!!')
