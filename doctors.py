def showPersonalDataL(self, login, haslo):
    self.login = login
    self.haslo = haslo

    self.c.execute("SELECT * FROM dane_lekarz where login=%s and haslo=%s", (login, haslo))

    print("| %8s | %8s | %19s | %5s | %5s | %8s | %10s |" % ("Imię", "Nazwisko", "Ulica", "Nr budynku",
                                                            "Nr lokalu", "Kod pocztowy", "Miasto"))
    dane = self.c.fetchall()

    for row in dane:
        imie = row[2]
        nazwisko = row[3]
        ulica = row[4]
        nr_budynku = row[5]
        nr_lokalu = row[6]
        kod_pocztowy = row[7]
        miasto = row[8]

        print("| %8s | %8s | %8s | %10s | %9s | %12s | %10s |" % (imie, nazwisko, ulica, nr_budynku, nr_lokalu,
                                                                  kod_pocztowy, miasto))


def showVisitL(self, login, haslo):
    self.login = login
    self.haslo = haslo

    self.c.execute("SELECT * from lekarz_wizyta where login=%s and haslo=%s", (login, haslo))

    dane = self.c.fetchall()

    if len(dane) > 4:

        print("| %4s | %8s | %10s | %12s | %23s   " % ("ID", "Imię", "Nazwisko", "Data wizyty", "Choroba"))

        for row in dane:
            id = row[0]
            imie = row[5]
            nazwisko = row[6]
            data_wizyty = row[7]
            choroba = row[8]

            print("| %2s | %8s | %10s | %12s | %23s " % (id, imie, nazwisko, data_wizyty, choroba))

    else:
        print("Brak zarejestrowanych wizyt!")


def deleteVisitL(self, login, haslo):
    self.login = login
    self.haslo = haslo

    showVisitL(self, login, haslo)

    num = input("Podaj ID wizyty do odwołania: ")

    self.c.execute("DELETE from wizyta where id_wizyta=%s", num)

    self.transaction()