def showPersonalData(self, login, haslo):
    self.login = login
    self.haslo = haslo

    self.c.execute("SELECT * FROM adres_pacjent where login=%s and haslo=%s", (login, haslo))

    print("| %8s | %8s | %9s | %5s | %5s | %8s | %10s |" % ("Imię", "Nazwisko", "Ulica", "Nr budynku",
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


def showDoctors(self):
    self.c.execute("SELECT * from lekarz_specjalizacja_2")

    print("| %8s | %10s | %12s | %13s" % ("Numer", "Imię", "Nazwisko", "Specjalizacja"))

    dane = self.c.fetchall()

    for row in dane:
        id = row[0]
        imie = row[1]
        nazwisko = row[2]
        specjalizacja = row[3]

        print("| %8s | %10s | %12s | %13s" % (id, imie, nazwisko, specjalizacja))


def showVisit(self, login, haslo):
    self.login = login
    self.haslo = haslo

    self.c.execute("select * from pacjent_choroba where login=%s and haslo=%s", (login, haslo))

    print("| %8s | %10s | %12s | %23s | %15s " % ("Imię", "Nazwisko", "Data wizyty", "Choroba",
                                                  "Lekarz"))

    dane = self.c.fetchall()

    for row in dane:
        imie = row[3]
        nazwisko = row[4]
        data_wizyty = row[5]
        choroba = row[6]
        imie_l = row[7]
        nazwisko_l = row[8]

        print("| %8s | %10s | %12s | %23s | %15s" % (imie, nazwisko, data_wizyty, choroba,
                                                     imie_l + " " + nazwisko_l))