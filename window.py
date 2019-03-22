from tkinter import filedialog
from tkinter import *
from controller import Controller


class Window(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.folder_path = StringVar()
        self.master = master

        self.controller = Controller(self)
        self.output = StringVar()
        self.description = StringVar()
        self.initWindow()
        self.controller.update()

    def initWindow(self):
        self.master.title("Introspection")

        self.pack(fill=BOTH, expand=0)

        # Pierwszy rzad - wybor folderu
        Label(self, text="Select folder").grid(row=0)
        Label(self, textvariable=self.controller.folder_path, bg="gray",
              width=90).grid(row=0, column=1, columnspan=4, padx=10)
        Button(self, text="Browse", command=self.browse_button,
               bg="blue", fg="white").grid(row=0, column=5, padx=10)

        Label(self, text="Akceptowane są tylko te funckje, które przyjmują 2 argumenty typu int.\nDziałania wykonywane są dla liczb >= 1").grid(
            row=1, columnspan=5)

        # Drugi rzad - lista plikow *.py
        Label(self, text="Select file (module)").grid(row=2, columnspan=3)
        self.file_list = Listbox(self, width=50, height=20)
        self.file_list.bind("<<ListboxSelect>>", self.controller.fileSelection)
        self.file_list.configure(exportselection=False)
        self.file_list.grid(row=3, column=0, columnspan=3)

        # Drugi rzad - lista dostepnych funkcji
        Label(self, text="Select Function").grid(
            row=2, column=3, columnspan=3)
        self.function_list = Listbox(self, width=50, height=20)
        self.function_list.bind("<<ListboxSelect>>",
                                self.controller.functionSelection)
        self.function_list.configure(exportselection=False)
        self.function_list.grid(row=3, column=3, columnspan=3)

        # Trzeci rząd - input
        Label(self, text="arg1: ").grid(row=4, column=1)

        self.arg1 = Entry(self, width=4)
        self.arg1.grid(row=5, column=1)

        self.arg1.delete(0, END)
        self.arg1.insert(0, "0")

        Label(self, text="arg2: ").grid(row=4, column=2)
        self.arg2 = Entry(self, width=4)
        self.arg2.grid(row=5, column=2)

        self.arg2.delete(0, END)
        self.arg2.insert(0, "0")

        # Opis funkcji
        Label(self, textvariable=self.description,
              bg="gray").grid(row=4, column=3, columnspan=3)

        # Trzeci rząd przycisk Calculate
        Button(self, text="Calculate", command=self.controller.calculate,
               bg="blue", fg="white").grid(row=6, column=1, columnspan=2)

        # Trzeci rząd wynik
        Label(self, text="Output", bg="green").grid(row=5, column=4)
        Label(self, textvariable=self.output,
              bg="yellow", width=10).grid(row=6, column=4)

    def browse_button(self):
        filename = filedialog.askdirectory()
        self.controller.folder_path.set(filename)
        self.controller.update()
        print(filename)
