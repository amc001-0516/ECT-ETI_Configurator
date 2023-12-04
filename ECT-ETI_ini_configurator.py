#from json.tool import main
import shutil
from sys import path
from tkinter import *
import tkinter
from fileinput import filename
#from inspect import CO_ITERABLE_COROUTINE
import os
from shutil import copyfile
#from sre_constants import CATEGORY_UNI_NOT_LINEBREAK
from tkinter import filedialog
from datetime import datetime
root = Tk()
root.title ('CTI_ETI ini file Generator')

root.geometry("550x800")
#root.config(bg='#0f4b6e')
root.config(bg="#F8F8F8")
p1 = PhotoImage(file = 'moto_ico2.png')

root.iconphoto(False, p1)

var = StringVar()
#label = Label( root, textvariable=var, relief=RIDGE, font=("Helvetia",21), bg='#116562', fg="yellow", activebackground ="#4a7abc", activeforeground="white",)
label = Label( root, textvariable=var, relief=RIDGE, font=("Helvetia",21), bg='#E0E0EE', fg="black", activebackground ="#4a7abc", activeforeground="white",)
var.set("CTI_ETI INI FILE GENERATOR")
label.place(x=65,y=25)
sel = StringVar()
sel.set("ECT or ETI ")
drop = OptionMenu(root, sel, "ECT","ETI")
drop.place(x=350,y=200)

ctieti2 = Label( root, text="ETI OR ECT SELECTION", relief=GROOVE, font=("Arial",14),fg= "black")
ctieti2.place(x=100,y=200)

sub = Button(root, text="SUBMIT",relief=RAISED,font=("Arial",18), bg='#E0E0EE', fg="black",cursor="hand2",
activebackground ="#4a7abc", activeforeground="white",
command = lambda:[submit()])
sub.place(x=220,y=700)

def submit():
    global sel2
    sel2=sel.get()
#    global sel2
    
    if str(sel2)=="ECT":
    
        quit_window()
        ect_script()
    else:
    
        quit_window()
        eti_script()
root.destroy
def quit_window():
    root.destroy()

print(str(sel.get()))

