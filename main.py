import sys
from data_reader import load_students, print_indiv_results
from classes import Student, Community

def find_student_by_name(students, name):
    for s in students:
        if s.name == name:  # must match exactly
            return s
    return None

def add_new_student(students):
    print('Add yourself as a new student:')

    name = input('Your name (for example: Alice F): ')

    sleep_s = input('Hours of sleep per day (0-24): ')
    study_s = input('Hours of study per day (0-24): ')
    stress_s = input('Stress level (1-10): ')

    try:
        sleep = int(sleep_s)
        study = int(study_s)
        stress = int(stress_s)
    except ValueError:
        print('Sorry, those must be whole numbers. Not adding student."')
        return

    if not (0 <= sleep <= 24 and 0 <= study <= 24 and 1 <= stress <= 10):
        print('Values are out of range. Not adding student.')
        return

    new_student = Student(name, sleep, study, stress)
    students.append(new_student)
    print('Added:', name)

def main(argv):
    if len(argv) < 2:
        print("Usage: python main.py <path-to-datafile>")
        return 2
    data_path = argv[1]

    students = load_students(data_path)
    print("Loaded students:", [s.name for s in students])
    if not students:
        print('No students found.')
        return 1

    answer = input('Would you like to add new students? (y/n): ')
    if answer.lower() == 'y':
        add_new_student(students)

    community = Community(students)

    print('Example names from the file: Alice F, Kara U, Kyli S, etc.')
    name_to_find = input('Enter the name of a student to view: ')

    student = find_student_by_name(students, name_to_find)

    if student is None:
        print('No such student found.')
    else:
        print_indiv_results([student], community)

    community.display_summary()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))






