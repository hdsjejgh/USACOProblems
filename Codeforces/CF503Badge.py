N = int(input())
students = list(map(lambda x:int(x)-1,input().split()))
answers = []
for student,target in enumerate(students):
    t,h = target,students[target]
    while t!=h:
        t=students[t]
        h=students[students[h]]
    t=student
    while t!=h:
        t=students[t]
        h=students[h]
    answers.append(str(t+1))
print(' '.join(answers))