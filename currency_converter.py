import tkinter as tk
from tkinter import *

class Currency:
    def __init__(self, root):
        self.root = root
        self.root.title("Meine Tkinter GUI")
        self.language = "de"
        self.texts = {
            "de": {
                "title": "Währungsrechner",
                "start_currency": "Startwährung",
                "target_currency": "Zielwährung",
                "amount_label": "Gib deinen Betrag ein:",
                "convert_button": "Umrechnen",
                "result_label": "",
                "to": "zu"
            },
            "en": {
                "title": "Currency Converter",
                "start_currency": "Start Currency",
                "target_currency": "Target Currency",
                "amount_label": "Enter your amount:",
                "convert_button": "Convert",
                "result_label": "",
                "to": "to"
            }
        }

    def show(self): 
        # Button für Sprachenwechsel
        self.button = tk.Button(self.root, text="Sprache wechseln", command=self.switch_language)
        self.button.pack(pady=10)

        # Startwährung
        self.opt1 = StringVar(value=self.texts[self.language]["start_currency"])

        # Dropdown-Optionen
        self.currencys = ["Yen", "Euro", "Dollar", "Schwedische Krone"]

        # Dropdown-Menü-1
        self.option_menu1 = OptionMenu(self.root, self.opt1, *self.currencys)
        self.option_menu1.pack()

        # Label
        self.lbl = Label(self.root, text=self.texts[self.language]["to"])
        self.lbl.pack()

        # Zielwährung
        self.opt2 = StringVar(value=self.texts[self.language]["target_currency"])

        # Dropdown-Optionen
        self.currencys = ["Yen", "Euro", "Dollar", "Schwedische Krone"]

        # Dropdown-Menü-2
        self.option_menu2 = OptionMenu(self.root, self.opt2, *self.currencys)
        self.option_menu2.pack()

        # Label
        self.label = tk.Label(self.root, text=self.texts[self.language]["amount_label"])
        self.label.pack(pady=10)

        # Entry-Feld
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        # Button
        self.button = tk.Button(self.root, text=self.texts[self.language]["convert_button"], command=self.umrechnen)
        self.button.pack(pady=10)

        # Label für Ausgabe
        self.output_label = tk.Label(self.root, text=self.texts[self.language]["result_label"])
        self.output_label.pack(pady=10)

    def umrechnen(self):
        betrag = float(self.entry.get())
        startwährung = self.opt1.get()
        zielwährung = self.opt2.get()

        kurse = {
            ("Euro", "Dollar"): 1.13,
            ("Dollar", "Euro"): 0.88496,

            ("Euro", "Yen"): 160.52,
            ("Yen", "Euro"): 0.0062,

            ("Euro", "Schwedische Krone"): 10.84,
            ("Schwedische Krone", "Euro"): 0.0922,

            ("Dollar", "Yen"): 141.6195,
            ("Yen", "Dollar"): 0.0071,

            ("Dollar", "Schwedische Krone"): 9.5841,
            ("Schwedische Krone", "Dollar"): 0.1044,

            ("Yen", "Schwedische Krone"): 0.0675,
            ("Schwedische Krone", "Yen"): 14.8068,
        }
        
        if startwährung == zielwährung:
            ergebnis = betrag
        else:
            ergebnis = betrag * kurse.get((startwährung, zielwährung), 1)

        self.output_label.config(text=f"{betrag:.2f} {startwährung} = {ergebnis:.2f} {zielwährung}")

    def switch_language(self, language=None):
        self.language = "en" if self.language == "de" else "de"
        for widget in self.root.winfo_children():
            widget.destroy()
        self.show()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    gui = Currency(root)
    gui.show()
    root.mainloop()