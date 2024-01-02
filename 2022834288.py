import tkinter as tk
import mysql.connector

#perfume calculation
def total():
    # Perfume calculation
        champagnetoast_price = int(champagnetoastEntry.get())*20
        sunsetglow_price = int(sunsetglowEntry.get())*20
        inthestars_price = int(inthestarsEntry.get())*20
        youretheone_price = int(youretheoneEntry.get())*20
        intothenight_price = int(intothenightEntry.get())*20

        total_perfumeprice = champagnetoast_price + sunsetglow_price + inthestars_price + youretheone_price + intothenight_price
        print("Total Perfume Price:", total_perfumeprice)

# Body wash calculation
        athousandwishes_price = int(athousandwishesEntry.get()) * 10
        gingham_price = int(ginghamEntry.get()) * 10
        warmnvanillasugar_price = int(warmvanillasugarEntry.get()) * 10
        strawberrysnowflakes_price = int(strawberrysnowflakesEntry.get()) * 10
        purewonder_price_bodywash = int(purewonderEntry.get()) * 10

        total_bodywashprice = athousandwishes_price + gingham_price + warmnvanillasugar_price + strawberrysnowflakes_price + purewonder_price_bodywash
        print("Total Body Wash Price:", total_bodywashprice)

# Add the calculation for the total of both perfumes and body wash
        total_all_products = total_perfumeprice + total_bodywashprice
        print("Total All Products Price:", total_all_products)

# bill area
        customer_details= f"THANKYOU,DATA INSERTED SUCCESSFULLY!\n\nName:{nameEntry.get()}\nPhone number:{phoneEntry.get()}\nEmail:{emailEntry.get()}"
        bill_text = f"Perfume Total:RM {total_perfumeprice}\nBody Wash Total:RM {total_bodywashprice}\nTotal All Products:RM {total_all_products}"
        textarea.insert(tk.END, customer_details + "\n\n")
        textarea.insert(tk.END, bill_text + "\n\n")

# Establish a connection to the MySQL server
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bbw_shopping"
            )

# Create a cursor object to interact with the database
        cursor = mydb.cursor()

