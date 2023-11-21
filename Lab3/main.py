from teacher import Teacher
from group import Group

import time
import random
from numpy.random import rand
from numpy.random import randint
from collections import defaultdict

#constants
n_iter = 50
n_pop = 100
n_classes = 7
r_cross = 0.9
r_mut = 1.0 / float(5*10)

days = [
	"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
]

subjects = [
	"Math", "Physics", "Chemistry", "Biology",
	"History", "Geography", "English", "Literature",
	"Computer Science", "Programming", "Music", "Art", 
	"None"
]

teachers = [
	Teacher(name="John Doe", subjects=["Math", "Physics"], max_hours=30),
	Teacher(name="Jane Smith", subjects=["Chemistry", "Biology"], max_hours=27),
	Teacher(name="Alice Johnson", subjects=["History", "Geography"], max_hours=24),
	Teacher(name="Bob Wilson", subjects=["English", "Literature"], max_hours=26),
	Teacher(name="Eva Brown", subjects=["Computer Science", "Programming"], max_hours=30),
	Teacher(name="David Miller", subjects=["Music"], max_hours=25),
	Teacher(name="Sophia Lee", subjects=["Art"], max_hours=25),
	Teacher(name="Daniel Davis", subjects=["Math"], max_hours=18),
	Teacher(name="Emma Taylor", subjects=["English"], max_hours=21),
	Teacher(name="Michael White", subjects=["Programming"], max_hours=21),
	Teacher(name="Olivia Anderson", subjects=["History"], max_hours=20),
	Teacher(name="William Harris", subjects=["Biology"], max_hours=19),
	Teacher(name="Ava Martin", subjects=["Literature"], max_hours=18),
	Teacher(name="Liam Wilson", subjects=["Computer Science"], max_hours=20),
	Teacher(name="Abigail Moore", subjects=["History", "Geography"], max_hours=24),
	Teacher(name="James Robinson", subjects=["Physics"], max_hours=19),
	Teacher(name="Emily Garcia", subjects=["Math"], max_hours=25),
	Teacher(name="Logan Thomas", subjects=["English"], max_hours=22),
	Teacher(name="Harper Lee", subjects=["Computer Science", "Programming"], max_hours=18),
	Teacher(name="Mia Thompson", subjects=["Chemistry"], max_hours=16)
]

groups = [
    Group(group_name="Group1", subjects_hours={"Math": 2, "Physics": 3, "Chemistry": 3, "English": 2, "Programming": 4, "Literature": 4, "History": 1, "Computer Science": 2, "Geography": 4}),
    Group(group_name="Group2", subjects_hours={"English": 3, "Literature": 3, "History": 3, "Biology": 2,  "Computer Science": 3, "Math": 1, "Physics": 2, "Chemistry": 3}),
    Group(group_name="Group3", subjects_hours={"Computer Science": 2, "Programming": 1, "Math": 4, "Physics": 2, "Literature": 4, "Geography": 1, "History": 4, "Biology": 2, "Chemistry": 4, "Music": 4}),
    Group(group_name="Group4", subjects_hours={"Music": 4, "Art": 2, "History": 3, "Computer Science": 1, "Programming": 1,  "Biology": 3, "English": 3,"Physics": 3, "Math": 2}),
    Group(group_name="Group5", subjects_hours={"English": 2, "Literature": 4, "Biology": 2, "Geography": 3, "Chemistry": 1, "Math": 4, "Physics": 3}),
    Group(group_name="Group6", subjects_hours={"Chemistry": 4, "Music": 2, "Physics": 3, "Art": 2, "History": 3, "Math": 4, "Geography": 1, "Literature": 3}),
    Group(group_name="Group7", subjects_hours={"Computer Science": 2, "Programming": 4, "Math": 2,"Art": 2, "Chemistry": 2,  "Biology": 4, "History": 4, "Geography": 4, "Physics": 4}),
    Group(group_name="Group8", subjects_hours={"Math": 4, "Physics": 3, "Chemistry": 4, "History": 3,"Geography": 4, "English": 4, "Programming": 3}),
    Group(group_name="Group9", subjects_hours={"History": 3, "Computer Science": 2, "English": 3, "Programming": 1,  "Art": 2, "Biology": 4, "Literature": 3, "Physics": 3, "Computer Science": 2,  "Math": 2}),
    Group(group_name="Group10", subjects_hours={"Programming": 4, "Biology": 3, "Art": 2, "Geography": 4, "Computer Science": 2, "History": 3, "English": 4, "Math": 4, "Physics": 2})
]


