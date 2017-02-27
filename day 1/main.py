name = "Bob"
print name

x = 4
print name + str(x)

#this is a comment

grade = 90

#javascript
#if (grade>69) {
#console.log("nice.job") }

if grade>89:
    print "you earned the grade of an A"
elif grade>79:
    print "you earned the grade of an B"
elif grade>69:
    print "you earned the grade of an C"
elif grade>59:
    print "you earned the grade of an D"
else:
    print "Sorry, you failed! :'("


def gradeMsg(g):
    if g>89:
        message = "you earned the grade of an A"
    elif g>79:
        message = "you earned the grade of an B"
    elif g>69:
        message = "you earned the grade of an C"
    elif g>59:
        message = "you earned the grade of an D"
    else:
        message = "Sorry, you failed! :'("
    return message

print gradeMsg(87)


#var dice = Math.floor(Math.random() * 6 + 1)

import random

die = random.randrange(1,7)
print die

#for (var i=0; i<5; i++) { console.log(Math.floor(Math.random() * 10)) }

for i in range(0,5,2):
    print i

name = "Kelsey"
for i in name:
    print i

grades = [7,31,40]
for i in grades:
    print i

print len(grades)

grades.pop()
print grades

grades.pop(0)
print grades

grades.append(70)
print grades



import random

def roll(n, r):
    count = 0
    for i in range(0, r):
        if random.randint(1,6) == n:
            count+=1
    return count
print roll(6,100)

def rolled(r):
    rolls = [0,0,0,0,0,0]
    for i in range(0,r):
        die = random.randint(1,6)
        rolls[die - 1] +=1
        #if die == 1:
           # rolls[0] += 1
    return rolls
print rolled(20)