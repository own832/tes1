
sum1=0
sum2=0
sum3=0



days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
for i in days:
    mood=input(f"Enter your mood for {i}: ")
    if mood =="happy":
        sum1+=1
    elif mood =="sad":
        sum2+=1
    elif mood=="stress":
        sum3+=1
print("""
      the percentage of each mood
      over a week
      """)
sum1=sum1/7
sum2=sum2/7
sum3=sum3/7


print("happy mood over a week",sum1*100)
print("sad mood over a week",sum2*100)
print("stress mood over a week", sum3*100)