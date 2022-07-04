def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1,2,3,4,5]))

def mean2(value):
    if type(value) == dict:
        the_mean = sum(value.values())/len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(mean2(student_grades))


student_grades.values()



