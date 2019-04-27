#!/bin/python

Song = { "name":"Kwang Ho Song",
          "assignment" : [92, 96, 84, 90], 
          "test" : [80, 90], 
          "lab" : [89, 78] 
        } 

         

Hanks = { "name":"Tom Hanks", 
         "assignment" : [90, 95, 86, 90], 
         "test" : [95, 90], 
         "lab" : [98, 97] 
       } 

 

Paice = { "name" : "Ian Paice", 
          "assignment" : [77, 82, 83, 79], 
          "test" : [78, 87], 
          "lab" : [80, 80] 
        } 

          

Duck = { "name" : "Trump Duck", 
         "assignment" : [57, 55, 58, 41], 
         "test" : [40, 50], 
         "lab" : [49, 44] 
       } 

         

Cruz = { "name" : "Cruz Tom", 
        "assignment" : [89, 89, 60, 86], 
        "test" : [65, 86], 
        "lab" : [70, 80.6] 
}


def grading(score): 
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else : return "E"

def calculateAverage(students):
    l = len(students)
    i = 0
    while i < l:
        ass = sum(students[i]["assignment"])/4 * 30/100
        tst = sum(students[i]["test"])/2 * 50/100
        lab = sum(students[i]["lab"])/2 * 20/100
        # print(ass, tst, lab)
        students[i]["avg_assignment"] = ass
        students[i]["avg_test"] = tst
        students[i]["avg_lab"] = lab
        
        # students[i]["avg_assignment_grade"] = grading(ass)
        # students[i]["avg_test_grade"] = grading(tst)
        # students[i]["avg_lab_grade"] = grading(lab)

        finalScore = ass + tst + lab
        students[i]["final_score"] = finalScore
        students[i]["final_grade"] = grading(finalScore)

        print("{}:\n\tassignment: {}\n\ttest: {}\n\tlab: {}\n\t최종점수: {}\n\t최종학점: {}".format(students[i]["name"], ass, tst, lab, finalScore, grading(finalScore)))
        i += 1
    # print(students)

def calculateAverageClass(students):
    l = len(students)
    i = 0
    tot = 0
    while i < l:
        tot += students[i]["final_score"]
        i += 1
    
    avg = tot/l
    grade = grading(avg)
    print("{}: {}".format("학급평균", avg))
    print("{}: {}".format("학급학점", grade))

if __name__ == '__main__':
    # print(grading(70))
    print(Song.get("name"))
    students = []
    students.append(Song)
    students.append(Hanks)
    students.append(Paice)
    students.append(Duck)
    students.append(Cruz)
    # print(students)
    calculateAverage(students)
    calculateAverageClass(students)
    # print(students)