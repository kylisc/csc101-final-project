from classes import Student, Community

def read_student_line(line, line_num):
    raw = line.strip()
    if raw == '':
        return None
    if raw[0] == '#':
        return None

    parts = [p.strip() for p in raw.split(',')]

    if len(parts) != 4:
        print("  Error", raw)
        return None

    name = parts[0]
    sleep_s = parts[1]
    study_s = parts[2]
    stress_s = parts[3]

    try:
        sleep = int(sleep_s)
        study = int(study_s)
        stress = int(stress_s)
    except ValueError:
        print("  Error", raw)
        return None

    if not (0 <= sleep <= 24 and 0 <= study <= 24 and 1 <= stress <= 10):
        print("  Error", raw)
        return None

    return Student(name, sleep, study, stress)

def load_students(path):
    students = []

    try:
        file = open(path, 'r')
    except FileNotFoundError:
        print("  Error", path)
        return students

    line_num = 1
    for line in file:
        s = read_student_line(line, line_num)
        if s is not None:
            students.append(s)
        line_num += 1

    file.close()
    return students

def print_indiv_results(students, community):
    for s in students:
        score, label = s.wellness_score()
        print()
        print('Student:', s.name)
        print('Sleep:', s.sleep_hours, 'hours')
        print('Study:', s.study_hours, 'hours')
        print('Stress Level:', s.stress_level)
        print('Wellness Score:', score, '(', label, ')')
        print('Tip:', community.tip_for_student(s))