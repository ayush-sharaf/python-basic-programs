q=["The International Literacy Day is observed on","The language of Lakshadweep. a Union Territory of India, is","In which group of places the Kumbha Mela is held every twelve years?","Bahubali festival is related to","Which day is observed as the World Standards  Day?"]
a=["Sep 8","Nov 28","May 2","Sep 22","Tamil","Hindi","Malayalam","Telugu","Ujjain. Purl; Prayag. Haridwar","Prayag. Haridwar, Ujjain,. Nasik","Rameshwaram. Purl, Badrinath. Dwarika","Chittakoot, Ujjain, Prayag,'Haridwar","Islam","Hinduism","Buddhism","Jainism","June 26","Oct 14","Nov 15","Dec 2"]
print("Welcome to KBC!!\n Give correct answers to win cash prizes.\nfor each question you will be offered a higher amount\n if any question is wrong then you will disqualified from the competiotion")
for i in range (0,5):
    print("Your ",i+1,"th question is on the screen. \n",q[i])
    print("your options are :\n")
    if i==0:
        print(a[0:4])
        print("You will win 5000 for this qustion")
        c = int(input("Enter your choice:"))
        if c==1:
            print("Correct answer !!!")
            amount=5000
            continue
        else:
            print("Wrong answer!!!")
            break
    if i == 1:
        print(a[4:9])
        print("You will win 10000 for this qustion")
        c = int(input("Enter your choice:"))
        if c == 3:
            print("Correct answer !!!")
            amount=15000
            continue
        else:
            print("Wrong answer!!!")
            break
    if i == 2:
        print(a[9:13])
        print("You will win 15000 for this qustion")
        c = int(input("Enter your choice:"))
        if c == 2:
            print("Correct answer !!!")
            amount=30000
            continue
        else:
            print("Wrong answer!!!")
            break
    if i == 3:
        print(a[13:17])
        print("You will win 20000 for this qustion")
        c = int(input("Enter your choice:"))
        if c == 4:
            print("Correct answer !!!")
            amount=50000
            continue
        else:
            print("Wrong answer!!!")
            break
    if i == 4:
        print(a[17:21])
        print("You will win 25000 for this qustion")
        c = int(input("Enter your choice:"))
        if c == 2:
            print("Correct answer !!!")
            amount = 75000
            continue
        else:
            print("Wrong answer!!!")
            break
print("You won Rs.",amount)




