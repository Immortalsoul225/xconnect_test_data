import random
import copy

class Lecture:
    def __init__(self, subject, teacher):
        self.subject = subject
        self.teacher = teacher

class Timetable:
    def __init__(self, days):
        self.days = days
        self.schedule = {day: [] for day in days}

    def add_lecture(self, day, lecture):
        self.schedule[day].append(lecture)

def generate_initial_population(classes, teachers, days, timetable_count):
    population = []
    for _ in range(timetable_count):
        timetable = {class_: Timetable(days) for class_ in classes}
        for day in days:
            for class_ in classes:
                subjects = classes[class_]
                random.shuffle(subjects)
                
                for subject in subjects:
                    teacher = random.choice(teachers[subject])
                    lecture = Lecture(subject, teacher)
                    timetable[class_].add_lecture(day, lecture)
        population.append(timetable)
    return population

def fitness(timetable):
    conflicts = 0
    for class_, schedule in timetable.items():
        teacher_lectures = {}
        for day, lectures in schedule.schedule.items():
            for lecture in lectures:
                teacher = lecture.teacher
                if teacher in teacher_lectures:
                    if day in teacher_lectures[teacher]:
                        conflicts += 1
                    else:
                        teacher_lectures[teacher].append(day)
                else:
                    teacher_lectures[teacher] = [day]
    return conflicts

def crossover(parent1, parent2):
    child = copy.deepcopy(parent1)
    for class_, schedule in child.items():
        for day, lectures in schedule.schedule.items():
            for lecture in lectures:
                if random.choice([True, False]):
                    teacher = random.choice(parent2[class_].schedule[day]).teacher
                    child[class_].add_lecture(day, Lecture(lecture.subject, teacher))
    return child

def mutate(timetable, teachers, days):
    mutated_timetable = copy.deepcopy(timetable)
    class_to_mutate = random.choice(list(mutated_timetable.keys()))
    day_to_mutate = random.choice(days)
    
    # Remove a random lecture
    if mutated_timetable[class_].schedule[day_to_mutate]:
        mutated_timetable[class_].schedule[day_to_mutate].pop(random.randint(0, len(mutated_timetable[class_].schedule[day_to_mutate])-1))

    # Add a new random lecture
    subjects = classes[class_to_mutate]
    random.shuffle(subjects)
    teacher = random.choice(teachers[random.choice(subjects)])
    new_lecture = Lecture(random.choice(subjects), teacher)
    mutated_timetable[class_].add_lecture(day_to_mutate, new_lecture)

    return mutated_timetable

def genetic_algorithm(classes, teachers, days, timetable_count, generations):
    population = generate_initial_population(classes, teachers, days, timetable_count)
    for generation in range(generations):
        population.sort(key=lambda x: fitness(x))
        if fitness(population[0]) == 0:
            return population[0]
        
        # Select the top 10% of the population as parents
        parents = population[:int(timetable_count * 0.1)]

        # Generate offspring through crossover
        offspring = []
        for _ in range(timetable_count - len(parents)):
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2)
            offspring.append(child)

        # Apply mutation to some offspring
        for _ in range(int(timetable_count * 0.1)):
            mutated_child = mutate(random.choice(offspring), teachers, days)
            offspring.append(mutated_child)

        # Combine parents and offspring to form the next generation
        population = parents + offspring

    return population[0]

if __name__ == "__main__":
    classes = {
        "FY": ["stalin", "worral", "aqualla", "arti"],
        "SY": ["rushita", "worral", "aqualla", "Edward"],
        "TY": ["vipul", "worral", "aqualla", "rushita"]
    }
    teachers = {
        "stalin": ["Subject A"],
        "worral": ["Subject B"],
        "aqualla": ["Subject C"],
        "arti": ["Subject D"],
        "rushita": ["Subject E"],
        "Edward": ["Subject F"],
        "vipul": ["Subject G"]

    }
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    timetable_count = 100
    generations = 1000

    final_timetable = genetic_algorithm(classes, teachers, days, timetable_count, generations)
    
    print("\nFinal Timetable:")
    for class_, schedule in final_timetable.items():
        print(f"\nTimetable for {class_} class:")
        for day, lectures in schedule.schedule.items():
            print(f"\n{day}:")
            for lecture in lectures:
                print(f"{lecture.subject} - {lecture.teacher}")

