def average_rating(grades):
    if len(grades) < 1:
        return 0
    else:
        gr = []
        for el in grades:
            gr.extend(grades[el])
        res = sum(gr)/len(gr)
        return res

def grades_course(lst, course):
    gr = []
    for man in lst:
        if course in man.grades.keys():
            gr.extend(man.grades[course])
    res = sum(gr)/len(gr)
    return res

class Student:
    students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.students.append(self)

    def grade_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_rating(self.grades)}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершённые курсы: {', '.join(self.finished_courses)}"
        return res


    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other} не студент.')
            return
        return average_rating(self.grades) < average_rating(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    lectors = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        Lecturer.lectors.append(self)

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_rating(self.grades)}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other} не лектор.')
            return
        return average_rating(self.grades) < average_rating(other.grades)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


roman = Student('Роман', 'Чернов', 'мужчина')
roman.courses_in_progress += ['Python', 'Git', 'ООП']
roman.finished_courses = ['Дизайн']

anya = Student('Аня', 'Форджер', 'девушка')
anya.courses_in_progress += ['Python', 'Git']
anya.finished_courses = ['Введение в программирование']

oleg = Lecturer('Олег', 'Булыгин')
oleg.courses_attached += ['Python', 'ООП']

jenya = Lecturer('Евгений', 'Егоров')
jenya.courses_attached += ['Python']

alyona = Lecturer('Алёна', 'Батицкая')
alyona.courses_attached += ['Git']

femida = Reviewer('Фемида', 'Справедливая')
femida.courses_attached += ['Python', 'ООП']

fsb = Reviewer('Анатолий', 'Стрельцов')
fsb.courses_attached += ['Git']


femida.rate_hw(roman, 'Python', 10)
femida.rate_hw(roman, 'OOP', 8)
fsb.rate_hw(roman, 'Git', 8)
print(roman)

print()

femida.rate_hw(anya, 'Python', 5)
fsb.rate_hw(anya, 'Git', 3)
print(anya)

print()

print(f'Оценки Романа лучше, чем у Ани: {roman > anya}')

print()

anya.grade_lector(oleg, 'Python', 9)
roman.grade_lector(oleg, 'Python', 10)
roman.grade_lector(oleg, 'OOP', 10)
print(oleg)

print()

anya.grade_lector(jenya, 'Python', 6)
roman.grade_lector(jenya, 'Python', 7)
print(jenya)

print()

anya.grade_lector(alyona, 'Git', 9)
roman.grade_lector(alyona, 'Git', 10)
print(alyona)

print()

print(f'Оценки Олега хуже, чем у Алёны: {oleg < alyona}')

print()

print(femida)

print()

print(f"Средняя оценка всех студентов по дисциплине Git: {grades_course(Student.students, 'Git')}")
print(f"Средняя оценка всех лекторов по дисциплине Python: {grades_course(Lecturer.lectors, 'Python')}")