def ect_script():

    main = Tk()
    main.title ('ECT ini file Generator')

    main.geometry("550x900")
    main.config(bg='#F8F8F8')
    p1 = PhotoImage(file = 'moto_ico2.png')
    bg= PhotoImage (file = "canvas_bg3.png")
    #main.geometry("550x1000")
    #bg= PhotoImage (file = "bg7.png")

    label1 = Label(main, image=bg)
    label1.place(x=0,y=0)



    main.iconphoto(False, p1)
    var = StringVar()
    label = Label( main, textvariable=var, relief=RIDGE, font=("Helvetia",18), bg='#E0E0EE', fg="black", activebackground ="#4a7abc", activeforeground="white",)
    var.set("ECT INI FILE GENERATOR")
    label.place(x=125,y=5)
    zone = StringVar()
    zone.set("Zone ID")
    drop = OptionMenu(main, zone, "1","2","3","4","5","6","7")
    drop.place(x=290,y=60)

    def show():
        myLabel = label(main, text=zone.get()).pack()

    def gotoeti():
        print("ETI")

    #def ecteti():

        #if toggle_button.config('text')[-1] == 'ECT':
        #    toggle_button.config(text='ETI',relief=RIDGE,font=("Arial",12),bg='yellow', fg="blue",command=gotoeti)
        #    nmdsel["state"] = "disabled"
        #else:
        #    toggle_button.config(text='ECT',relief=RIDGE,font=("Arial",12),bg='blue', fg="black")
        #    nmdsel["state"] = "normal"
    #toggle_button = Button(text="ECT", width=10,relief=RIDGE,font=("Arial",12),bg='blue', 
    #fg="black")
    #toggle_button.place(x=200,y=55)

    ctieti = Label( main, text="Zone Selection                    ", relief=GROOVE, font=("Arial",12), fg="black")
    ctieti.place(x=50,y=60)

    site = StringVar()
    site.set("Site ID")
    nmdsites = [i for i in range(191)]
    drop = OptionMenu(main, site, *nmdsites)
    drop.place(x=290,y=110)
    nmdsel = Label( main, text="NMD Site selection             ", relief=GROOVE, font=("Arial",12), fg="black" )
    nmdsel.place(x=50,y=110)
    #Timezone selection
    tz = StringVar()
    tz.set("Time Zone")
    mgipid = StringVar()
    mgipid.set("Hub ID")
    drop = OptionMenu(main, tz, "CST","EST","PACIFIC","MOUNTAIN","ALASKA","HAWAII","OTHER")
    drop.place(x=290,y=265)

    #HUB TYPE selection
    '''hub = StringVar()
    hub.set("  TYPE")
    drop = OptionMenu(main, hub, "  Analog","  Digital T1","  DIGITAL E1","  DIGITAL ISDN")
    drop.place(x=200,y=300)'''
    drop = OptionMenu(main, mgipid, "1","2")
    drop.place(x=290,y=210)

    mgip = Label( main, text="Media Gateway IP address", relief=GROOVE, font=("Arial",12), fg="black")
    mgip.place(x=50,y=160)

    mgipidsel = Label( main, text="Media Gateway (Hub) ID    ", relief=GROOVE, font=("Arial",12), fg="black")
    mgipidsel.place(x=50,y=215)

    mgtwy_ip = Entry (main)
    mgtwy_ip.place(x=290,y=160)



    def Line1_enable():
        if pn1["state"] == "normal":
            pn1["state"] = "disabled"
            phn1["state"] = "disabled"
            pn1e["text"] = "enable"
            pn1e["fg"] = "blue"
        else:
            pn1["state"] = "normal"
            phn1["state"] = "normal"
            pn1e["text"] = "disable"
            pn1e["fg"] = "black"
    def Line2_enable():
        if pn2["state"] == "normal":
            pn2["state"] = "disabled"
            phn2["state"] = "disabled"
            pn2e["text"] = "enable"
            pn2e["fg"] = "blue"
        else:
            pn2["state"] = "normal"
            phn2["state"] = "normal"
            pn2e["text"] = "disable"
            pn2e["fg"] = "black"
    def Line3_enable():
        if pn3["state"] == "normal":
            pn3["state"] = "disabled"
            phn3["state"] = "disabled"
            pn3e["text"] = "enable"
            pn3e["fg"] = "blue"
        else:
            pn3["state"] = "normal"
            phn3["state"] = "normal"
            pn3e["text"] = "disable"
            pn3e["fg"] = "black"
    def Line4_enable():
        if pn4["state"] == "normal":
            pn4["state"] = "disabled"
            phn4["state"] = "disabled"
            pn4e["text"] = "enable"
            pn4e["fg"] = "blue"
        else:
            pn4["state"] = "normal"
            phn4["state"] = "normal"
            pn4e["text"] = "disable"
            pn4e["fg"] = "black"
    def Line5_enable():
        if pn5["state"] == "normal":
            pn5["state"] = "disabled"
            phn5["state"] = "disabled"
            pn5e["text"] = "enable"
            pn5e["fg"] = "blue"
        else:
            pn5["state"] = "normal"
            phn5["state"] = "normal"
            pn5e["text"] = "disable"            
            pn5e["fg"] = "black"
    def Line6_enable():
        if pn6["state"] == "normal":
            pn6["state"] = "disabled"
            phn6["state"] = "disabled"
            pn6e["text"] = "enable"
            pn6e["fg"] = "blue"

        else:
            pn6["state"] = "normal"
            phn6["state"] = "normal"
            pn6e["text"] = "disable"
            pn6e["fg"] = "black"

    phn1 = Entry (main,state="disabled")
    phn1.place(x=290,y=450)

    phn2 = Entry (main,state="disabled")
    phn2.place(x=290,y=480)

    phn3 = Entry (main,state="disabled")
    phn3.place(x=290,y=510)
    
    phn4 = Entry (main,state="disabled")
    phn4.place(x=290,y=540)

    phn5 = Entry (main,state="disabled")
    phn5.place(x=290,y=570)
    
    phn6 = Entry (main,state="disabled")
    phn6.place(x=290,y=600)

    pn = Label( main, text="Enter phone numbers (optional) - Analog Gateways only", relief=RIDGE, font=("Arial",12), fg="black",state="normal")
    pn.place(x=50,y=410)

    pn1 = Label( main, text="Line 1 phone number", relief=RAISED, font=("Arial",10), fg="blue",state="disabled")
    pn1.place(x=150,y=450)

    pn2 = Label( main, text="Line 2 phone number", relief=RAISED, font=("Arial",10), fg="blue",state="disabled")
    pn2.place(x=150,y=480)

    pn3 = Label( main, text="Line 3 phone number", relief=RAISED, font=("Arial",10), fg="blue",state="disabled")
    pn3.place(x=150,y=510)

    pn4 = Label( main, text="Line 4 phone number", relief=RAISED, font=("Arial",10), fg="blue",state="disabled")
    pn4.place(x=150,y=540)

    pn5 = Label( main, text="Line 5 phone number", relief=RAISED, font=("Arial",10), fg="blue",state="disabled")
    pn5.place(x=150,y=570)

    pn6 = Label( main, text="Line 6 phone number", relief=RAISED, font=("Arial",10), fg="blue",state="disabled")
    pn6.place(x=150,y=600)

    pn1e = Button( main, text="enable", relief=RAISED, font=("Arial",10), fg="blue",state="normal", cursor="hand2", command=Line1_enable)
    pn1e.place(x=50,y=450)

    pn2e = Button( main, text="enable", relief=RAISED, font=("Arial",10), fg="blue",state="normal", cursor="hand2",command=Line2_enable)
    pn2e.place(x=50,y=480)

    pn3e = Button( main, text="enable", relief=RAISED, font=("Arial",10), fg="blue",state="normal", cursor="hand2",command=Line3_enable)
    pn3e.place(x=50,y=510)

    pn4e = Button( main, text="enable", relief=RAISED, font=("Arial",10), fg="blue",state="normal", cursor="hand2",command=Line4_enable)
    pn4e.place(x=50,y=540)

    pn5e = Button( main, text="enable", relief=RAISED, font=("Arial",10), fg="blue",state="normal", cursor="hand2",command=Line5_enable)
    pn5e.place(x=50,y=570)

    pn6e = Button( main, text="enable", relief=RAISED, font=("Arial",10), fg="blue",state="normal", cursor="hand2",command=Line6_enable)
    pn6e.place(x=50,y=600)

    cid = IntVar()
    cb=Checkbutton(main, text="Use same phone numbers for caller ID", variable=cid)
    cb.place(x=50, y=640)

