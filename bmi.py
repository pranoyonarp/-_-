#This is a BODY MASS INDEX(BMI) calculator
def bm (a):
      while a!=0:
        print("enter your weight in kilogram")
        weight=int(input())
        print("enter your height in meter")
        height=float(input())
        bmi=weight//(height*height)
        if bmi<18.5:
         print("your bmi is =",bmi,"you are underweight")
        elif bmi>=18.5 and bmi<=24.9:
         print("your bmi is =",bmi,"normal weight")
        elif bmi>=25.0 and bmi<=29.9:
         print("your bmi is =",bmi,"overweight")
        print("press 1 for continue and 0 for exit")
        a=int(input())
        bm(a)
bm(1)
print("do exercise")
