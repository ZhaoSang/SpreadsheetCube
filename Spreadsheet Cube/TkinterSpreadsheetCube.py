from tkinter import *

#create top banner
class Banner(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()


    def createWidget(self):
        #create logo
        global logo
        logo = PhotoImage(file="logo.png")
        self.label01 = Label(self, image=logo, anchor=W, width=50, height=40,bg="white")
        self.label01.grid(row=0,rowspan=2, column=0, sticky=W, padx=150,ipadx=150)

        #create toggle button with modes showing up
        global togglegif1, togglegif2
        togglegif1 = PhotoImage(file="Frame 1.png")
        togglegif2 = PhotoImage(file="Frame 2.png")
        self.label02 = Label(self, image=togglegif1, anchor=E, width=30, height=30, bg="white")
        self.label02.grid(column=1, row=0, pady=0, ipady=0,ipadx=0)
        self.label02.bind('<Button-1>', self.clicked)
        self.label03 = Label(self, text="Consolidation Mode", bg="white", width=18)
        self.label03.grid(column=1, row=1, sticky=E, pady=0, ipady=0,ipadx=100)

        #toggle event
    def clicked(self, event):
        if self.label03['text'] == "Consolidation Mode":
            self.label03.configure(text="Split Mode")
            self.label02.configure(image=togglegif2)
        else:
            self.label03.configure(text="Consolidation Mode")
            self.label02.configure(image=togglegif1)


#create original file banner
class OriginalFileBanner(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()


    def createWidget(self):

        # add a label for functions with original files/folder
        self.label04 = Label(self, text="Original Files    ", bg="white", width=18, anchor=CENTER, font=("Calibri", 14), fg="black")
        self.label04.grid(row=0,column=0, sticky=W)

        # add a button for additional functions - replace with Tkinter file dialog button later
        self.button01 = Button(self, text="   Select Folder    ", width=10, font=("Helvetica", 10))
        self.button01.grid(row=0, column=1, padx=20)

        # add labels for additional functions
        global photoadd, photounlock, photolock
        photoadd = PhotoImage(file="add row.png")
        photounlock = PhotoImage(file="unlock file.png")
        photolock = PhotoImage(file="lock file.png")
        self.label05 = Label(self, image=photounlock, anchor=W, width=120, height=30, bg="white")
        self.label05.grid(column=2, row=0, pady=0, ipady=0, ipadx=0)
        self.label06 = Label(self, image=photolock, anchor=W, width=120, height=30, bg="white")
        self.label06.grid(column=3, row=0, pady=0, ipady=0, ipadx=0)
        self.label07 = Label(self, image=photoadd, anchor=W, width=140, height=30, bg="white")
        self.label07.grid(column=4, row=0, pady=0, ipady=0, ipadx=0)




'''to do
class FileSelectorFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()


    def createWidget(self):
        pass


class TargetBannerFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()


    def createWidget(self):
        pass


class TargetFileSelectorFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()


    def createWidget(self):
        pass


class TargetFileSelectorFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()


    def createWidget(self):
        pass


class BottomFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()


    def createWidget(self):
        pass
'''



if __name__=="__main__":
    root = Tk()
    root.geometry("1000x600+200+100")
    root.title("Spreadsheet Cube")
    root["bg"] = "white"
    banner = Banner(root)
    banner["bg"] = "white"
    originalBanner = OriginalFileBanner(root)
    originalBanner["bg"] = "white"
    originalBanner["highlightbackground"] = "black"
    originalBanner["highlightthickness"] = 1

    '''to create later
    fileSelector = FileSelectorFrame(root)
    fileSelector["bg"] = "pink"
    targetBanner = TargetBannerFrame(root)
    targetBanner["bg"] = "light yellow"
    targetFileSelector = TargetFileSelectorFrame(root)
    targetFileSelector["bg"] = "light green"
    bottomFrame = BottomFrame(root)
    bottomFrame["bg"] = "violet"
    '''
    root.mainloop()