#    def switch():
#        if pn["state"] == "normal":
#            pn["state"] = "disabled"
#            pn1["state"] = "disabled"
##            pn2["state"] = "disabled"
#           pn3["state"] = "disabled"
#            pn4["state"] = "disabled"
#            pn5["state"] = "disabled"
#            pn6["state"] = "disabled"
#            pn1e["state"] = "disabled"
#            pn2e["state"] = "disabled"
#            pn3e["state"] = "disabled"
#            pn4e["state"] = "disabled"
#            pn5e["state"] = "disabled"
#            pn6e["state"] = "disabled"
#            phn1["state"] = "disabled"
#            phn2["state"] = "disabled"
#            phn3["state"] = "disabled"
#            phn4["state"] = "disabled"
#            phn5["state"] = "disabled"
#            phn6["state"] = "disabled"
#            b1["text"] = "Enable all phone numbers"
#        else:
#            pn["state"] = "normal"
#            pn1["state"] = "normal"
#            pn2["state"] = "normal"
#            pn3["state"] = "normal"
#            pn4["state"] = "normal"
#            pn5["state"] = "normal"
#            pn6["state"] = "normal"
#            pn1e["state"] = "normal"
#            pn2e["state"] = "normal"
#            pn3e["state"] = "normal"
#            pn4e["state"] = "normal"
#            pn5e["state"] = "normal"
#            pn6e["state"] = "normal"
#            phn1["state"] = "normal"
#            phn2["state"] = "normal"
#            phn3["state"] = "normal"
#            phn4["state"] = "normal"
#            phn5["state"] = "normal"
#            phn6["state"] = "normal"

#            b1["text"] = "Disable all phone numbers"