# Inserting data into a table
        sql = "INSERT INTO `customer_details` (Name, Phone_number, Email,Total_perfumeprice,Total_bodywashprice, Total_allproductprice) VALUES(%s,%s,%s,%s,%s,%s)"
        val = (nameEntry.get(),phoneEntry.get(),emailEntry.get(),total_perfumeprice,total_bodywashprice,total_all_products)

        try:
            cursor.execute(sql, val)
            mydb.commit()
            print("Data inserted successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            mydb.rollback()

        cursor.close()
        mydb.close()

#GUI
root= tk.Tk()
root.title ("BBW shopping")
root.geometry ('810x300')

#label
label= tk.Label(root,text='Bath & Body Works Shopping',font=('Georgia Font', 20, 'italic')
                    ,bg='palevioletred',fg='mistyrose',bd=10, relief='groove')
label.pack(ipadx=800) 

#customer details frame
customer_details_frame=tk.LabelFrame(root,text='Customer Details',font=('Times New Roman',10,'bold')
                                     ,bg='mistyrose',fg= 'tomato',bd=5,relief= 'groove')
customer_details_frame.pack(ipadx=800)
#name 
nameLabel=tk.Label(customer_details_frame,text='Name',font=('Times New Roman',10,'bold'),bg='mistyrose'
                   ,fg= 'palevioletred')
nameLabel.grid (row=0,column=0,ipadx=5,ipady=5)
nameEntry=tk.Entry(customer_details_frame,font=('Times New Roman', 10),bd=3)
nameEntry.grid (row=0,column=1,ipadx=20)
#phone number 
phoneLabel=tk.Label(customer_details_frame,text='Phone',font=('Times New Roman',10,'bold'),bg='mistyrose'
                   ,fg= 'palevioletred')
phoneLabel.grid(row=0,column=2,ipadx=5,ipady=5)
phoneEntry=tk.Entry(customer_details_frame,font=('Times New Roman', 10),bd=3)
phoneEntry.grid (row=0,column=3,ipadx=10)
#email
emailLabel=tk.Label(customer_details_frame,text='Email',font=('Times New Roman',10,'bold'),bg='mistyrose'
                   ,fg= 'palevioletred')
emailLabel.grid(row=0,column=4,ipadx=10,ipady=5)
emailEntry=tk.Entry(customer_details_frame,font=('Times New Roman', 10),bd=3)
emailEntry.grid (row=0,column=5,ipadx=30)

#products frame
productsFrame=tk.Frame(root)
productsFrame.pack(pady=3)

#perfumes frame
perfumesframe=tk.LabelFrame(productsFrame,text='Perfumes (RM20/each)',font=('Times New Roman',10,'bold')
                                     ,bg='mistyrose',fg= 'tomato',bd=5,relief= 'groove')
perfumesframe.grid(row=0,column=0)
#champange toast 
champagnetoastLabel=tk.Label(perfumesframe,text='champagne toast',font=('Times New Roman',10,'bold'),bg='mistyrose',
                              fg='palevioletred')
champagnetoastLabel.grid(row=0,column=0)
champagnetoastEntry=tk.Entry(perfumesframe,font=('Times New Roman',10,),width=10,bd=3)
champagnetoastEntry.grid(row=0,column=1,padx=5,pady=5)
champagnetoastEntry.insert(0,0)
#pure wonder
sunsetglowLabel=tk.Label(perfumesframe,text='sunset glow',font=('Times New Roman',10,'bold'),bg='mistyrose',
                              fg='palevioletred')
sunsetglowLabel.grid(row=1,column=0)
sunsetglowEntry=tk.Entry(perfumesframe,font=('Times New Roman',10,),width=10,bd=3)
sunsetglowEntry.grid(row=1,column=1,padx=5,pady=5)
sunsetglowEntry.insert(0,0)
#in the stars
inthestarsLabel=tk.Label(perfumesframe,text='in the stars',font=('Times New Roman',10,'bold'),bg='mistyrose',
                              fg='palevioletred')
inthestarsLabel.grid(row=2,column=0)
inthestarsEntry=tk.Entry(perfumesframe,font=('Times New Roman',10,),width=10,bd=3)
inthestarsEntry.grid(row=2,column=1,padx=5,pady=5)
inthestarsEntry.insert(0,0)
#you're the one
youretheoneLabel=tk.Label(perfumesframe,text='you are the one',font=('Times New Roman',10,'bold'),bg='mistyrose',
                              fg='palevioletred')
youretheoneLabel.grid(row=3,column=0)
youretheoneEntry=tk.Entry(perfumesframe,font=('Times New Roman',10,),width=10,bd=3)
youretheoneEntry.grid(row=3,column=1,padx=5,pady=5)
youretheoneEntry.insert(0,0)
#into the night
intothenightLabel=tk.Label(perfumesframe,text='into the night',font=('Times New Roman',10,'bold'),bg='mistyrose',
                              fg='palevioletred')
intothenightLabel.grid(row=4,column=0)
intothenightEntry=tk.Entry(perfumesframe,font=('Times New Roman',10,),width=10,bd=3)
intothenightEntry.grid(row=4,column=1,padx=5,pady=5)
intothenightEntry.insert(0,0)


#bodywash frame
bodywashframe=tk.LabelFrame(productsFrame,text='Body Wash (RM10/each)',font=('Times New Roman',10,'bold')
                                     ,bg='mistyrose',fg= 'tomato',bd=5,relief= 'groove')
bodywashframe.grid(row=0,column=1)
#a thousand wishes
athousandwishesLabel=tk.Label(bodywashframe,text='a thousand wishes',font=('Times New Roman',10,'bold'),bg='mistyrose',
                              fg='palevioletred')
athousandwishesLabel.grid(row=0,column=0)
athousandwishesEntry=tk.Entry(bodywashframe,font=('Times New Roman',10,),width=10,bd=3)
athousandwishesEntry.grid(row=0,column=1,padx=5,pady=5)
athousandwishesEntry.insert(0,0)
#gingham
ginghamLabel=tk.Label(bodywashframe,text='gingham',font=('Times New Roman',10,'bold'),bg='mistyrose',
                              fg='palevioletred')
ginghamLabel.grid(row=1,column=0)
ginghamEntry=tk.Entry(bodywashframe,font=('Times New Roman',10,),width=10,bd=3)
ginghamEntry.grid(row=1,column=1,padx=5,pady=5)
ginghamEntry.insert(0,0)
#warmn vanilla sugar
warmvanillasugarLabel=tk.Label(bodywashframe,text='warm vanilla sugar',font=('Times New Roman',10,'bold'),bg='mistyrose',
                              fg='palevioletred')
warmvanillasugarLabel.grid(row=2,column=0)
warmvanillasugarEntry=tk.Entry(bodywashframe,font=('Times New Roman',10,),width=10,bd=3)
warmvanillasugarEntry.grid(row=2,column=1,padx=5,pady=5)
warmvanillasugarEntry.insert(0,0)
#strawberry snowflakes
strawberrysnowflakesLabel=tk.Label(bodywashframe,text='strawberry snowflakes',font=('Times New Roman',10,'bold'),bg='mistyrose',
                              fg='palevioletred')
strawberrysnowflakesLabel.grid(row=3,column=0)
strawberrysnowflakesEntry=tk.Entry(bodywashframe,font=('Times New Roman',10,),width=10,bd=3)
strawberrysnowflakesEntry.grid(row=3,column=1,padx=5,pady=5)
strawberrysnowflakesEntry.insert(0,0)
#pure wonder
purewonderLabel=tk.Label(bodywashframe,text='pure wonder',font=('Times New Roman',10,'bold'),bg='mistyrose',
                              fg='palevioletred')
purewonderLabel.grid(row=4,column=0)
purewonderEntry=tk.Entry(bodywashframe,font=('Times New Roman',10,),width=10,bd=3)
purewonderEntry.grid(row=4,column=1,padx=5,pady=5)
purewonderEntry.insert(0,0)

#enter frame
buttonFrame=tk.Frame(productsFrame,bd=8,relief='groove')
buttonFrame.grid(row=0,column=2,padx=5)
enterButton=tk.Button(productsFrame,text='ENTER',font=('Times New Roman',10,'bold'),bd=5,bg='mistyrose'
                   ,fg= 'tomato',padx=10,pady=75,command=total)
enterButton.grid(row=0,column=2)

#billframe
billframe=tk.Frame(productsFrame,bd=8,relief='groove')
billframe.grid(row=0,column=3,ipadx=5,padx=5)

billareaLabel=tk.Label(billframe,text='BILL AREA',font=('Times New Roman',10,'bold'),fg= 'tomato')
billareaLabel.pack() 

scrollbar=tk.Scrollbar(billframe,orient='vertical')
scrollbar.pack(side='right', fill='y')
textarea=tk.Text(billframe,width=36,height=9)
textarea.pack()
scrollbar.config(command=textarea.yview)

root.mainloop()

