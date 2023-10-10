from tkinter import *
from movieRecommendationCode import main
from tkinter import messagebox


root = Tk()
root.title('MovieRecommendation')
root.geometry("680x480")
root.configure(background="gray")

def Value():
    try:
        s=my_movie_Enter.get()
        s=main(s)
        my_output = Label(root,text=f'\n{s[0]},\n{s[1]},\n{s[2]},\n{s[3]},\n{s[4]},\n{s[5]}',bg='cyan',width=25,height=15)
        my_output.place(x=200,y=230)
    except Exception as e:
        response = messagebox.showwarning("Waring", "Write Full Movie name")
        if response==0:
            print("Message Pop Up")


my_Label = Label(root,text="Movie Recommendation System",font=("Arial", 25),bg='gray',fg='black',anchor='center',padx=20,pady=20)

my_movie = Label(root,text='Enter Your Movie Name: ',bg='gray',font=('Arial',16),padx=20,pady=20)
my_movie_Enter= Entry(root,width=25,font=('Arial',16))

submit_btn = Button(root,text='Submit',width=10,height=1,command=Value)

button_quit = Button(root,text = "Exit Program",command =root.quit)

my_Label.place(x = 40,y = 30)
my_movie.place(x=60,y=120)
my_movie_Enter.place(x=325,y=140)
submit_btn.place(x=250,y=200)
button_quit.place(x=350,y=200)
root.mainloop()