#    agree=IntVar()
#    b1= Button(text="Enable phone numbers", command=switch)
#    b1.place(x=50, y=420)
    
    tzsel = Label( main, text="Time Zone Selection           ", relief=GROOVE, font=("Arial",12), fg="black")
    tzsel.place(x=50,y=265)

    def browseFiles():
        global filename
        filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("ini files",
                                                            "*.ini*"),
                                                        ("all files",
                                                            "*.*")))


        label_file_explorer.configure(text="File selected: "+filename)
        print(filename)

    label_file_explorer = Label(main,
                                text = "Template path =",

                                fg = "black")
    label_file_explorer.place(x=50,y=360)
    button_explore = Button(main,
                            text = "Import ini Template            ",
                            relief=RAISED,
                            font="Arial",
                            cursor="hand2",
                            fg="black",
                            command = browseFiles)
    button_explore.place(x=50,y=310)
    print(filename)
    path = str(filename)
    print ("path=", path)

    def submit():
        global tz2
        global nmd
        global ictmg_p
        global zo
        global hub2
        global path
        global ctmgid
        global phone1
        global phone2
        global phone3
        global phone4
        global phone5
        global phone6
        global callid
        ictmg_p=mgtwy_ip.get()
        nmd=site.get()
        zo=zone.get()
        tz2=tz.get()
        ctmgid=mgipid.get()
        hid=mgipid.get()
        phone1=phn1.get()
        phone2=phn2.get()
        phone3=phn3.get()
        phone4=phn4.get()
        phone5=phn5.get()
        phone6=phn6.get()
        callid=cid.get()


    def ip_dis():
        mgtwy_ip["state"] = "disabled"
        phn1["state"] = "disabled"
        phn2["state"] = "disabled"
        phn3["state"] = "disabled"
        phn4["state"] = "disabled"
        phn5["state"] = "disabled"
        phn6["state"] = "disabled"

    def capt():
        global ip
        z = zone.get()
        s = site.get()
        tiz = tz.get()
        ip = mgtwy_ip.get()
        hid=mgipid.get()
        disp_data.insert(0,f'Zone:{z}\n  Site:{s} \n Time zone:{tiz} \n Media Gateway Hub ip = {ip} \n Hub ID = {hid}')

    disp_data = Entry(
        main,
        width=65,
        font=('Arial', 10)
        )
    disp_data.place(x=50,y=740)

    def data_disp():
        z = zone.get()
        s = site.get()
        tiz = tz.get()
        ip = mgtwy_ip.get()
        hid=mgipid.get()
        phone1=phn1.get()
        phone2=phn2.get()
        phone3=phn3.get()
        phone4=phn4.get()
        phone5=phn5.get()
        phone6=phn6.get()
        print(phone1)
        print(phone2)
        print(phone3)
        print(phone4)
        print(phone5)
        print(phone6)
        print(callid)


        tkinter.messagebox.showinfo("Collected Parameters for config file", f' Zone ID: {z}\n Site ID: {s} \n Time Zone: {tiz} \n Media Gateway Hub ip = {ip} \n Hub ID = {hid} \n Phone numbers: \n {phone1} \n {phone2} \n {phone3} \n {phone4} \n {phone5} \n {phone6}\n \n Proceed to GENERATE ini FILE' )

    myButton7 = Button(main, text="Load and validate values",relief=RAISED,font=("Arial",16), bg='#E0E0EE', fg="black",cursor="hand2",
    activebackground ="#4a7abc", activeforeground="white",
    command = lambda:[submit(), capt(), ip_dis(), data_disp()])
    myButton7.place(x=50,y=690)
    myButton8 = Button(main, text="GENERATE ini FILE",relief=RAISED,font=("Arial",14),bg='#E0E0EE', fg="black",cursor="hand2",
    activebackground ="#4a7abc", activeforeground="white", command = lambda:[main.destroy, ect_gen_conf()])
    myButton8.place(x=50,y=790)

    myButton9 = Button(main, text="EXIT",relief=RAISED,font=("Arial",14),bg='#E0E0EE', fg="black",cursor="hand2",
    command = main.quit)
    myButton9.place(x=50,y=840)

    def instructions():
        tkinter.messagebox.showinfo("Script Generator steps", "ECT-ETI ini File Generator\n\n\n1. Select ECT or ETI depending on your deployment\n2. Select Astro Zone\n3. Select NMD Site (ECT only)\n4. Enter Media Gateway (Hub) IP address (see Ip Plan)\n5. Import Template from local drive\n6. LOAD VALUES and Validate\n7. Verify Values\n8. Generate file and exit\n\n\nCheck READ ME FIRST file for more detail")
        return ("done amc026")
    def sup():
        tkinter.messagebox.showinfo("About Script Generator   VERSION 1.05.01", "Support email: amc026@motorolasolutions.com")

    menubar = Menu(main)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=main.quit)
    

    helpmenu = Menu(menubar, tearoff=0)

    helpmenu.add_command(label="Help with Script", command=instructions)
    helpmenu.add_command(label="About...", command=sup)
    helpmenu.add_separator()
    menubar.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="Exit Script Generator", command=main.quit)
    support = Menu(menubar, tearoff=0)
    support.add_command(label="amc026", command="instructions")
    main.config(menu=menubar)
    
    main.mainloop()

