#quiz game
#import tkinter
from  tkinter import*
import random
question = ["1. Who developed Python Programming Language ?",
            "2. Which type of Programming does Python support ?",
            "3. Is Python case sensitive when dealing with identifiers ?",
            "4. Which of the following is the correct extension of the Python file ?",
            "5. Is Python code compiled or interpreted ?",
            "6. Which of the following is used to define a block of code in Python language ?",
            #"7  ?",
            #"8 ngnf ag98rr giagiy cp89ycw hsfdpp ?",
            #"9 fgloshg seroi slo8yrg ,fhnfl ?",
           # "10 blvdshoi fghv   hehah rliwaeoiw ?",
]

answers_choice = [
    [" Wick van Rossum"," Rasmus Lerdorf"," Guido van Rossumd)"," Niene Stom",],
    [" object-oriented programming"," structured programming"," functional programming"," all of the mentioned",],
    ["no","yes","machine dependentd", "none of the mentioned",],
    [".python",".pI",".py",".p",],
    [" Python code is only compiled","Python code is only interpreted","both","noan above",],
    [" Capitalized"," lower case"," UPPER CASE","None of the mentioned",],
   

]

answers = [2,3,1,2,1,3]

user_answer = []
indexes = []
def gen():
    global indexes
    while(len(indexes)<5):
        x=random.randint(0,5)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    #print(indexes)

def showresult(score):
    labQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    lableresult = Label(root,font="lucida 30 bold",fg="blue")
    lableresult.pack(pady=50)
    if score >= 20:
        lableresult.configure(text="You are Excellent !!")
    elif(score >=10 | score < 20 ):
        lableresult.configure(text="You can Better !!")
    else:
        lableresult.configure(text="You Should Work Hard !!")




def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)



ques = 1
def selected():
    global radiovar,user_answer
    global labQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        labQuestion.config(text=question[indexes[ques]])
        r1["text"] = answers_choice[indexes[ques]][0]
        r2["text"] = answers_choice[indexes[ques]][1]
        r3["text"] = answers_choice[indexes[ques]][2]
        r4["text"] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        print(indexes)
        print(user_answer)
        calc()



def startquiz():
    global labQuestion,r1,r2,r3,r4
    labQuestion=Label(root,text=question[indexes[0]],bg="sky blue",fg="black",font=2,wraplength=400,justify="center",width=500)
    labQuestion.pack(pady=15)
    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)


    r1=Radiobutton(root,text=answers_choice[indexes[0]][0],font=5,value=0,variable=radiovar,bg="dark green",fg="white",command=selected)
    r1.pack(pady=8)

    r2=Radiobutton(root,text=answers_choice[indexes[0]][1],font=5,value=1,variable=radiovar,bg="dark green",fg="white",command=selected)
    r2.pack(pady=14)

    r3=Radiobutton(root,text=answers_choice[indexes[0]][2],font=5,value=2,variable=radiovar,bg="dark green",fg="white",command=selected)
    r3.pack(pady=15)

    r4=Radiobutton(root,text=answers_choice[indexes[0]][3],font=5,value=3,variable=radiovar,bg="dark green",fg="white",command=selected)
    r4.pack(pady=17)



def pressed():
    lable1.destroy()
    button1.destroy()
    lable2.destroy()
    lable3.destroy()
    gen()
    startquiz()



root = Tk()
root.geometry("500x400")
root.title("QUIZ GAME")
root.resizable(0,0)
lable1=Label(root,text = "QUIZ GAME",fg="white",font="lucida 25 bold",bg="black")
lable1.pack(pady=20)
button1=Button(root,text="START",bg="green",fg="black",font="lucida 15 bold",command=pressed)
button1.pack(pady=22)
lable2=Label(root,text="Read The Rules And\nClick Start Once You Ready",fg="black",font=2)
lable2.pack()
lable3=Label(root,text="This quiz contains 5 question you will\nGet 20 seconds to solve a question\nOnce you select a radio button that will be a final\nChoice hence think before you select",bg="black",fg="yellow",font=1)
lable3.pack(pady=25)
root.mainloop()
