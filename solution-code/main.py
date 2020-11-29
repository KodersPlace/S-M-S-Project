from os import system

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
        'roll_no': 4,
        'name': 'Babar',
        'father_name': 'Hasan',
    },
    {
        'roll_no': 5,
        'name': 'Amir',
        'father_name': 'Salman',
    },
]


# ------------------------------------------------------------------

def add_student():
    global DATA
    name = input("Enter student name: ").strip()
    father_name = input("Enter father name: ").strip()
    if name == '' or father_name == '':
        print('Please give valid values')
        system('clear')
        return add_student()

    rolls = []
    for student in DATA:
        rolls.append(student['roll_no'])

    new_student = {
        'roll_no': max(rolls) + 1,
        'name': name,
        'father_name': father_name
    }
    DATA.append(new_student)
    print('Student successfully added!')


def view_students():
    global DATA
    print("---- STUDENTS' DATA ----")
    for student in DATA:
        print(
            f'{student["roll_no"]}  {student["name"]} {student["father_name"]}')
    return


def update_student():
    global DATA
    roll_no = int(
        input('Enter roll number of student you want to update: ').strip())

    index = None
    for i in range(len(DATA)):
        student = DATA[i]
        if student['roll_no'] == roll_no:
            index = i
            break

    if roll_no < 1 or index == None:
        print('Enter valid roll number')
        return update_student()

    updated_name = input('Enter updated name: ').strip()
    updated_father_name = input('Enter updated name: ').strip()

    if updated_name == '':
        updated_name = DATA[index]['name']
    if updated_father_name == '':
        updated_father_name = DATA[index]['father_name']

    updated_data = {
        'roll_no': roll_no,
        'name': updated_name,
        'father_name': updated_father_name
    }

    DATA[index] = updated_data

    print('Student updated successfully!')


def delete_student():
    global DATA
    roll_no = int(
        input('Enter roll number of student you want to delete: ').strip())

    index = None
    for i in range(len(DATA)):
        student = DATA[i]
        if student['roll_no'] == roll_no:
            index = i
            break

    if roll_no < 1 or index == None:
        print('Enter valid roll number')
        return update_student()

    DATA.pop(index)
    print('Student data successfully deleted!')


def main_menu():
    leading_spaces = "\t" * 3
    print(f'{leading_spaces}----WELCOME TO STUDENT MANAGEMENT SYSTEM----')
    print('Choose what you want to do?')
    # CRUD -> CREATE(ADD), READ(VIEW), UPDATE, DELETE
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
        print('Please select valid option')
        system('clear')
        return main_menu()

    system('clear')  # system('cls') <- for windows
    if option == 1:
        add_student()
    elif option == 2:
        view_students()
    elif option == 3:
        update_student()
    else:
        delete_student()

    input("Press any key to continue...")
    system('clear')
    main_menu()


def main():
    main_menu()


if __name__ == '__main__':
    main()