def ect_gen_conf():
    from mal_it import mal

    item=int(nmd)
    nmdv= ((format(item, "03d")))
    nmdv2= ((format(item, "02d")))
    mgn = "z00{}nmd{}ctmg01".format(zo,nmdv)
    nec_ip = "z0{}nmd{}tg1.nmd{}.zone{}".format(zo,nmdv,item,zo)
    tg="z00{}nmd{}tg0{}".format(zo,nmdv,ctmgid)
    hid2=["ctmg0",ctmgid]
    f=""
    id=f.join(hid2)

    mgn2 = "z00{}nmd{}ctmg0{}".format(zo,nmdv,ctmgid)
    print("name =", mgn2)

    z=int(zo)
    if int(z)>7:
        print ("Astro zones valid values 1-7 please try again")
    zn = "zone{}".format(zo)

    a=str(233)
    s="."
    b=str(0)
    l_pdns = ["10",zo,a,"163"]
    l_sdns = ["10",b,b,"226"]
    Pdns=s.join(l_pdns)
    sdns=s.join(l_sdns)
    ra = ["10",zo,"233","166"]
    rad=s.join(ra)
    l_Pntp = ["10",zo,a,"89"]
    l_sntp = ["10",zo,a,"90"]
    pntp=s.join(l_Pntp)
    sntp=s.join(l_sntp)
    l_sysl = ["10",zo,a,"249"]
    l_med_gty = ["10",zo,nmd,"269"]
    l_gtwy = ["10",zo,nmd,"254"]
    l_telphy = ["10",zo,nmd,"250"]



    sysl=s.join(l_sysl)
    med_gty=s.join(l_med_gty)
    gtwy=s.join(l_gtwy)
    telphy=s.join(l_telphy)



    if tz2 == "CST":
        utcoff=(-21600)
    elif tz2 == "PACIFIC":
        utcoff=(-28800)
    elif tz2 == "MOUNTAIN":
        utcoff=(-25200)
    elif tz2 == "EST":
        utcoff=(-18000)
    elif tz2 == "ALASKA":
        utcoff=(-32400)
    elif tz2 == "HAWAII":
        utcoff=(-36000)
    else: utcoff=(-32400)

    utc2=str(utcoff)

    alist=[mgn]
    alist.append(pntp)
    alist.append(sntp)
    alist.append(ictmg_p)
    alist.append(telphy)
    alist.append(gtwy)
    alist.append(Pdns)
    alist.append(sysl)
    alist.append(mgn)
    alist.append(zn)
    alist.append(nec_ip)
    alist.append(nmd)
    alist.append(utc2)
    alist.append(nec_ip)
    alist.append(nec_ip)
    alist.append(nec_ip)
    alist.append(nec_ip)
    alist.append(rad)
    alist.append(sdns)
    alist.append(id)
    alist.append(phone1)
    alist.append(phone2)
    alist.append(phone3)
    alist.append(phone4)
    alist.append(phone5)
    alist.append(phone6)


    from fileinput import FileInput
    bien = ["Pdns","pntp","sntp","ictmg_p","telphy","gtwy","Pdns","sysl","mgn","zn","nmd","nec_ip","utc2","nec_ip","mgn"]

    print ("alist =", alist)
    alista = [i for i in alist if i]
    print ("new alist=",alista)
    
    ini_file = filename
    new_file2= ini_file + ".backup.ini"
    #new_file3= mgn + ini_file
    copyfile (ini_file, new_file2)
    #copyfile (ini_file, new_file3)

    new_file_name = ini_file[1].replace('.ini', '_folded.ini')
    #copyfile (ini_file, new_file_name)


    for i, b in zip(mal,alista):
         
        def replacetext(search_text, replace_text):

            with FileInput(ini_file, inplace=True,
                        backup='.bak') as f:
                for line in f:
                    print(line.replace(search_text,
                                    replace_text), end='')

        search_text = i
        replace_text = b
        print(replacetext(search_text, replace_text))

    date2 = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    print(date2)
    with open(filename, "r") as f:
        contents = f.readlines()
    contents.insert(18, ";ECT-ETI Configurator version 1.05.01")
    contents.insert(20, ";File creation timestamp: " + date2)   
    with open(filename, "w") as f:
        contents = "".join(contents)
        f.write(contents)
        f.close

    def phoneid():
        bc = []
        bc.append(phone1)
        bc.append(phone2)
        bc.append(phone3)
        bc.append(phone4)
        bc.append(phone5)
        bc.append(phone6)
        blist = [i for i in bc if i]
        print("ph list= ",blist)
        
        from mal_it import plid
        print ("call id list =",plid)

        for m, n in zip (plid, blist):
            def replacetext(search_text, replace_text):

                with FileInput(ini_file, inplace=True,
                        backup='.bak2') as f:
                    for line in f:
                        print(line.replace(search_text,
                                    replace_text), end='')                      
        search_text = m
        replace_text = n
        print(replacetext(search_text, replace_text))

    if callid==1:
        phoneid()
    else:
        print(callid)

    print ("old name=", ini_file )
    new_name= (ini_file + "_" + mgn2 +  "_" + ip + ".ini")
    new_name2= (mgn2 +  "_" + ip + ".ini")
    #new_name= ( u_gtname + "_" + ini_file + ".ini")
    print ("new name =", new_name)
    shutil.copy (ini_file, new_name)
    shutil.copy (ini_file, new_name2)
    copyfile (new_file2, ini_file)






    print("File generation complete!  A backup file has been created with extension '.backup.ini'.")
    tkinter.messagebox.showinfo("Success",  " File generation completed. A backup file has been created with extension '.backup.ini'.") 
    



