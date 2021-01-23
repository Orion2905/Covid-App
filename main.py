from covid import Covid
import tkinter as tk
import flag

class App:
    def __init__(self, root):
        root.geometry("500x600")
        root.resizable(False, False)
        root.title("COVID")

        font = ("Arial", 12)

        title = tk.Label(root, text="Scopri l'andamento del covid nel tuo paese")
        title.pack()

        title2 = tk.Label(root, text="Lista delle citta")
        title2.pack()

        self.city = tk.Listbox(root, width=50, font=font)
        self.get_stat()

        enter = tk.Label(root, text="Inserisci una tra i paesi elencati qui sopra: ")
        enter.pack()

        self.stat = tk.Listbox(root, width=50, font=font)

        y = tk.StringVar()
        self.input_1 = tk.Entry(root, textvariable=y)
        self.input_1.pack()

        btn = tk.Button(root, text="Esplora i dati", command=self.get_stat2)
        btn.pack()


        title3 = tk.Label(root, text="Dati relativi al tuo paese: ")
        title3.pack()

        copyrights = tk.Label(root, text="copyrights Orion")
        copyrights.pack(side=tk.BOTTOM)




    def get_stat(self):
        countries = Covid().list_countries()
        cnt=0
        for i in countries:
            cnt+=1
            self.city.insert(cnt, i)
            print(i)

        self.city.pack()

    def get_stat2(self):
        # c = input("Scegli il paese: ")
        stat = Covid().get_status_by_country_name(self.input_1.get())
        cnt=0
        self.stat.insert(cnt, "Dati relativi a: " + self.input_1.get())
        for l in stat:
            cnt+=1
            a = l
            b = stat[l]
            print(a + " : " + str(b))
            self.stat.insert(cnt, a + ": " + str(b))
            print(l, "->", stat[l])
        self.stat.pack()

if __name__ == "__main__":
    root = tk.Tk()
    run = App(root)
    root.mainloop()