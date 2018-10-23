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