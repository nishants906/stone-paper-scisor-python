import random
list=["stone","paper","scisor"]
a="y"
print("\t\t\tSTONE PAPER SCISOR")
print("\t\tchoose st=stone,pa=paper,sc=scisor")
while a=="y":
    n=random.randint(0,2)
    b=raw_input("choose ur option :")
    if (b=="st")or(b=="pa")or(b=="sc"):
        print("computer chooses :",list[n])
        
        if b[0]==list[n][0] and b[1]==list[n][1]:
            print("game tie")
        else:
            if(list[n]=="stone") and (b=="pa"):
                print("u win")
            else:
                if (list[n]=="stone") and (b=="sc"):
                    print("u loose")
                else:
                    if(list[n]=="paper") and (b=="st"):
                        print("u loose")
                    else:
                        if(list[n]=="paper") and (b=="pa"):
                            print("u win")
                        else:
                            if(list[n]=="scisor") and (b=="st"):
                                print("u win")
                            else:
                                print("u loose")
    else:
        print("invalid option")
        
    a=raw_input("want to play again(y/n):")
    print("\n")
   
