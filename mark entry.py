tamil=int(input("TAMIL:"))
english=int(input("ENGLISH:"))
maths=int(input("MATHEMATICS:"))
science=int(input("SCIENCE:"))
social=int(input("social:"))
a=(tamil+english+maths+science+social)
b=(a/5)
if(b>=35):
    print("you are pass")
else:
    print("you are fail")