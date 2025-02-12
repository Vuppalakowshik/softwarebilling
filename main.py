from tkinter import *

root=Tk()
root.title('Reatail billing system')
root.geometry('1270x685')
root.iconbitmap('billingicon.ico')
headingLabel=Label(root,text='Reatail Billing System',font=('times new roman',30,'bold')
,bg='gray20',fg='gold', bd=12,relief=GROOVE)
headingLabel.pack(fill=X)
customer_details_frame=LabelFrame(root,text='Customer details',font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=GROOVE,bg='gray20')

customer_details_frame.pack(fill=X,pady=10)
nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray20'
                ,fg='white')
nameLabel.grid(row=0,column=0,padx=20,pady=2)
nameEntry=Entry(customer_details_frame,font=('arial',15),bd=8,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='gray20'
                ,fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=8,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='gray20'
                ,fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=8,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7 ,width=10)
searchButton.grid(row=0,column=6,padx=20,pady=8)


productsFrame=Frame(root)
productsFrame.pack(pady=10)

cosmeticFrame=LabelFrame(productsFrame,text='Cosmotics' ,font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmeticFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticFrame,text='bathsoap',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
bathsoapLabel.grid(row=0,column=0 ,pady=9,padx=10,sticky='w')
bathsoapEntry=Entry(cosmeticFrame, font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)

facecreamLabel=Label(cosmeticFrame,text='Facecream',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
facecreamLabel.grid(row=1,column=0 ,pady=9,padx=10,sticky='w')
facecreamEntry=Entry(cosmeticFrame, font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)

facewashLabel=Label(cosmeticFrame,text='Facewash',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
facewashLabel.grid(row=2,column=0 ,pady=9,padx=10,sticky='w')
facewashEntry=Entry(cosmeticFrame, font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)

hairsprayLabel=Label(cosmeticFrame,text='Hairspray',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
hairsprayLabel.grid(row=3,column=0 ,pady=9,padx=10,sticky='w')
hairsprayEntry=Entry(cosmeticFrame, font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)


hairgelLabel=Label(cosmeticFrame,text='Hairgel',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
hairgelLabel.grid(row=4,column=0 ,pady=9,padx=10,sticky='w')
hairgelEntry=Entry(cosmeticFrame, font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)


bodylotionLabel=Label(cosmeticFrame,text='bodylotion',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
bodylotionLabel.grid(row=5,column=0 ,pady=9,padx=10,sticky='w')
bodylotionEntry=Entry(cosmeticFrame, font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)

groceryFrame=LabelFrame(productsFrame,text='Grocery' ,font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1)

RiceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
RiceLabel.grid(row=0,column=0 ,pady=9,padx=10,sticky='w')
RiceEntry=Entry(groceryFrame, font=('times new roman',15,'bold'),width=10,bd=5)
RiceEntry.grid(row=0,column=1,pady=9,padx=10)

oilLabel=Label(groceryFrame,text='OIL',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
oilLabel.grid(row=1,column=0 ,pady=9,padx=10,sticky='w')
oilEntry=Entry(groceryFrame, font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)

daalLabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
daalLabel.grid(row=2,column=0 ,pady=9,padx=10,sticky='w')
daalEntry=Entry(groceryFrame, font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10)

WheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
WheatLabel.grid(row=3,column=0 ,pady=9,padx=10,sticky='w')
WheatEntry=Entry(groceryFrame, font=('times new roman',15,'bold'),width=10,bd=5)
WheatEntry.grid(row=3,column=1,pady=9,padx=10)

SugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
SugarLabel.grid(row=4,column=0 ,pady=9,padx=10,sticky='w')
SugarEntry=Entry(groceryFrame, font=('times new roman',15,'bold'),width=10,bd=5)
SugarEntry.grid(row=4,column=1,pady=9,padx=10)


TeaLabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
TeaLabel.grid(row=5,column=0 ,pady=9,padx=10,sticky='w')
TeaEntry=Entry(groceryFrame, font=('times new roman',15,'bold'),width=10,bd=5)
TeaEntry.grid(row=5,column=1,pady=9,padx=10)




drinksFrame=LabelFrame(productsFrame,text='Cold drinks' ,font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=GROOVE,bg='gray20')
drinksFrame.grid(row=0,column=2)

MaazaLabel=Label(drinksFrame,text='Maaza',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
MaazaLabel.grid(row=0,column=0 ,pady=9,padx=10,sticky='w')
MaazaEntry=Entry(drinksFrame, font=('times new roman',15,'bold'),width=10,bd=5)
MaazaEntry.grid(row=0,column=1,pady=9,padx=10)

pepsiLabel=Label(drinksFrame,text='Pepsi',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
pepsiLabel.grid(row=1,column=0 ,pady=9,padx=10,sticky='w')
pepsiEntry=Entry(drinksFrame, font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)

spriteLabel=Label(drinksFrame,text='Sprite',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
spriteLabel.grid(row=2,column=0 ,pady=9,padx=10,sticky='w')
spriteEntry=Entry(drinksFrame, font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)

pepsiLabel=Label(drinksFrame,text='Pepsi',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
pepsiLabel.grid(row=1,column=0 ,pady=9,padx=10,sticky='w')
pepsiEntry=Entry(drinksFrame, font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)

root.mainloop()