def eti_script():
    main = Tk()
    main.title ('ETI ini file Generator')

    main.geometry("550x900")
    main.config(bg='#F8F8F8')
    p1 = PhotoImage(file = 'moto_ico2.png')
    main.iconphoto(False, p1)

   
    bg= PhotoImage (file = "eti_bg.png")
    label1 = Label(main, image=bg)
    label1.place(x=0,y=0)


    var = StringVar()
    label = Label( main, textvariable=var, relief=RIDGE, font=("Helvetia",18), bg='#E0E0EE', fg="black", activebackground ="#4a7abc", activeforeground="white",)
    var.set("ETI INI FILE GENERATOR")
    label.place(x=100,y=5)
    zone = StringVar()
    zone.set("Zone ID")
    drop = OptionMenu(main, zone, "1","2","3","4","5","6","7")
    drop.place(x=290,y=105)

    def show():
        myLabel = label(main, text=zone.get()).pack()

    def gotoeti():
        print("ETI")

    #def ecteti():

        #if toggle_button.config('text')[-1] == 'ECT':
        #    toggle_button.config(text='ETI',relief=RIDGE,font=("Arial",12),bg='yellow', fg="blue",command=gotoeti)
        #    nmdsel["state"] = "disabled"
        #else:
        #    toggle_button.config(text='ECT',relief=RIDGE,font=("Arial",12),bg='blue', fg="black")
        #    nmdsel["state"] = "normal"


    #toggle_button = Button(text="ETI", width=10,relief=RIDGE,font=("Arial",12),bg='blue', 
    #fg="black")
    #toggle_button.place(x=200,y=55)

    ctieti = Label( main, text="Zone Selection                 ", relief=GROOVE, font=("Arial",12), fg="black")
    ctieti.place(x=50,y=110)

    
    tz = StringVar()
    tz.set("Time Zone")
    drop = OptionMenu(main, tz, "CST","EST","PACIFIC","MOUNTAIN","ALASKA","HAWAII","OTHER")
    drop.place(x=290,y=200)

    #
    mgipid = StringVar()
    mgipid.set("Hub ID")
    #HUB TYPE selection
    '''hub = StringVar()
    hub.set("  TYPE")
    drop = OptionMenu(main, hub, "  Analog","  Digital T1","  DIGITAL E1","  DIGITAL ISDN")
    drop.place(x=200,y=300)'''
    drop = OptionMenu(main, mgipid, "1","2","3","4")
    drop.place(x=290,y=150)

    mgipidsel = Label( main, text="Media Gateway (Hub) ID ", relief=GROOVE, font=("Arial",12), fg="black")
    mgipidsel.place(x=50,y=150)

    #mgip = Label( main, text="Media Gateway (Hub) IP address", relief=RIDGE, font=("Arial",12), fg="blue")
    #mgip.place(x=50,y=250)

    #mgip = Label( main, text="Media Gateway (Hub) IP address", relief=RIDGE, font=("Arial",12), fg="blue")
    #mgip.place(x=290,y=250)
