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

def showDisease(self):
    self.c.execute("SELECT * FROM CHOROBA order by id_choroba")

    print("| %2s | %23s | %2s" % ("ID", "Choroba", "Opis"))

    dane = self.c.fetchall()

    for row in dane:
        id = row[0]
        nazwa = row[1]
        opis = row[2]

        print("| %2s | %23s | %20s" % (id, nazwa, opis))

def addDisease(self):

    showDisease(self)

    choroba = input("Podaj nazwę nowej choroby: ")
    opis = input("Podaj opis choroby: ")

    self.c.execute("INSERT INTO Choroba (nazwa_choroby, opis) VALUES (%s, %s)", (choroba, opis))

    self.c.transaction()