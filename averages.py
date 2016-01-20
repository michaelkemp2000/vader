# Averages using functions, lists and dicts

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!

def get_average(student):

    homework = 0.10 * average(student["homework"])
    quizzes = 0.30 * average(student["quizzes"])
    tests = 0.60 * average(student["tests"])
    total = homework + quizzes + tests
    return total

def average(numbers):

    total = numbers
    total = sum(total) / len(numbers)
    return float(total)

def get_letter_grade(score):

    if score >= 90:
        return "A"

    elif score >= 80 and score < 90:
        return "B"

    elif score >= 70 and score < 80:
        return "C"

    elif score >= 60 and score < 70:
        return "D"

    else:
        return "F"

def get_class_average(students):

    results = []
    for s in students:
        result = get_average(s)
        results.append(result)
    return average(results)


classmates = [lloyd, alice, tyler]
lessons = ['homework', 'quizzes', 'tests']

score = get_average(lloyd)
print get_letter_grade(score)
results = get_class_average(classmates)
print results

# def average(people, numbers):
    
#    total = 0
#    for p in people:
#        print p['name']
#        for n in numbers:
#            total = sum(p[n])
#            total = float(total) / len(p[n])
#            print "Average %s: %d" % (n, total)
#        print ""
