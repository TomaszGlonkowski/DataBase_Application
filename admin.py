def showSpecialization(self):
    self.c.execute("SELECT * FROM SPECJALIZACJA order by id_specjalizacja")

    print("| %2s | %10s " % ("ID", "SPECJALIZACJA"))

    dane = self.c.fetchall()

    for row in dane:
        id = row[0]
        nazwa = row[1]

        print("| %2s | %10s " % (id, nazwa))

def addSpecialization(self):

    showSpecialization(self)

    nazwa = input("Podaj nazwę nowej specjalizacji: ")

    self.c.execute("INSERT INTO Specjalizacja (nazwa) VALUES (%s)", (nazwa))

    self.transaction()