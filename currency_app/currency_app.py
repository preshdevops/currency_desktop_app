import requests

key = "87943bbd3ea2d514a2d0902d6d0159dde86047c1"

#FETCH CURENCY LIST
parameters = {"api_key": key, "format": "json"}
url = "https://api.getgeoapi.com/v2/currency/list"
response = requests.get(url, parameters)
data=response.json()
print("Select a currency code ")
for x in data['currencies']:
    #print(x," -- ",data['currencies'][x])
      pass
      
 

parameters = {
"api_key": key,
'from':"EUR",
"to":"GBP",
"amount":10,
"format": "json"}



from tkinter import *
base = Tk()
base.geometry("800x550")
base.title("My Currency converter")

frm1=Frame(base,bg="blue")
frm1.pack(fill=BOTH,expand=True,ipady=10,ipadx=10)


frm_left=Frame(frm1,bg="white")
frm_left.pack(fill=BOTH,expand=True,ipady=10,ipadx=10,
pady=10,padx=10,side=LEFT)




listbox=Listbox(frm_left,font=("Arial",20),fg="blue",height=3) 
listbox.pack()
'''
for x in range(20):
     listbox.insert(END,x)
 '''
for x in data['currencies']:
     #print(x," -- ",data['currencies'][x])
     listdata = f"{x}*** {data['currencies'][x]}"
     listbox.insert(END,listdata)

def Show_Select():
     zee=listbox.curselection()
     print(zee,zee[0])
     zee2=listbox.get(zee[0])
     x=zee2.split("***")
     data=f"From : {x[0]}"
     frm_cur=x[0]
     lbl1.config(text=data)
     parameters['from']=frm_cur
     print(parameters)
     
btn1=Button(frm_left,text="Select From_Cur",bg="blue",
fg="white",font=("Arial",16),
command=Show_Select)
btn1.pack(padx=10,pady=5)



listbox2=Listbox(frm_left,font=("Arial",20),fg="blue",height=3) 
listbox2.pack()
'''
for x in range(20):
     listbox.insert(END,x)
 '''
for y in data['currencies']:
     #print(x," -- ",data['currencies'][x])
     listdata2 = f"{y}*** {data['currencies'][y]}"
     listbox2.insert(END,listdata2)


def Show_Select2():
     zee2=listbox2.curselection()
     print(zee2,zee2[0])
     zed=listbox2.get(zee2[0])
     x=zed.split("***")
     data=f"To : {x[0]}"
     to_cur=x[0]
     lbl2.config(text=data)
     parameters['to']=to_cur
     print(parameters)
     
     
btn2=Button(frm_left,text="Select To_Cur",bg="blue",
fg="white",font=("Arial",16),
command=Show_Select2)
btn2.pack(padx=10,pady=5)     


#SECTION FOR AMOUNT ENTRY
#==============================================
def Show_Select3():   
     zed=ent4.get()  
     data=f"Amount : {zed}"
     lbl3.config(text=data)
     amt=zed
     parameters['amount']=amt
     print(parameters)
     doConvert()
 




def doConvert():
                        
            url = "https://api.getgeoapi.com/v2/currency/convert"
            response = requests.get(url, parameters)
            data=response.json()
            print(data)
           



 
lbl4=Label(frm_left,bg="white",font=("calibri",20),
text="Enter Amount",fg="blue")
lbl4.pack(ipadx=10,ipady=10,padx=20,fill=X,expand=True)

ent4=Entry(frm_left,bg="white",font=("calibri",20),fg="blue")
ent4.pack(ipadx=5,ipady=5,padx=10,fill=X,expand=True)


btn3=Button(frm_left,text="Select Amount",bg="blue",
fg="white",font=("Arial",16),
command=Show_Select3)
btn3.pack(padx=10,pady=5)   

def doConvert():
    url = "https://api.getgeoapi.com/v2/currency/convert"
    response = requests.get(url, parameters)
    data = response.json()
    print(data) # keep this if you still want debug info

    try:
        result = data["rates"][parameters["to"]]["rate_for_amount"]
        rate = data['rates']
        lbl_result.config(text=f"Result: {result}")
        lbl_rate.config(text=f"Rate: {rate}")
        
    except Exception as e:
        lbl_result.config(text="Conversion failed")
        print("Error:", e)


frm_right=Frame(frm1,bg="white")
frm_right.pack(fill=BOTH,expand=True,ipady=10,
ipadx=10,pady=10,padx=10,side=LEFT)
lbl_result = Label(frm_right, bg="white", font=("calibri", 20), 
                   text="Result will appear here", fg="green")
lbl_result.pack(ipadx=10, ipady=10, padx=20, fill=X, expand=True)
lbl_rate = Label(frm_right, bg="white", font=("calibri", 20), 
                   text="Result will appear here", fg="green", wraplength=200, justify="left")
lbl_rate.pack(ipadx=10, ipady=10, padx=20, fill=X, expand=True)


lbl1=Label(frm_right,bg="white",font=("calibri",20),
text="selection",fg="blue")
lbl1.pack(ipadx=10,ipady=10,padx=20,fill=X,expand=True)



lbl2=Label(frm_right,bg="white",font=("calibri",20),
text="selection",fg="blue")
lbl2.pack(ipadx=10,ipady=10,padx=20,fill=X,expand=True)


lbl3=Label(frm_right,bg="white",font=("calibri",20),
text="selection",fg="blue")
lbl3.pack(ipadx=10,ipady=10,padx=20,fill=X,expand=True)

btn_convert = Button(frm_left, text="Convert", bg="green",
                     fg="white", font=("Arial", 16),
                     command=doConvert)
btn_convert.pack(padx=10, pady=5)

base.mainloop()