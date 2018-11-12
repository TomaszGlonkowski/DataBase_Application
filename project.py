from DataBase_Application.patients import *
from DataBase_Application.doctors import *
from DataBase_Application.admin import *
import pymysql

class DBConnect:

    def __init__(self):
        self.conn = pymysql.connect("localhost", "root", "Tom94glo!", "hospital", charset="utf8")
        self.c = self.conn.cursor()
        print("Nastąpiło połączenie do bazy danych.")
        self.menu()

    def transaction(self):

        dec = input("Czy na pewno chcesz wprowadzić zmiany? T/N ").upper()

        if dec == "T":
            self.conn.commit()
        else:
            self.conn.rollback()


    def menu(self):
        global id, id_login, id_adres, id_lekarz
        log = input("Z - Zarejestruj się, L - logowanie\n")
        if log == "L":
            login = input("Podaj login: ")
            haslo = input("Podaj hasło: ")
            self.c.execute("SELECT * from login where login=%s and haslo=%s", (login, haslo))
            dane = self.c.fetchall()
            if len(dane) > 0:
                if dane[0][1] == 2:
                    print("Zalogowałeś się do systemu! (Pacjent)")
                    while True:
                        dec = input("Menu [P - pokaż dane osobowe, L - lekarze, W - wizyty, A - umów wizytę, "
                                    "D - odwołaj wizytę, Q - wyjdż] ").upper()
                        if dec == "P":
                            showPersonalData(self, login, haslo)
                        elif dec == "L":
                            showDoctors(self)
                        elif dec == "W":
                            showVisit(self, login, haslo)
                        elif dec == "A":
                            addVisit(self, login, haslo)
                        elif dec == "D":
                            deleteVisit(self, login, haslo)
                        elif dec == "Q":
                            break
                elif dane[0][1] == 1:
                    print("Zalogowałeś się do systemu! (Lekarz)")
                    while True:
                        dec = input("Menu [P - pokaż dane osobowe, W - wizyty, D - odwołaj wizytę, Q - wyjdź] ").upper()
                        if dec == "P":
                            showPersonalDataL(self, login, haslo)
                        elif dec == "W":
                            showVisitL(self, login, haslo)
                        elif dec == "D":
                            deleteVisitL(self, login, haslo)
                        elif dec == "Q":
                            break
                else:
                    print("Zalogowałeś się do systemu! (Admin)")
                    while True:

                        dec = input("\nMenu [PL - pokaż lekarzy, UL - usuń lekarza, PS - pokaż specjalizacje, "
                                    "DS - dodaj specjalizację, PC - pokaż choroby, DC - dodaj chorobę, "
                                    "PP - pokaż pacjentów, UP - usuń pacjenta Q - wyjdź] ").upper()

                        if dec == "DS":
                            addSpecialization(self)
                        elif dec == "PS":
                            showSpecialization(self)
                        elif dec == "PC":
                            showDisease(self)
                        elif dec == "DC":
                            addDisease(self)
                        elif dec == "PL":
                            showDoctors(self)
                        elif dec == "PP":
                            showPatients(self)
                        elif dec == "UP":
                            deletePatients(self)
                        elif dec == "UL":
                            deleteDoctors(self);
                        elif dec == "Q":
                            break

            else:
                print("Błędny login lub hasło!")
                self.menu()

        elif log == "Z":
            # start rejestracji nowego użytkownika

            message = input("Rejestrujesz się jako lekarz czy pacjent? L/P ")
            login = input("Podaj login: ")
            haslo = input("Podaj hasło: ")

            if message == "P":
                # proces rejestracji pacjenta

                id_role = 2
                self.c.execute("INSERT INTO hospital.login (id_role, login , haslo) VALUES (%s, %s , %s)",
                               (id_role, login, haslo))

                self.c.execute("SELECT * from login where login=%s and haslo=%s", (login, haslo))

                dane = self.c.fetchall()

                for row in dane:
                    id_login = row[0]

                # pacjent podaje dane osobowe

                imie = input("Podaj imię: ")
                nazwisko = input("Podaj nazwisko: ")
                pesel = input("Podaj pesel: ")
                data_urodzenia = input("Podaj datę urodzenia(format rrrr-mm-dd): ")

                self.c.execute("SELECT * FROM plec")
                print("| %2s | %10s    " % ("ID", "Płeć"))

                dane = self.c.fetchall()

                for row in dane:
                    id = row[0]
                    plec = row[1]

                    print("| %2s | %10s    " % (id, plec))

                plec = input("Podaj plec: (ID): ")

                # pacjent podaje dane teleadresowe

                ulica = input("Podaj ulicę: ")
                nr_budynku = input("Podaj nr budynku: ")
                nr_lokalu = input("Podaj nr lokalu: ")
                miasto = input("Podaj miasto: ")
                kod_pocztowy = input("Podaj kod pocztowy: ")
                wojewodztwo = input("Podaj wojewodztwo: ")
                kraj = input("Podaj kraj urodzenia: ")
                telefon = input("Podaj telefon kontaktowy: ")
                email = input("Podaj email: ")

                self.c.execute("INSERT INTO dane_teleadresowe (ulica, nr_budynku, nr_lokalu, miasto, kod_pocztowy, "
                               "wojewodztwo, kraj, telefon, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                               (ulica, nr_budynku, nr_lokalu, miasto, kod_pocztowy, wojewodztwo, kraj, telefon, email))

                self.c.execute("SELECT * FROM dane_teleadresowe where email=%s", (email))

                dane = self.c.fetchall()

                for row in dane:
                    id_adres = row[0]

                # pacjent zostaje wprowadzony do bazy danych

                self.c.execute("INSERT INTO pacjent (id_login, id_adres, id_plec, Imie, Nazwisko, Pesel, "
                               "Data_urodzenia) VALUES (%s ,%s ,%s, %s, %s , %s, %s)",
                               (id_login, id_adres, plec, imie, nazwisko, pesel, data_urodzenia))

            else:

                id_role = 1
                self.c.execute("INSERT INTO hospital.login (id_role, login , haslo) VALUES (%s, %s , %s)",
                               (id_role, login, haslo))

                self.c.execute("SELECT * from login where login=%s and haslo=%s", (login, haslo))

                dane = self.c.fetchall()

                for row in dane:
                    id_login = row[0]

                    #lekarz podaje dane osobowe

                    imie = input("Podaj imię: ")
                    nazwisko = input("Podaj nazwisko: ")
                    data_zatrudnienia = input("Podaj datę zatrudnienia(format rrrr-mm-dd): ")

                    self.c.execute("SELECT * FROM plec")
                    print("| %2s | %10s    " % ("ID", "Płeć"))

                    dane = self.c.fetchall()

                    for row in dane:
                        id = row[0]
                        plec = row[1]

                        print("| %2s | %10s    " % (id, plec))

                    plec = input("Podaj plec: (ID): ")

                    # lekarz podaje dane teleadresowe

                    ulica = input("Podaj ulicę: ")
                    nr_budynku = input("Podaj nr budynku: ")
                    nr_lokalu = input("Podaj nr lokalu: ")
                    miasto = input("Podaj miasto: ")
                    kod_pocztowy = input("Podaj kod pocztowy: ")
                    wojewodztwo = input("Podaj wojewodztwo: ")
                    kraj = input("Podaj kraj urodzenia: ")
                    telefon = input("Podaj telefon kontaktowy: ")
                    email = input("Podaj email: ")

                    self.c.execute("INSERT INTO dane_teleadresowe (ulica, nr_budynku, nr_lokalu, miasto, kod_pocztowy, "
                                   "wojewodztwo, kraj, telefon, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                   (ulica, nr_budynku, nr_lokalu, miasto, kod_pocztowy, wojewodztwo, kraj, telefon,
                                    email))

                    self.c.execute("SELECT * FROM dane_teleadresowe where email=%s", (email))

                    dane = self.c.fetchall()

                    for row in dane:
                        id_adres = row[0]

                    self.c.execute(
                        "INSERT INTO Lekarz (id_login, id_adres, id_plec, Imie, Nazwisko, Data_zatrudnienia) "
                        "VALUES (%s ,%s ,%s, %s, %s, %s)",
                        (id_login, id_adres, plec, imie, nazwisko, data_zatrudnienia))

                    # lekarz wybiera swoją specjalizację

                    print("\nWybór specjalizacji!\n")

                    self.c.execute("SELECT * FROM LEKARZ where id_login=%s", (id_login))

                    dane = self.c.fetchall()

                    for row in dane:
                        id_lekarz = row[0]

                    while True:

                        showSpecialization(self)

                        id_specjalizacja = input("\nPodaj ID swoich specjalizacji (Q - wyjście): ")

                        if id_specjalizacja != "Q":
                            self.c.execute("INSERT INTO Lekarz_Specjalizacja (id_lekarz, id_specjalizacja) "
                                           "VALUES (%s, %s)", (id_lekarz, id_specjalizacja))
                        elif id_specjalizacja == "Q":
                            break

            dec = input("Czy na pewno chcesz wprowadzić zmiany? T/N ").upper()

            if dec == "T":
                self.conn.commit()
                print("Pomyślnie przeszedłeś rejestrację - spróbuj się zalogować.\n")
                self.menu()
            else:
                print("Rozpocznij proces rejestracji ponownie!!\n")
                self.conn.rollback()
                self.menu()



obj = DBConnect()