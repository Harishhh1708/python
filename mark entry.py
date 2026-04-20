tamil=int(input("Tamil:"))
english=int(input("English:"))
maths=int(input("Mathematics:"))
science=int(input("Science:"))
social=int(input("social:"))
a=(tamil+english+maths+science+social)
b=(a/5)
if(b>=35):
    print("you are pass")
else:
    print("you are fail")