#    mgtwy_ip = Entry (main)
#    mgtwy_ip.place(x=290,y=250)

    tzsel = Label( main, text="Time Zone Selection        ", relief=GROOVE, font=("Arial",12), fg="black")
    tzsel.place(x=50,y=200)

    def browseFiles():
        global filename
        filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("ini files",
                                                            "*.ini*"),
                                                        ("all files",
                                                            "*.*")))


        label_file_explorer.configure(text="File selected: "+filename)
        print(filename)

    label_file_explorer = Label(main,
                                text = "Template path = ",

                                fg = "black")
    label_file_explorer.place(x=50,y=320)
    button_explore = Button(main,
                            text = "Import ini Template        ",
                            relief=RAISED,
                            font="Arial",
                            fg="black",
                            cursor="hand2",
                            command = browseFiles)
    button_explore.place(x=50,y=250)
    print(filename)
    path = str(filename)
    print ("path=", path)

    def submit():
        global tz2
        global nmd
        global ictmg_p
        global zo
        global hub2
        global path
        global hubid

        zo=zone.get()
        tz2=tz.get()
        hubid=mgipid.get()
        hub2=int(hubid)
        hubid2=str(10+hub2)
        r="."
        gtwy_ip=["10",zo,"234",(hubid2)]
        mgtw_ip=r.join(gtwy_ip)
        ictmg_p=mgtw_ip

    def capt():
        z = zone.get()
        tiz = tz.get()
        ip = ictmg_p
        disp_data.insert(0,f'Zone:{z} \n Time zone:{tiz} \n Media Gateway Hub ip = {ip} \n Hub ID = {hubid}')

    disp_data = Entry(
        main,
        width=65,
        font=('Arial', 9)
        )
    disp_data.place(x=50,y=500)

    def data_disp():
        z = zone.get()
        tiz = tz.get()
        ip = ictmg_p
        tkinter.messagebox.showinfo("Collected Parameters for config file", f' Zone ID: {z} \n Time Zone: {tiz} \n Media Gateway Hub ip = {ip} \n Hub ID = {hubid} \n \n Proceed to generate ETI ini file')

    myButton7 = Button(main, text="Load Values",relief=RAISED,font=("Arial",16), bg='#E0E0EE', fg="black",cursor="hand2",
    activebackground ="#4a7abc", activeforeground="white",
    command = lambda:[submit(), capt(), data_disp()])
    myButton7.place(x=50,y=450)
    myButton8 = Button(main, text="GENERATE ETI ini FILE ",relief=RAISED,font=("Arial",14),bg='#E0E0EE', fg="black",cursor="hand2",
    activebackground ="#4a7abc", activeforeground="white", command = lambda:[main.destroy, eti_gen_conf()])
    myButton8.place(x=50,y=750)

    myButton9 = Button(main, text="EXIT",relief=RAISED,font=("Arial",14),bg='#E0E0EE', fg="black",cursor="hand2",
    command = main.quit)
    myButton9.place(x=50,y=810)

    def instructions():
        tkinter.messagebox.showinfo("Script Generator steps", "ECT-ETI ini File Generator\n\n\n1. Select ECT or ETI depending on your deployment\n2. Select Astro Zone\n3. Select NMD Site (ECT only)\n4. Enter Media Gateway (Hub) IP address (see Ip Plan)\n5. Import Template from local drive\n6. LOAD VALUES and Validate\n7. Verify Values\n8. Generate file and exit\n\n\nCheck READ ME FIRST file for more detail")
        return ("done amc026")
    def sup():
        tkinter.messagebox.showinfo("About Script Generator   VERSION 1.05.01", "Support email: amc026@motorolasolutions.com")

    menubar = Menu(main)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=main.quit)
    

    helpmenu = Menu(menubar, tearoff=0)

    helpmenu.add_command(label="Help with Script", command=instructions)
    helpmenu.add_command(label="About...", command=sup)
    helpmenu.add_separator()
    menubar.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="Exit Script Generator", command=main.quit)
    support = Menu(menubar, tearoff=0)
    support.add_command(label="amc026", command="instructions")
    main.config(menu=menubar)
    main.mainloop()