def generate_population():
	population = list()
	for _ in range(n_pop):
		schedule = list()
		for group in groups:
			for day in days:
				for i in range(n_classes):
					cell = dict()
					cell["Day"] = day
					cell["Lesson"] = str(i+1)
					cell["Group"] = group
					cell["Subject"] = random.choice(subjects)
					cell["Teacher"] = get_random_teacher(cell["Subject"])
					schedule.append(cell)
		population.append(schedule)
	return population


def get_random_teacher(subject):
    eligible_teachers = [teacher for teacher in teachers if subject in teacher.subjects]
    if eligible_teachers:
        return random.choice(eligible_teachers)
    else:
        return None


def crossover(p1, p2, r_cross):
	c1, c2 = p1.copy(), p2.copy()
	if rand() < r_cross:
		pt = randint(1, len(p1)-2)
		c1 = p1[:pt] + p2[pt:]
		c2 = p2[:pt] + p1[pt:]
	return [c1, c2]


def selection(pop, scores, k=3):
	selection_ix = randint(len(pop))
	for ix in randint(0, len(pop), k-1):
		if scores[ix] > scores[selection_ix]:
			selection_ix = ix
	return pop[selection_ix]


def mutation(schedule, r_mut):
	for i in range(len(schedule)):
		if rand() < r_mut:
			schedule[i]["Subject"] = random.choice(subjects)
			schedule[i]["Teacher"] = get_random_teacher(schedule[i]["Subject"])


def genetic_algorithm(objective, n_iter, n_pop, r_cross, r_mut):
	pop = generate_population()
	best, best_eval = pop[0], objective(pop[0])
	for gen in range(n_iter):
		print("Gen:", gen)
		scores = [objective(c) for c in pop]
		for i in range(n_pop):
			if scores[i] > best_eval:
				best, best_eval = pop[i], scores[i]
				print("Current best score:", best_eval)
		selected = [selection(pop, scores) for _ in range(n_pop)]
		children = list()
		for i in range(0, n_pop, 2):
			p1, p2 = selected[i], selected[i+1]
			for c in crossover(p1, p2, r_cross):
				mutation(c, r_mut)
				children.append(c)
		pop = children
	return [best, best_eval]


def accurate(x):
	def_groups = defaultdict(dict)
	def_teachers = defaultdict(dict)
	for item in x:
		group = item["Group"]
		subject = item["Subject"]
		teacher = item["Teacher"]
		def_groups[group][subject] = def_groups[group].get(subject, 0) + 1
		if teacher is not None:
			def_teachers[teacher][subject] = def_teachers[teacher].get(subject, 0) + 1
	groups = dict(def_groups)
	teachers = dict(def_teachers)
	return (teachers_accurate(teachers) + groups_accurate(groups)) / 2


def teachers_accurate(teachers):
	score = 0
	for teacher, subjects_hours in teachers.items():
		total_hours = sum(subjects_hours.values())
		if total_hours <= teacher.max_hours:
			score += 1
	return score / len(teachers)


def groups_accurate(groups):
	total_score = 0
	for group, actual_schedule in groups.items():
		planned_schedule = group.subjects_hours
		total_actual = sum(hours for subject, hours in actual_schedule.items() if subject != "None")
		total_planned = sum(hours for hours in planned_schedule.values())
		score = 0
		for subject, planned_hours in planned_schedule.items():
			if subject in actual_schedule:
				actual_hours = actual_schedule[subject]
				score += min(actual_hours, planned_hours)
		total_score += score / max(total_actual, total_planned)
	return total_score / len(groups)


def main():
	best, score = genetic_algorithm(accurate, n_iter, n_pop, r_cross, r_mut)
	print('Done!')
	print("Best score:", score)
	for cell in best:
		print(cell["Day"])
		print(cell["Lesson"])
		print(cell["Group"])
		print(cell["Subject"])
		print(cell["Teacher"])
		time.sleep(1)
	
    
if __name__ == '__main__':
	main()