from DataBase_Application.patients import *
from DataBase_Application.doctors import *
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
                else:
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
                print("Błędny login lub hasło!")


obj = DBConnect()