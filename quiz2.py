print("======================================================================")
print("BANO QABIL QUIZ 2")
print("VERSION 5")
print("TOPIC : Variables , Datatypes ,Operators")
print("Total marks = 5")
score = 0

ans = input("Which symbol is used to store data in variable? A) == B) = C) + D) * :")
if ans == "B" or ans == "b":
    score = 1
ans = input("Name = (Ali) define its datatype? A)int B)float C)str D)bool :")
if ans == "C" or ans == "c" :
    score = score + 1
ans = input("True and False datatype? A) int B) float C) str D) bool :")
if ans == "D" or ans == "d" :
    score = score + 1
ans = input (" 9.8 / 2 result? A)4 B)6 C)10 D)16 :")
if ans == "A" or ans == "a" :
    score = score + 1
ans = input("To write name of varible which is true? A)1st name B)first name C)first_name D)first-name :")
if ans == "C" or ans == "c" :
    score = score + 1

print("Score:",score,"/5")
if score == 5 :
    print("Excellent")
if score == 0 :
    print("fail")