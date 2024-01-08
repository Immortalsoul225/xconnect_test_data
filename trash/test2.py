import random

class Lecture:
    def __init__(self, class_name, subject, teacher):
        self.class_name = class_name
        self.subject = subject
        self.teacher = teacher

class Timetable:
    def __init__(self, days):
        self.days = days
        self.schedule = {day: [] for day in days}

    def add_lecture(self, day, lecture):
        self.schedule[day].append(lecture)

def generate_timetable(classes, teachers, days):
    timetable = {class_: Timetable(days) for class_ in classes}

    for class_ in classes:
        subjects = ["Subject A", "Subject B", "Subject C"]
        random.shuffle(subjects)

        for subject in subjects:
            teacher = random.choice(teachers[subject])
            for day in days:
                lectures_of_teacher = [lecture.teacher for timetable_class in timetable.values() for timetable_day, timetable_lectures in timetable_class.schedule.items() for lecture in timetable_lectures if lecture.teacher == teacher]
                
                available_days = [d for d in days if d not in timetable[class_].schedule or len(timetable[class_].schedule[d]) < 6]
                if not available_days:
                    break

                day = random.choice(available_days)
                lecture = Lecture(class_, subject, teacher)
                timetable[class_].add_lecture(day, lecture)

    return timetable

def print_timetable(timetable):
    for class_, schedule in timetable.items():
        print(f"\nTimetable for {class_} class:")
        for day, lectures in schedule.schedule.items():
            print(f"\n{day}:")
            for lecture in lectures:
                print(f"{lecture.subject} - {lecture.teacher}")

if __name__ == "__main__":
    classes = ["FY", "SY", "TY"]
    teachers = {
        "Subject A": ["Teacher A", "Teacher B"],
        "Subject B": ["Teacher C", "Teacher D"],
        "Subject C": ["Teacher E", "Teacher F"]
    }
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    timetable = generate_timetable(classes, teachers, days)
    print_timetable(timetable)
