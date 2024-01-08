import random

class Lecture:
    def __init__(self, day, subject, teacher):
        self.day = day
        self.subject = subject
        self.teacher = teacher

class Timetable:
    def __init__(self, days):
        self.days = days
        self.schedule = {day: [] for day in days}

    def add_lecture(self, lecture):
        self.schedule[lecture.day].append(lecture)

def generate_timetable(classes, teachers, days):
    timetable = {class_: Timetable(days) for class_ in classes}
    
    for class_ in classes:
        subjects = teachers[class_].keys()
        for subject in subjects:
            teacher = teachers[class_][subject]
            available_days = days.copy()
            random.shuffle(available_days)
            
            for _ in range(4):
                if not available_days:
                    break
                day = available_days.pop()
                lecture = Lecture(day, subject, teacher)
                timetable[class_].add_lecture(lecture)

    return timetable

def print_timetable(timetable):
    for class_, schedule in timetable.items():
        print(f"\nTimetable for {class_} class:")
        for day, lectures in schedule.schedule.items():
            print(f"\n{day}:")
            for lecture in lectures:
                print(f"{lecture.teacher} - {lecture.subject} ")

if __name__ == "__main__":
    classes = ["FY", "SY", "TY"]
    teachers = {
        "FY": {"Math": "Teacher1", "Physics": "Teacher2","Chemistry": "Teacher3", "Biology": "Teacher4","History": "Teacher5", "Geography": "Teacher6"},
        "SY": {"Math": "Teacher1", "Physics": "Teacher2","Chemistry": "Teacher3", "Biology": "Teacher4","History": "Teacher5", "Geography": "Teacher6"},
        "TY": {"Math": "Teacher1", "Physics": "Teacher2","Chemistry": "Teacher3", "Biology": "Teacher4","History": "Teacher5", "Geography": "Teacher6"}
    }
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday"]

    timetable = generate_timetable(classes, teachers, days)
    print_timetable(timetable)