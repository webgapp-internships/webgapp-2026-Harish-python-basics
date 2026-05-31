mark=[75,22,90,34,67]
def check_grade(mark):
    if mark>=35:
        return "pass"
    else:
        return "fail"

for i in range (len(mark)):
    result=check_grade(mark[i])

    print("studen",i+1,":",result)
