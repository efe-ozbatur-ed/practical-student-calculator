# This is a practical multi-purpose calculator with a graphical user interface written in
# Python to help with studies and assignments. Optimised for mainly Turkish high schools.
# Originally developed in 2019, this version features an English translation for
# readability purposes for the Software Testing portfolio.

# Imports
import tkinter as tk
import math


# Main Class
class PracticalStudentCalculator(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        function_options = [StartPage, MolHesaplama, Basinc, Hacim, Sicaklik, Is, Yol, Kuvvet, Guc, Potansiyel, Kinetik,
                  Akim, Gerilim, Silindir, Kup, Dikdortgen, Kure, CemberCevre, CemberYayi, DaireAlan, DaireDilim,
                  IcAcilar, DuzgunIc, Kosegen, DuzgunDis, DogruDenklem, DogruEgim, YuzdeArtis, YuzdeAzalis,
                  KokBulma, Modulo, Faktoriyel, Trigonometri, HeceOlcusu]

        self.frames = {}
        for F in function_options:
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.Label(self, text="Welcome to the practical student calculator!", fg="white", bg="purple").grid(row=0,column=0, sticky="w")
        label2 = tk.Label(self, text="Choose a formula:\n", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        label3 = tk.Label(self, text="Chemistry: ", fg="white", bg="purple").grid(row=2,column=0, sticky="w")

        button1 = tk.Button(self, text="Mol calculation", highlightbackground="purple",
                            command=lambda: controller.show_frame("MolHesaplama")).grid(row=3, column=0, sticky="nsew")
        button2 = tk.Button(self, text="Pressure of a real gas", highlightbackground="purple",
                            command=lambda: controller.show_frame("Basinc")).grid(row=3, column=1, sticky="nsew")
        button3 = tk.Button(self, text="Volume of a real gas", highlightbackground="purple",
                            command=lambda: controller.show_frame("Hacim")).grid(row=3, column=2, sticky="nsew")
        button4 = tk.Button(self, text="Temperature of a real gas", highlightbackground="purple",
                            command=lambda: controller.show_frame("Sicaklik")).grid(row=3, column=3, sticky="nsew")

        label4 = tk.Label(self, text="\nPhysics: ", fg="white", bg="purple").grid(row=4, column=0, sticky="w")

        button5 = tk.Button(self, text="Work calculator", highlightbackground="purple",
                            command=lambda: controller.show_frame("Is")).grid(row=5, column=0, sticky="nsew")
        button6 = tk.Button(self, text="Distance calculator", highlightbackground="purple",
                            command=lambda: controller.show_frame("Yol")).grid(row=5, column=1, sticky="nsew")
        button7 = tk.Button(self, text="Force calculator", highlightbackground="purple",
                            command=lambda: controller.show_frame("Kuvvet")).grid(row=5, column=2, sticky="nsew")
        button8 = tk.Button(self, text="Power calculator", highlightbackground="purple",
                            command=lambda: controller.show_frame("Guc")).grid(row=5, column=3, sticky="nsew")
        button9 = tk.Button(self, text="Potential energy", highlightbackground="purple",
                            command=lambda: controller.show_frame("Potansiyel")).grid(row=6, column=0, sticky="nsew")
        button10 = tk.Button(self, text="Kinetic energy", highlightbackground="purple",
                            command=lambda: controller.show_frame("Kinetik")).grid(row=6, column=1, sticky="nsew")
        button11 = tk.Button(self, text="Current calculator", highlightbackground="purple",
                            command=lambda: controller.show_frame("Akim")).grid(row=6, column=2, sticky="nsew")
        button12 = tk.Button(self, text="Voltage calculator", highlightbackground="purple",
                            command=lambda: controller.show_frame("Gerilim")).grid(row=6, column=3, sticky="nsew")

        label5 = tk.Label(self, text="\nMaths: ", fg="white", bg="purple").grid(row=7, column=0, sticky="w")

        button13 = tk.Button(self, text="Cylinder volume", highlightbackground="purple",
                             command=lambda: controller.show_frame("Silindir")).grid(row=8, column=0, sticky="nsew")

        button14 = tk.Button(self, text="Cube volume", highlightbackground="purple",
                             command=lambda: controller.show_frame("Kup")).grid(row=8, column=1, sticky="nsew")

        button15 = tk.Button(self, text="Cuboid volume", highlightbackground="purple",
                             command=lambda: controller.show_frame("Dikdortgen")).grid(row=8, column=2, sticky="nsew")

        button16 = tk.Button(self, text="Sphere volume", highlightbackground="purple",
                             command=lambda: controller.show_frame("Kure")).grid(row=8, column=3, sticky="nsew")

        button17 = tk.Button(self, text="Circle circumference", highlightbackground="purple",
                             command=lambda: controller.show_frame("CemberCevre")).grid(row=9, column=0, sticky="nsew")

        button18 = tk.Button(self, text="Arc of circumference length", highlightbackground="purple",
                             command=lambda: controller.show_frame("CemberYayi")).grid(row=9, column=1, sticky="nsew")

        button19 = tk.Button(self, text="Area of a circle", highlightbackground="purple",
                             command=lambda: controller.show_frame("DaireAlan")).grid(row=9, column=2, sticky="nsew")

        button20 = tk.Button(self, text="Area of a circular sector", highlightbackground="purple",
                             command=lambda: controller.show_frame("DaireDilim")).grid(row=9, column=3, sticky="nsew")

        button21 = tk.Button(self, text="Interior angle sum of a polygon", highlightbackground="purple",
                             command=lambda: controller.show_frame("IcAcilar")).grid(row=10, column=0, sticky="nsew")

        button22 = tk.Button(self, text="Interior angle of a regular polygon", highlightbackground="purple",
                             command=lambda: controller.show_frame("DuzgunIc")).grid(row=10, column=1, sticky="nsew")

        button23 = tk.Button(self, text="Number of diagonals", highlightbackground="purple",
                             command=lambda: controller.show_frame("Kosegen")).grid(row=10, column=2, sticky="nsew")

        button24 = tk.Button(self, text="Exterior angle of a regular polygon", highlightbackground="purple",
                             command=lambda: controller.show_frame("DuzgunDis")).grid(row=10, column=3, sticky="nsew")

        button25 = tk.Button(self, text="Equation of a line", highlightbackground="purple",
                             command=lambda: controller.show_frame("DogruDenklem")).grid(row=11, column=0, sticky="nsew")

        button26 = tk.Button(self, text="Line slope calculator", highlightbackground="purple",
                             command=lambda: controller.show_frame("DogruEgim")).grid(row=11, column=1, sticky="nsew")

        button27 = tk.Button(self, text="Percentage increase finder", highlightbackground="purple",
                             command=lambda: controller.show_frame("YuzdeArtis")).grid(row=11, column=2, sticky="nsew")

        button28 = tk.Button(self, text="Percentage decrease finder", highlightbackground="purple",
                             command=lambda: controller.show_frame("YuzdeAzalis")).grid(row=11, column=3, sticky="nsew")

        button29 = tk.Button(self, text="Exponent and root finder", highlightbackground="purple",
                             command=lambda: controller.show_frame("KokBulma")).grid(row=12, column=0, sticky="nsew")

        button30 = tk.Button(self, text="Modulo finder", highlightbackground="purple",
                             command=lambda: controller.show_frame("Modulo")).grid(row=12, column=1, sticky="nsew")

        button31 = tk.Button(self, text="Factorial finder", highlightbackground="purple",
                             command=lambda: controller.show_frame("Faktoriyel")).grid(row=12, column=2, sticky="nsew")

        button32 = tk.Button(self, text="Trigonometry (Radian)", highlightbackground="purple",
                             command=lambda: controller.show_frame("Trigonometri")).grid(row=12, column=3, sticky="nsew")

        label6 = tk.Label(self, text="\nExtras: ", fg="white", bg="purple").grid(row=13, column=0, sticky="w")

        button32 = tk.Button(self, text="Syllabic verse calculator for Turkish", highlightbackground="purple",
                             command=lambda: controller.show_frame("HeceOlcusu")).grid(row=14, column=0, sticky="nsew")

        label7 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=15, column=0, sticky="w")

        # Function to close the program
        def kapatma():
            self.destroy()
            exit()

        button31 = tk.Button(self, text="Exit program", highlightbackground="purple",
                             command= kapatma).grid(row=16, column=0, sticky="w")

        self.configure(background="purple")

# Mol calculation class
class MolHesaplama(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Mol calculator:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Enter the mass of the atom / molecule: ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Enter the atomic / molecular mass of the atom / molecule: ", fg="white", bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            try:
                sonuc = num1 / num2
            except ZeroDivisionError:
                pass
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=5, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult (mol): ", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=7, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Pressure of a real gas class
class Basinc(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Pressure of a real gas:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Volume of the gas: ", fg="white", bg="purple").grid(row=1,column=0,sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        hacim = 0

        try:
            hacim = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Mol number of the gas: ", fg="white",
                          bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        mol = 0

        try:
            mol = int(entry2.get())
        except ValueError:
            pass

        label4 = tk.Label(self, text="Temperature value of the gas (in Celsius): ", fg="white",
                          bg="purple").grid(row=5, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=6, column=0, sticky="w")

        sicaklik = 0

        try:
            sicaklik = float(entry3.get())
        except ValueError:
            pass

        def hesap():
            hacim = float(entry1.get())
            mol = float(entry2.get())
            sicaklik = float(entry3.get()) + 273.0

            try:
                sonuc = (mol * 22.4 * sicaklik) / 273
                sonuc = sonuc / hacim
            except ZeroDivisionError:
                pass
            entry4.delete(0, "end")

            entry4.insert(0, sonuc)

        button1 = tk.Button(self, text="Calculate", highlightbackground="purple", command=hesap).grid(row=7, column=0,
                                                                                                    sticky="w")

        label5 = tk.Label(self, text="\nResult (atm): ", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        entry4 = tk.Entry(self, highlightbackground="purple")

        entry4.grid(row=9, column=0, sticky="w")

        self.configure(background="purple")

        label6 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=10, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=11, column=0, sticky="w")

# Volume of a real gas class
class Hacim(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Volume of a real gas:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Pressure amount of the gas: ", fg="white", bg="purple").grid(row=1,column=0,sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        basinc = 0

        try:
            basinc = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Mol number of the gas: ", fg="white",
                          bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        mol = 0

        try:
            mol = int(entry2.get())
        except ValueError:
            pass

        label4 = tk.Label(self, text="Temperature value of the gas (in Celsius): ", fg="white",
                          bg="purple").grid(row=5, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=6, column=0, sticky="w")

        sicaklik = 0

        try:
            sicaklik = int(entry3.get())
        except ValueError:
            pass

        def hesap():
            basinc = float(entry1.get())
            mol = float(entry2.get())
            sicaklik = float(entry3.get()) + 273.0

            try:
                sonuc = (mol * 22.4 * sicaklik) / 273
                sonuc = sonuc / basinc
            except ZeroDivisionError:
                pass
            entry4.delete(0, "end")

            entry4.insert(0, sonuc)

        button1 = tk.Button(self, text="Calculate", highlightbackground="purple", command=hesap).grid(row=7, column=0,
                                                                                                    sticky="w")

        label5 = tk.Label(self, text="\nResult (L): ", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        entry4 = tk.Entry(self, highlightbackground="purple")

        entry4.grid(row=9, column=0, sticky="w")

        self.configure(background="purple")

        label6 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=10, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=11, column=0, sticky="w")

# Temperature of a real gas class
class Sicaklik(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Temperature of a real gas:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Pressure amount of the gas: ", fg="white", bg="purple").grid(row=1,column=0,sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        basinc = 0

        try:
            basinc = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Mol number of the gas: ", fg="white",
                          bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        mol = 0

        try:
            mol = int(entry2.get())
        except ValueError:
            pass

        label4 = tk.Label(self, text="Volume of the gas: ", fg="white",
                          bg="purple").grid(row=5, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=6, column=0, sticky="w")

        hacim = 0

        try:
            hacim = int(entry3.get())
        except ValueError:
            pass

        def hesap():
            basinc = float(entry1.get())
            mol = float(entry2.get())
            hacim = float(entry3.get())

            try:
                sonuc = (basinc * hacim)
                sonuc = sonuc / ((mol * 22.4) / 273)
                sonuc = sonuc - 273
            except ZeroDivisionError:
                pass
            entry4.delete(0, "end")

            entry4.insert(0, sonuc)

        button1 = tk.Button(self, text="Calculate", highlightbackground="purple", command=hesap).grid(row=7, column=0,
                                                                                                    sticky="w")

        label5 = tk.Label(self, text="\nResult (Celsius): ", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        entry4 = tk.Entry(self, highlightbackground="purple")

        entry4.grid(row=9, column=0, sticky="w")

        self.configure(background="purple")

        label6 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=10, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=11, column=0, sticky="w")

# Work calculator class
class Is(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Work calculator:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Applied force: ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Distance amount (∆x): ", fg="white", bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            try:
                sonuc = num1 * num2
            except ZeroDivisionError:
                pass
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=5, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult (Joule): ", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=7, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Distance calculator
class Yol(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Distance calculator:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Acceleration value: ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Amount of time (s): ", fg="white", bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            sonuc = (num1 * (num2*num2)) / 2
            entry3.delete(0, "end")
            entry3.insert(0, sonuc)

        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=5, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult (m): ", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=7, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Force calculator class
class Kuvvet(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Force calculator:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Mass of the object: ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Acceleration amount: ", fg="white", bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            sonuc = num1 * num2
            entry3.delete(0, "end")
            entry3.insert(0, sonuc)

        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=5, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult (N): ", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=7, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Power calculator
class Guc(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Power calculator:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Amount of work: ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Amount of elapsed time (s): ", fg="white", bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            try:
                sonuc = num1 / num2
            except ZeroDivisionError:
                pass
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=5, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult (Watt): ", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=7, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Potential energy calculator class
class Potansiyel(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Potential energy calculator:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Mass of the object (kg): ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Height (m): ", fg="white", bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            sonuc = num1 * 10 * num2
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=5, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult (Joule): ", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=7, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Kinetic energy calculator class
class Kinetik(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Kinetic energy calculator:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Mass of the object (kg): ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Velocity amount (v): ", fg="white", bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            sonuc = (num1 * (num2 * num2)) / 2
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=5, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult (Joule): ", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=7, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Current intensity calculator
class Akim(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Current intensity:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Amount of charge (q): ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Amount of time (t): ", fg="white", bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            try:
                sonuc = num1 / num2
            except ZeroDivisionError:
                pass
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=5, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult (Amper): ", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=7, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Voltage calculator
class Gerilim(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Voltage calculator:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Amount of current (I): ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Amount of resistance (R): ", fg="white", bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            sonuc = num1*num2
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=5, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult (V): ", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=7, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Cylinder volume calculator
class Silindir(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Cylinder volume calculator:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Radius of the base: ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Cylinder height: ", fg="white", bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            sonuc = (num1*num1)*num2
            sonuc = str(sonuc) + "π"
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=5, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult (cm^3): ", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=7, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Cube volume calculator
class Kup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Cube volume:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Length of a single edge of the cube: ", fg="white", bg="purple").grid(row=1,column=0,sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        def hesap():
            num1 = float(entry1.get())

            sonuc = num1*num1*num1

            entry4.delete(0, "end")

            entry4.insert(0, sonuc)

        button1 = tk.Button(self, text="Calculate", highlightbackground="purple", command=hesap).grid(row=3, column=0,
                                                                                                    sticky="w")

        label5 = tk.Label(self, text="\nResult (cm^3): ", fg="white", bg="purple").grid(row=4, column=0, sticky="w")

        entry4 = tk.Entry(self, highlightbackground="purple")

        entry4.grid(row=5, column=0, sticky="w")

        self.configure(background="purple")

        label6 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=7, column=0, sticky="w")

# Cuboid volume calculator
class Dikdortgen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Cuboid volume:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Width of the cuboid: ", fg="white", bg="purple").grid(row=1,column=0,sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Length of the cuboid: ", fg="white",
                          bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        label4 = tk.Label(self, text="Height of the cuboid: ", fg="white",
                          bg="purple").grid(row=5, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=6, column=0, sticky="w")

        num3 = 0

        try:
            num3 = int(entry3.get())
        except ValueError:
            pass

        def hesap():
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            num3 = float(entry3.get())

            sonuc = num1*num2*num3
            entry4.delete(0, "end")

            entry4.insert(0, sonuc)

        button1 = tk.Button(self, text="Calculate", highlightbackground="purple", command=hesap).grid(row=7, column=0,
                                                                                                    sticky="w")

        label5 = tk.Label(self, text="\nResult (cm^3): ", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        entry4 = tk.Entry(self, highlightbackground="purple")

        entry4.grid(row=9, column=0, sticky="w")

        self.configure(background="purple")

        label6 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=10, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=11, column=0, sticky="w")

# Sphere volume calculator
class Kure(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Sphere volume:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Sphere radius: ", fg="white", bg="purple").grid(row=1,column=0,sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        def hesap():
            num1 = float(entry1.get())

            sonuc = (4*(num1*num1*num1)) / 3
            sonuc = str(sonuc) + "π"

            entry4.delete(0, "end")

            entry4.insert(0, sonuc)

        button1 = tk.Button(self, text="Calculate", highlightbackground="purple", command=hesap).grid(row=3, column=0,
                                                                                                    sticky="w")

        label5 = tk.Label(self, text="\nResult (cm^3): ", fg="white", bg="purple").grid(row=4, column=0, sticky="w")

        entry4 = tk.Entry(self, highlightbackground="purple")

        entry4.grid(row=5, column=0, sticky="w")

        self.configure(background="purple")

        label6 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=7, column=0, sticky="w")

# Circle circumference calculator
class CemberCevre(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Circle circumference:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Circle radius: ", fg="white", bg="purple").grid(row=1,column=0,sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        def hesap():
            num1 = float(entry1.get())

            sonuc = 2 * num1
            sonuc = str(sonuc) + "π"

            entry4.delete(0, "end")

            entry4.insert(0, sonuc)

        button1 = tk.Button(self, text="Calculate", highlightbackground="purple", command=hesap).grid(row=3, column=0,
                                                                                                    sticky="w")

        label5 = tk.Label(self, text="\nResult (cm): ", fg="white", bg="purple").grid(row=4, column=0, sticky="w")

        entry4 = tk.Entry(self, highlightbackground="purple")

        entry4.grid(row=5, column=0, sticky="w")

        self.configure(background="purple")

        label6 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=7, column=0, sticky="w")

# Arc of circumference length calculator
class CemberYayi(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Arc of circumference length:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Circle radius: ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Center angle of the arc: ", fg="white", bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            sonuc = 2 * num1 * (num2 / 360)
            sonuc = str(sonuc) + "π"
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=5, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult (cm^3): ", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=7, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Area of a circle calculator
class DaireAlan(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Area of a circle:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Circle radius: ", fg="white", bg="purple").grid(row=1,column=0,sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        def hesap():
            num1 = float(entry1.get())

            sonuc = num1 * num1
            sonuc = str(sonuc) + "π"

            entry4.delete(0, "end")

            entry4.insert(0, sonuc)

        button1 = tk.Button(self, text="Calculate", highlightbackground="purple", command=hesap).grid(row=3, column=0,
                                                                                                    sticky="w")

        label5 = tk.Label(self, text="\nResult (cm^2): ", fg="white", bg="purple").grid(row=4, column=0, sticky="w")

        entry4 = tk.Entry(self, highlightbackground="purple")

        entry4.grid(row=5, column=0, sticky="w")

        self.configure(background="purple")

        label6 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=7, column=0, sticky="w")

# Area of a circular sector calculator
class DaireDilim(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Area of a circular sector:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Circle radius: ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Center angle of the circular sector: ", fg="white", bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            sonuc = (num1 * num1) * (num2 / 360)
            sonuc = str(sonuc) + "π"
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=5, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult (cm^2): ", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=7, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Interior angle sum of a polygon calculator
class IcAcilar(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Interior angle sum of a polygon:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Number of edges of the polygon: ", fg="white", bg="purple").grid(row=1,column=0,sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())

            sonuc = (num1 - 2) * 180

            entry4.delete(0, "end")

            entry4.insert(0, sonuc)

        button1 = tk.Button(self, text="Calculate", highlightbackground="purple", command=hesap).grid(row=3, column=0,
                                                                                                    sticky="w")

        label5 = tk.Label(self, text="\nResult (angle): ", fg="white", bg="purple").grid(row=4, column=0, sticky="w")

        entry4 = tk.Entry(self, highlightbackground="purple")

        entry4.grid(row=5, column=0, sticky="w")

        self.configure(background="purple")

        label6 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=7, column=0, sticky="w")

# Interior angle of a regular polygon calculator
class DuzgunIc(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Number of diagonals:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Number of edges of the polygon: ", fg="white", bg="purple").grid(row=1,column=0,sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())

            sonuc = ((num1 - 2) * 180) / num1

            entry4.delete(0, "end")

            entry4.insert(0, sonuc)

        button1 = tk.Button(self, text="Calculate", highlightbackground="purple", command=hesap).grid(row=3, column=0,
                                                                                                    sticky="w")

        label5 = tk.Label(self, text="\nResult (angle): ", fg="white", bg="purple").grid(row=4, column=0, sticky="w")

        entry4 = tk.Entry(self, highlightbackground="purple")

        entry4.grid(row=5, column=0, sticky="w")

        self.configure(background="purple")

        label6 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=7, column=0, sticky="w")

# Number of diagonals calculator
class Kosegen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Number of diagonals:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Number of edges of the polygon: ", fg="white", bg="purple").grid(row=1,column=0,sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())

            sonuc = (num1 * (num1-3)) / 2

            entry4.delete(0, "end")

            entry4.insert(0, sonuc)

        button1 = tk.Button(self, text="Calculate", highlightbackground="purple", command=hesap).grid(row=3, column=0,
                                                                                                    sticky="w")

        label5 = tk.Label(self, text="\nResult: ", fg="white", bg="purple").grid(row=4, column=0, sticky="w")

        entry4 = tk.Entry(self, highlightbackground="purple")

        entry4.grid(row=5, column=0, sticky="w")

        self.configure(background="purple")

        label6 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=7, column=0, sticky="w")

# Exterior angle of a regular polygon calculator
class DuzgunDis(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Exterior angle of a regular polygon:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Number of edges of the polygon: ", fg="white", bg="purple").grid(row=1,column=0,sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())

            sonuc = 360 / num1

            entry4.delete(0, "end")

            entry4.insert(0, sonuc)

        button1 = tk.Button(self, text="Calculate", highlightbackground="purple", command=hesap).grid(row=3, column=0,
                                                                                                    sticky="w")

        label5 = tk.Label(self, text="\nResult (angle): ", fg="white", bg="purple").grid(row=4, column=0, sticky="w")

        entry4 = tk.Entry(self, highlightbackground="purple")

        entry4.grid(row=5, column=0, sticky="w")

        self.configure(background="purple")

        label6 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=7, column=0, sticky="w")

# Equation of a line calculator
class DogruDenklem(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Equation of a line:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Coordinates of x1: ", fg="white", bg="purple").grid(row=1,column=0,sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Coordinates of y1: ", fg="white",
                          bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        label4 = tk.Label(self, text="Coordinates of x2: ", fg="white",
                          bg="purple").grid(row=5, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=6, column=0, sticky="w")

        num3 = 0

        try:
            num3 = int(entry3.get())
        except ValueError:
            pass

        label5 = tk.Label(self, text="Coordinates of y2: ", fg="white",
                          bg="purple").grid(row=7, column=0, sticky="w")

        entry4 = tk.Entry(self, highlightbackground="purple")

        entry4.grid(row=8, column=0, sticky="w")

        num4 = 0

        try:
            num4 = int(entry3.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            num3 = int(entry3.get())
            num4 = int(entry4.get())

            egim = (num2-num1) / (num4-num3)
            katsayi = num2 - (egim * num1)
            sonuc = str("y = " + str(egim) + "x + " + str(katsayi))
            entry5.delete(0, "end")

            entry5.insert(0, sonuc)

        button1 = tk.Button(self, text="Calculate", highlightbackground="purple", command=hesap).grid(row=9, column=0,
                                                                                                    sticky="w")

        label6 = tk.Label(self, text="\nResult: ", fg="white", bg="purple").grid(row=10, column=0, sticky="w")

        entry5 = tk.Entry(self, highlightbackground="purple")

        entry5.grid(row=11, column=0, sticky="w")

        self.configure(background="purple")

        label7 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=12, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=13, column=0, sticky="w")

# Line slope calculator
class DogruEgim(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Line slope calculator:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Coordinates of x1: ", fg="white", bg="purple").grid(row=1,column=0,sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Coordinates of y1: ", fg="white",
                          bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        label4 = tk.Label(self, text="Coordinates of x2: ", fg="white",
                          bg="purple").grid(row=5, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=6, column=0, sticky="w")

        num3 = 0

        try:
            num3 = int(entry3.get())
        except ValueError:
            pass

        label5 = tk.Label(self, text="Coordinates of y2: ", fg="white",
                          bg="purple").grid(row=7, column=0, sticky="w")

        entry4 = tk.Entry(self, highlightbackground="purple")

        entry4.grid(row=8, column=0, sticky="w")

        num4 = 0

        try:
            num4 = int(entry3.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            num3 = int(entry3.get())
            num4 = int(entry4.get())

            sonuc = (num2-num1) / (num4-num3)
            entry5.delete(0, "end")

            entry5.insert(0, sonuc)

        button1 = tk.Button(self, text="Calculate", highlightbackground="purple", command=hesap).grid(row=9, column=0,
                                                                                                    sticky="w")

        label6 = tk.Label(self, text="\nResult: ", fg="white", bg="purple").grid(row=10, column=0, sticky="w")

        entry5 = tk.Entry(self, highlightbackground="purple")

        entry5.grid(row=11, column=0, sticky="w")

        self.configure(background="purple")

        label7 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=12, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=13, column=0, sticky="w")

# Percentage increase finder
class YuzdeArtis(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Percentage increase finder:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Enter the number: ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Enter the percentage (do not write '%'): ", fg="white", bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            yuzde = (num1 * num2) / 100
            sonuc = num1 + yuzde
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=5, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult: ", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=7, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Percentage decrease finder
class YuzdeAzalis(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="# Percentage decrease finder:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Enter the number: ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Enter the percentage (do not write '%'): ", fg="white", bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            yuzde = (num1 * num2) / 100
            sonuc = num1 - yuzde
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=5, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult: ", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=7, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Exponent and root finder
class KokBulma(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Exponent and root finder:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Enter the number: ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Enter the exponent: ", fg="white", bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        def hesap():
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            sonuc = math.pow(num1, num2)
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=5, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult: ", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=7, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Modulo finder
class Modulo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Modulo finder:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Enter the divided number: ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        label3 = tk.Label(self, text="Enter the divider: ", fg="white", bg="purple").grid(row=3, column=0, sticky="w")

        entry2 = tk.Entry(self, highlightbackground="purple")

        entry2.grid(row=4, column=0, sticky="w")

        num2 = 0

        try:
            num2 = int(entry2.get())
        except ValueError:
            pass

        def hesap():
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            sonuc = num1 % num2
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=5, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult: ", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=7, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=8, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Factorial finder
class Faktoriyel(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Factorial finder:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Enter the number: ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        def hesap():
            num1 = int(entry1.get())
            sonuc = math.factorial(num1)
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=3, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult: ", fg="white", bg="purple").grid(row=4, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=5, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

# Trigonometry calculations in Radian
class Trigonometri(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Trigonometry (Radian):\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Enter the radian: ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        num1 = 0

        try:
            num1 = int(entry1.get())
        except ValueError:
            pass

        def sin():
            num1 = float(entry1.get())
            sonuc = math.sin(num1)
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)

        def cos():
            num1 = float(entry1.get())
            sonuc = math.cos(num1)
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)

        def tan():
            num1 = float(entry1.get())
            sonuc = math.tan(num1)
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)

        def cot():
            num1 = float(entry1.get())
            try:
                sonuc = 1 / (math.tan(num1))
            except ZeroDivisionError:
                pass
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)

        def asin():
            num1 = float(entry1.get())
            sonuc = math.asinh(num1)
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)

        def acos():
            num1 = float(entry1.get())
            sonuc = math.acosh(num1)
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)

        def atan():
            num1 = float(entry1.get())
            sonuc = math.atan(1/num1)
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)

        def acotf(x):
            pi = math.pi
            return (pi/2) - math.atan(x)

        def acot():
            num1 = float(entry1.get())
            try:
                sonuc = acotf(num1)
            except ZeroDivisionError:
                pass
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)

        def sec():
            num1 = float(entry1.get())
            try:
                sonuc = 1 / (math.cos(num1))
            except ZeroDivisionError:
                pass
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)

        def csc():
            num1 = float(entry1.get())
            try:
                sonuc = 1 / (math.sin(num1))
            except ZeroDivisionError:
                pass
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="sin", highlightbackground="purple", command=sin).grid(row=3, column=0,
                                                                                                        sticky="w")
        button2 = tk.Button(self, text="cos", highlightbackground="purple", command=cos).grid(row=4, column=0,
                                                                                                    sticky="w")
        button3 = tk.Button(self, text="tan", highlightbackground="purple", command=tan).grid(row=5, column=0,
                                                                                                    sticky="w")
        button4 = tk.Button(self, text="cot", highlightbackground="purple", command=cot).grid(row=6, column=0,
                                                                                                    sticky="w")
        button5 = tk.Button(self, text="asin", highlightbackground="purple", command=asin).grid(row=7, column=0,
                                                                                                    sticky="w")
        button6 = tk.Button(self, text="acos", highlightbackground="purple", command=acos).grid(row=8, column=0,
                                                                                                    sticky="w")
        button7 = tk.Button(self, text="atan", highlightbackground="purple", command=atan).grid(row=9, column=0,
                                                                                                 sticky="w")
        button8 = tk.Button(self, text="acot", highlightbackground="purple", command=acot).grid(row=10, column=0,
                                                                                                 sticky="w")
        button9 = tk.Button(self, text="sec", highlightbackground="purple", command=sec).grid(row=11, column=0,
                                                                                                 sticky="w")
        button10 = tk.Button(self, text="csc", highlightbackground="purple", command=csc).grid(row=12, column=0,
                                                                                                 sticky="w")

        label4 = tk.Label(self, text="\nResult (radian): ", fg="white", bg="purple").grid(row=13, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=14, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=15, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=16, column=0, sticky="w")

# Syllabic verse calculator for Turkish
class HeceOlcusu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Syllabic verse calculator for Turkish:\n ", fg="white", bg="purple").grid(row=0, column=0, sticky="w")

        label2 = tk.Label(self, text="Enter the word / sentence: ", fg="white", bg="purple").grid(row=1, column=0, sticky="w")

        entry1 = tk.Entry(self, highlightbackground="purple")

        entry1.grid(row=2, column=0, sticky="w")

        str1 = 0

        try:
            str1 = str(entry1.get())
        except ValueError:
            pass

        def hesap():
            str1 = str(entry1.get())
            ch= ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü', 'A', 'E', 'I', 'İ', 'O', 'Ö', 'U', 'Ü']
            hs1 = len(str1) - str1.replace(ch[0], "").__len__()
            hs2 = len(str1) - str1.replace(ch[1], "").__len__()
            hs3 = len(str1) - str1.replace(ch[2], "").__len__()
            hs4 = len(str1) - str1.replace(ch[3], "").__len__()
            hs5 = len(str1) - str1.replace(ch[4], "").__len__()
            hs6 = len(str1) - str1.replace(ch[5], "").__len__()
            hs7 = len(str1) - str1.replace(ch[6], "").__len__()
            hs8 = len(str1) - str1.replace(ch[7], "").__len__()
            hs9 = len(str1) - str1.replace(ch[8], "").__len__()
            hs10 = len(str1) - str1.replace(ch[9], "").__len__()
            hs11 = len(str1) - str1.replace(ch[10], "").__len__()
            hs12 = len(str1) - str1.replace(ch[11], "").__len__()
            hs13 = len(str1) - str1.replace(ch[12], "").__len__()
            hs14 = len(str1) - str1.replace(ch[13], "").__len__()
            hs15 = len(str1) - str1.replace(ch[14], "").__len__()
            hs16 = len(str1) - str1.replace(ch[15], "").__len__()
            sonuc = hs1+hs2+hs3+hs4+hs5+hs6+hs7+hs8+hs9+hs10+hs11+hs12+hs13+hs14+hs15+hs16
            entry3.delete(0, "end")

            entry3.insert(0, sonuc)


        button1 = tk.Button(self, text="Calculate", highlightbackground = "purple", command = hesap).grid(row=3, column=0, sticky="w")

        label4 = tk.Label(self, text="\nResult: ", fg="white", bg="purple").grid(row=4, column=0, sticky="w")

        entry3 = tk.Entry(self, highlightbackground="purple")

        entry3.grid(row=5, column=0, sticky="w")

        self.configure(background="purple")

        label5 = tk.Label(self, text="\n", fg="white", bg="purple").grid(row=6, column=0, sticky="w")

        button2 = tk.Button(self, text="Return back to main menu", highlightbackground="purple",
                             command=lambda: controller.show_frame("StartPage")).grid(row=9, column=0, sticky="w")

root = PracticalStudentCalculator()
root.mainloop()

