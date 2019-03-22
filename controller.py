import glob
import inspect
import sys
import re

from tkinter import messagebox
from tkinter import *

from importlib.util import module_from_spec, spec_from_file_location
from os.path import basename, isdir, join, splitext


class Controller:

    def __init__(self, app):
        self.app = app
        self.folder_path = StringVar()
        self.folder_path.set("folder")
        self.file_list = None
        self.function_list = None

    def update(self):
        self.app.file_list.delete(0, END)
        self.app.function_list.delete(0, END)

        if isdir(self.folder_path.get()):
            self.files = glob.glob(join(self.folder_path.get(), '*.py'))
            for file in self.files:
                self.app.file_list.insert(
                    END, self.getFileNameWithoutExtension(file))

    def fileSelection(self, evt):
        self.app.function_list.delete(0, END)
        self.app.output.set("")
        self.app.description.set("")

        value = str((self.app.file_list.get(
            self.app.file_list.curselection())))
        print(value)

        spec = spec_from_file_location(value, join(
            self.folder_path.get(), value + '.py'))
        loaded = module_from_spec(spec)
        if not inspect.ismodule(loaded):
            raise AssertionError()

        spec.loader.exec_module(loaded)
        self.loaded = loaded
        for fnc in inspect.getmembers(loaded, inspect.isfunction):
            self._inspect(*fnc)

    def functionSelection(self, evt):
        self.app.output.set("")
        value = str((self.app.function_list.get(
            self.app.function_list.curselection())))

        for fnc in inspect.getmembers(self.loaded, inspect.isfunction):
            if fnc[0] == value:
                print(value)
                self.fnc = fnc
                self.app.description.set('"{}"'.format(inspect.getdoc(fnc[1])))

    def getFileNameWithoutExtension(self, name):
        return splitext(basename(name))[0]

    def _inspect(self, name, fnc):
        spec = inspect.getfullargspec(fnc)
        if 2 != len(spec.args) or\
                self._incorrect_return(spec, int) or\
                self._incorrect_argument(spec, 0, int) or\
                self._incorrect_argument(spec, 1, int):
            return

        self.app.function_list.insert(END, name)

    def _incorrect_return(self, spec, class_):
        return self._incorrect_type(spec, 'return', class_)

    def _incorrect_argument(self, spec, name, class_):
        return self._incorrect_type(spec, spec.args[name], class_)

    def _incorrect_type(self, spec, key, class_):
        return key in spec.annotations and not issubclass(spec.annotations[key], class_)

    def execute(self, fnc):
        return fnc(self.x, self.y)

    def calculate(self):
        print(self.app.arg1.get() + " | " + self.app.arg2.get())
        if not re.search("^[0-9]+$", self.app.arg1.get()) or not re.search("^[0-9]+$", self.app.arg2.get()):
            messagebox.showerror("Error", "You must provide INTIGER numbers")
        elif not int(self.app.arg1.get()) or not int(self.app.arg1.get()):
            messagebox.showerror("Error", "Incorrect values")
        else:
            self.x = int((self.app.arg1.get()))
            self.y = int((self.app.arg2.get()))
            self.app.output.set(self.fnc[1](self.x, self.y))
