import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

class simpleapp_tk(tkinter.Tk):
	def __init__(self,parent):
		tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()

		self.entryVariable = tkinter.StringVar()
		self.entry = tkinter.Entry(self,textvariable=self.entryVariable)
		self.entry.grid(column=0,row=0,sticky='EW')
		self.entry = tkinter.Entry(self,textvariable=self.entryVariable)
		self.entry.grid(column=0,row=1,sticky='EW')
		self.entry.bind("<Return>", self.OnPressEnter)
		self.entryVariable.set(u"Enter Show Name.")

		button = tkinter.Button(self,text=u"Click me !",
								command=self.OnButtonClick)
		button.grid(column=1,row=0)

		broButton = tkinter.Button(self, text = 'Browse', width = 6, command=self.browse_file)
		broButton.grid(column=1,row=1)

		self.labelVariable = tkinter.StringVar()
		label = tkinter.Label(self,textvariable=self.labelVariable,
							  anchor="w",fg="black",bg="white")
		label.grid(column=0,row=2,columnspan=2,sticky='EW')
		self.labelVariable.set(u"Hello !")

		self.grid_columnconfigure(0,weight=1)
		self.resizable(True,True)
		self.update()
		self.geometry(self.geometry())       
		self.entry.focus_set()
		self.entry.selection_range(0, tkinter.END)
	
	def browse_file(self):

		fname = self.filedialog.askopenfilename(filetypes = (("Template files", "*.type"), ("All files", "*")))
		return self.fname

	def OnButtonClick(self):
		self.labelVariable.set( self.entryVariable.get()+" (You clicked the button)" )
		self.entry.focus_set()
		self.entry.selection_range(0, tkinter.END)

	def OnPressEnter(self,event):
		self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
		self.entry.focus_set()
		self.entry.selection_range(0, tkinter.END)

	

if __name__ == "__main__":
	app = simpleapp_tk(None)
	app.title('my application')
	app.mainloop()