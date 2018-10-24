def addSpecialization(self):

    self.c.execute("SELECT * FROM SPECJALIZACJA")

    print("| %2s | %10s " % ("ID", "SPECJALIZACJA"))

    dane = self.c.fetchall()

    for row in dane:
        id = row[0]
        nazwa = row[1]

        print("| %2s | %10s " % (id, nazwa))

    nazwa = input("Podaj nazwę nowej specjalizacji: ")

    self.c.execute("INSERT INTO Specjalizacja (nazwa) VALUES (%s)", (nazwa))

    self.transaction()