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
        global id, id_login, id_adres
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
                        dec = input("\nMenu [PL - pokaż lekarzy, PS - pokaż specjalizacje, "
                                    "S - dodaj specjalizację, PC - pokaż choroby, C - dodaj chorobę, "
                                    "PP - pokaż pacjentów,").upper()

                        if dec == "S":
                            addSpecialization(self)
                        elif dec == "PS":
                            showSpecialization(self)
                        elif dec == "PC":
                            showDisease(self)
                        elif dec == "C":
                            addDisease(self)
                        elif dec == "PL":
                            showDoctors(self)
                        elif dec == "PP":
                            showPatients(self)


            else:
                print("Błędny login lub hasło!")
                self.menu()

        elif log == "Z":

            login = input("Podaj login: ")
            haslo = input("Podaj hasło: ")
            id_role = 2
            self.c.execute("INSERT INTO hospital.login (id_role, login , haslo) VALUES (%s, %s , %s)",
                           (id_role, login, haslo))

            self.c.execute("SELECT * from login where login=%s and haslo=%s", (login, haslo))

            dane = self.c.fetchall()

            for row in dane:
                id_login = row[0]

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

            self.c.execute("INSERT INTO pacjent (id_login, id_adres, id_plec, Imie, Nazwisko, Pesel, Data_urodzenia) "
                           "VALUES (%s ,%s ,%s, %s, %s , %s, %s)",
                           (id_login, id_adres, plec, imie, nazwisko, pesel, data_urodzenia))

            self.transaction()

            print("Pomyślnie przeszedłeś rejestrację - spróbuj się zalogować.\n")

            self.menu()


obj = DBConnect()