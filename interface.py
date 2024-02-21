import numpy 
import pandas as pd
dataframe=pd.read_csv('car_data.csv')
x=dataframe.iloc[:,[1,3,4,6]].values
y=dataframe.iloc[:,2].values
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
x[:,2]=le.fit_transform(x[:,2])
x[:,3]=le.fit_transform(x[:,3])
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.005,random_state=0)
from sklearn.ensemble import RandomForestRegressor
reg=RandomForestRegressor(n_estimators=300,random_state=0)
reg.fit(xtrain,ytrain)
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def fun():
    pd=[e1.get(),e2.get(),c1.get(),c2.get()]
    if '' in pd:
        messagebox.showerror('warning','please enter all the values')
    else:
        pd[2]=le.fit_transform([pd[2]])[0]
        pd[3]=le.fit_transform([pd[3]])[0]
        res=reg.predict([pd])
        l=Label(frame,anchor='center',text='Predicted Price: '+str(int(res[0])),font=('Verdana',13,'italic'),width=25,bg='#272a32',foreground='white').place(x=160,y=480)
frame=Tk()
frame.title('Car Price Predictor')
frame.geometry('600x700+500+60')
bgm=PhotoImage(file='car.png')
bgl=Label(frame,image=bgm)
bgl.place(relheight=1,relwidth=1)
l=Label(frame,text='Car Price Predictor',font=('Times',25,'italic'),bg='#71bde2').place(x=170,y=23)
l1=Label(frame,text='Enter the Purchase Year: ',font=('Verdana',12,'italic'),bg='#8acbec')
l1.place(x=10,y=100)
l2=Label(frame,text='Enter the Distance Driven(in kms): ',font=('Verdana',12,'italic'),bg='#76c0e6')
l2.place(x=10,y=170)
l3=Label(frame,text='Enter the Fuel Type: ',font=('Verdana',12,'italic'),bg='#7acced')
l3.place(x=10,y=240)
l4=Label(frame,text='Enter the Transmission Type: ',font=('Verdana',12,'italic'),bg='#76c0e6')
l4.place(x=10,y=310)
e1=Entry(frame,font=('Verdana',12,'italic'),width=25)
e1.place(x=315,y=100)
e2=Entry(frame,font=('Verdana',12,'italic'),width=25)
e2.place(x=315,y=170)
c1=ttk.Combobox(frame,font=('Verdana',12,'italic'),width=23)
c1['values']=('Diesel','Petrol','CNG','LPG','Electric')
c2=ttk.Combobox(frame,font=('Verdana',12,'italic'),width=23)
c2['values']=('Manual','Automatic')
c1.place(x=315,y=240)
c2.place(x=315,y=310)
b=Button(frame,text='Predict',font=('Verdana',12,'italic'),width=20,bg='#272a32',foreground='white',command=fun)
b.place(x=200,y=400)
frame.pack_propagate(False)
frame.mainloop()

