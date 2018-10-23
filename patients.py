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

def showDisease(self):
    self.c.execute("select id_choroba, nazwa_choroby from choroba order by id_choroba")

    print("| %3s | %7s " % ("ID", "Choroba"))

    dane = self.c.fetchall()

    for row in dane:
        id = row[0]
        nazwa_choroby = row[1]

        print("| %3s | %5s " % (id, nazwa_choroby))


def idPatient(self, login, haslo):
    self.login = login
    self.haslo = haslo

    self.c.execute("SELECT * from id_pacjent where login=%s and haslo=%s", (login, haslo))

    print("| %3s | %10s | %10s " % ("ID", "Imię", "Nazwisko"))

    dane = self.c.fetchall()

    for row in dane:
        id = row[2]
        imie = row[3]
        nazwisko = row[4]

        print("| %3s | %10s | %10s " % (id, imie, nazwisko))


def specialization(self):
    self.c.execute("SELECT * from specjalizacja order by id_specjalizacja")

    print("| %3s | %12s" % ("ID", "Specjalizacja"))

    dane = self.c.fetchall()

    for row in dane:
        id = row[0]
        specjalizacja = row[1]

        print("| %3s | %13s" % (id, specjalizacja))


def doctor_specialization(self, specjalizacja):
    self.specjalizacja = specjalizacja

    self.c.execute("SELECT * FROM lekarze_specjalizacje where id_specjalizacja=%s", specjalizacja)

    print("| %3s | %6s" % ("ID", "Lekarz"))

    dane = self.c.fetchall()

    for row in dane:
        id = row[0]
        imie = row[1]
        nazwisko = row[2]

        print("| %3s | %8s" % (id, imie + " " + nazwisko))


def addVisit(self, login, haslo):
    self.login = login
    self.haslo = haslo

    idPatient(self, login, haslo)
    id = input("Podaj swoje ID: ")
    specialization(self)
    specjalizacja = input("Jaka specjalizacja lekarza Cie interesuję? (Podaj numer): ")
    doctor_specialization(self, specjalizacja)
    lekarz = input("Do jakiego lekarza umówić wizytę?(Podaj numer): ")
    showDisease(self)
    choroba = input("Jaka choroba?(Podaj numer): ")
    data = input("Podaj datę wizyty: ")

    self.c.execute("INSERT INTO wizyta (id_pacjent ,id_lekarz, id_choroba, data_wizyty) VALUES (%s ,%s, %s, %s)"
                   , (id, lekarz, choroba, data))

    self.transaction()


def deleteVisit(self, login, haslo):
    self.login = login
    self.haslo = haslo

    self.c.execute("select * from deleteWizyta where login=%s and haslo=%s", (login, haslo))

    print("| %2s | %12s | %23s | %15s " % ("ID", "Data wizyty", "Choroba",
                                           "Lekarz"))

    dane = self.c.fetchall()

    for row in dane:
        id = row[3]
        data = row[6]
        choroba = row[7]
        imie_l = row[8]
        nazwisko_l = row[9]

        print("| %2s | %12s | %23s | %15s " % (id, data, choroba, imie_l + " " + nazwisko_l))

    num = input("Podaj ID wizyty do odwołania: ")

    self.c.execute("DELETE from wizyta where id_wizyta=%s", num)

    self.transaction()