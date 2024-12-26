def average_grades(grades: dict):
    total_grade = sum(
        sum(grades[course]) / len(grades[course]) / len(grades)
        if grades.get(course) else 0 for course in grades)
    return total_grade



class Student: #студенты
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.grades = {}
        self.finished_courses = []
        self.courses_in_progress = []


    # метод оценки лекторов
    def rate_lecturer(self, lecturer, course, grades):

        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grades]
            else:
                lecturer.grades[course] = [grades]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия {self.surname}\n'
                f'Средняя оценка за домашние задания: {average_grades(self.grades)}\n'
                f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {",".join(self.finished_courses)}\n'
                )

    def __lt__(self, other):
        return average_grades(self.grades) < average_grades(other.grades)

    def __gt__(self, other):
        return average_grades(self.grades) > average_grades(other.grades)

    def __eq__(self, other):
        return average_grades(self.grades) == average_grades(other.grades)


class Mentor: #Преподаватели
    def __init__(self, name, surname, ):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"имя: {self.name}\nфамилия: {self.surname}"


class Lecturer(Mentor): #Лекторы
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

        def __str__(self):
            return (
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {average_grades(self.grades)}\n'
            )


    def __lt__(self, other):
        return average_grades(self.grades) < average_grades(other.grades)

    def __gt__(self, other):
        return average_grades(self.grades) > average_grades(other.grades)

    def __eq__(self, other):
        return average_grades(self.grades) == average_grades(other.grades)


class Reviewer(Mentor): #критик
    pass


#метод оценки студентов
    def rate_homework(self, student, course, grades ):

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grades]
            else:
                student.grades[course] = [grades]
        else:
            return 'Ошибка'

        def __str__(self):
            return f"имя: {self.name}\nфамилия: {self.surname}"

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
        )

#Вычисляем среднею оценку студентов по курсу
def average_student_grade(students: list, course: str,):
    sum_grade = 0
    quantity_grade = 0
    for student in students:
        if course in student.grades:
            sum_grade += sum(student.grades[course])
            quantity_grade += len(student.grades[course])
    grades_average = sum_grade / quantity_grade if sum_grade else 0
    return f'Средня оценка по курсу {course} у студентов составляет {grades_average}'



#Вычисляем среднею оценку лекторов по курсу
def average_lecturer_grade(lecturers: list, course: str):
    sum_grades = 0
    quantity_grades = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            sum_grades += sum(lecturer.grades[course])
            quantity_grades += len(lecturer.grades[course])
    grade_average = sum_grades / quantity_grades if sum_grades else 0
    return f'Средня оценка по курсу {course} у лекторов составляет {grade_average}'


best_student = Student('Иван', 'Иванов', 'м')

best_student.courses_in_progress += ['Python', 'Git']

best_student.finished_courses += ['Введение в программирование']

average_student = Student('Никита', 'Никитин', 'м')

average_student.courses_in_progress += ['Python', 'ООП']

average_student.finished_courses += ['Введение в программирование', 'Git']

lecturer_best = Lecturer('Марина', 'Маринова')

lecturer_best.courses_attached += ['Python']

lecturer_average = Lecturer('Сергей', 'Сергеев')

lecturer_average.courses_attached += ['ООП']

reviewers_best = Reviewer('Петр', 'Петров')

reviewers_best.courses_attached += ['Python', 'Git']

reviewers_average = Reviewer('Анастасия', 'Анастасьева')

reviewers_average.courses_attached += ['ООП']

best_student.rate_lecturer(lecturer_best, 'Python', 10)

average_student.rate_lecturer(lecturer_best, 'Python', 9)

average_student.rate_lecturer(lecturer_average, 'ООП', 7)

reviewers_best.rate_homework(best_student, 'Python', 10)

reviewers_best.rate_homework(best_student, 'Git', 9)

reviewers_best.rate_homework(average_student, 'Python', 6)

reviewers_average.rate_homework(average_student, 'ООП', 8)


print(best_student)
print(average_student)

print(lecturer_best)
print(lecturer_average)

print(reviewers_best)
print(reviewers_average)


if best_student > average_student:
    print(f'{best_student.name} {best_student.surname} имеет более высокую среднюю оценку по курсу')
else:
    print(f'{average_student.name} {average_student.surname} имеет более высокую среднюю оценку по курсу')

if lecturer_best > lecturer_average:
    print(f'{lecturer_best.name} {lecturer_best.surname} имеет более высокую среднюю оценку за лекции')
else:
    print(f'{lecturer_average.name} {lecturer_average.surname} имеет более высокую среднюю оценку за лекции')

print(average_student_grade([best_student,average_student],'Python'))
print(average_lecturer_grade([lecturer_best,lecturer_average],'Python'))