def eti_gen_conf():
    from mal_it import eti, eti2
    z=int(zo)
    if int(z)>7:
        print ("Astro zones valid values 1-7 please try again")
    zn = "zone{}".format(zo)
    znid = "z00{}".format(zo)
    znid_10 = "10.{}".format(zo)
    

    a=str(233)
    s="."
    f= ""
    b=str(0)
    zon = ["10",zo]
    zone=s.join(zon)
    reg=[znid,"IPPBX01"]
    reg2=f.join(reg)
    l_pdns = ["10",zo,a,"163"]
    l_sdns = ["10",b,b,"226"]
    Pdns=s.join(l_pdns)
    sdns=s.join(l_sdns)
    ra = ["10",zo,"233","166"]
    rad=s.join(ra)
    l_Pntp = ["10",zo,a,"89"]
    l_sntp = ["10",zo,a,"90"]
    pntp=s.join(l_Pntp)
    sntp=s.join(l_sntp)
    l_sysl = ["10",zo,a,"249"]
    mg01 = eti2[0]
    mg03=eti2[1]
    hubid2=["mg0",hubid]
    id=f.join(hubid2)
    j=""
    mdgty_n=["ippbx-mg0",hubid]
    gtname = j.join(mdgty_n)
    cipher = ("AES128-SHA256:AES256-SHA256'")
    k=""
    ngtname = [znid,gtname]
    u_gtname = k.join(ngtname)
 

    if tz2 == "CST":
        utcoff=(-21600)
    elif tz2 == "PACIFIC":
        utcoff=(-28800)
    elif tz2 == "MOUNTAIN":
        utcoff=(-25200)
    elif tz2 == "EST":
        utcoff=(-18000)
    elif tz2 == "ALASKA":
        utcoff=(-32400)
    elif tz2 == "HAWAII":
        utcoff=(-36000)
    else: utcoff=(-32400)

    utc2=str(utcoff)

    elist=[u_gtname]
    elist.append(Pdns)
    elist.append(sdns)
    elist.append(ictmg_p)
    elist.append(u_gtname)
    elist.append(zn)
    elist.append(utc2)
    elist.append(znid)
    elist.append(ictmg_p)
    elist.append(znid_10)
    elist.append(cipher)
    elist.append(reg2)

    
    from fileinput import FileInput
    bien = ["Pdns","pntp","sntp","ictmg_p","telphy","gtwy","Pdns","sysl","mgn","zn","nmd","nec_ip","utc2","nec_ip","mgn"]

    
    ini_file = filename
    new_file2= ini_file + "_backup.ini"
    print("initial file name=", ini_file)
    print("outcome file name=", new_file2)
    copyfile (ini_file, new_file2)


    for i, b in zip(eti,elist):
        
    

        def replacetext(search_text, replace_text):

            with FileInput(ini_file, inplace=True,
                        backup='.bak') as f:
                for line in f:
                    print(line.replace(search_text,
                                    replace_text), end='')

        search_text = i
        replace_text = b
        print(replacetext(search_text, replace_text))


    

    date2 = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    date3=datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    print(date2)
    print(date3)
    with open(filename, "r") as f:
        contents = f.readlines()
    contents.insert(18, ";ECT-ETI Configurator version 1.05.01")
    contents.insert(20, ";File creation timestamp: " + date2)   
    with open(filename, "w") as f:
        contents = "".join(contents)
        f.write(contents)

   
    print ("old name=", ini_file )
    new_name= (ini_file + "_" + u_gtname +  "_" + ictmg_p + ".ini")
    #new_name= ( u_gtname + "_" + ini_file + ".ini")
    print ("new name =", new_name)
    shutil.copy (ini_file, new_name)
    copyfile (new_file2, ini_file)

    print("File generation complete!  A backup file has been created with extension '.backup.ini'.")
    tkinter.messagebox.showinfo("Success",  " File generation completed. A backup file has been created with extension '.backup.ini'.") 
    #main.quit


root.mainloop()