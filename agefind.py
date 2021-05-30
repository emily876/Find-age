birth= int(input("enter your age or the year of birth"))
if(birth>2021):
    print("you are not born yet")
    exit()

year100 = birth+100
print("you will gonna be 100 yrs old in the year",year100)

i=input("want to know your age in a particular year? \n yes/no")
if(i == "yes"):
    ip= int(input("tell me which year?"))
    print("your age in that year will be",ip-birth,"yrs")
else:
    print("okay fine!!")
