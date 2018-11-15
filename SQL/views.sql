# adres pacjentów
create or replace view adres_pacjent as
    SELECT
		l.login,
        l.haslo,
        p.imie,
        p.nazwisko,
        d.ulica,
        d.nr_budynku,
        d.nr_lokalu,
        d.kod_pocztowy,
        d.miasto
    FROM
        pacjent AS p
            LEFT JOIN
        dane_teleadresowe AS d ON p.id_adres = d.id_adres
            join 
        login AS l ON l.id_login = p.id_login;
        
        
#choroba danego pacjenta
create or replace view pacjent_choroba as
SELECT 
    p.id_pacjent, l.login, l.haslo, p.imie, p.nazwisko, w.data_wizyty, c.nazwa_choroby as choroba, le.imie as imie_lekarza, le.nazwisko as nazwisko_lekarza 
FROM
    pacjent AS p
        LEFT JOIN
    wizyta AS w ON p.id_pacjent = w.id_pacjent
        LEFT JOIN
    choroba AS c ON w.id_choroba = c.id_choroba left join login as l on l.id_login = p.id_login left join lekarz as le on le.id_lekarz = w.id_lekarz;


#wyświetla id specjalizacji lekarzy
create or replace view lekarze_specjalizacje as
SELECT 
    l.id_lekarz,
    l.imie,
    l.nazwisko,
    s.id_specjalizacja 
FROM
    lekarz AS l
        JOIN
    lekarz_specjalizacja AS ls ON
         l.id_lekarz = ls.id_lekarz
        LEFT JOIN
    specjalizacja AS s ON ls.id_specjalizacja = s.id_specjalizacja
ORDER BY id_lekarz;

# wyświetla nazwy specjalizacji lekarzy
create or replace view lekarz_specjalizacja_2 as
SELECT 
    l.id_lekarz,
    l.imie,
    l.nazwisko,
    s.nazwa as specjalizacja
FROM
    lekarz AS l
        JOIN
    lekarz_specjalizacja AS ls ON
         l.id_lekarz = ls.id_lekarz
        LEFT JOIN
    specjalizacja AS s ON ls.id_specjalizacja = s.id_specjalizacja
ORDER BY id_lekarz;

#wyświetla dane osobowe lekarzy
create or replace view dane_lekarz as
SELECT 
    l.login,
    l.haslo,
    le.imie,
    le.nazwisko,
    d.ulica,
    d.nr_budynku,
    d.nr_lokalu,
    d.kod_pocztowy,
    d.miasto
FROM
    lekarz AS le
	 left JOIN
    dane_teleadresowe AS d ON le.id_adres = d.id_adres
      left JOIN
    login AS l ON l.id_login = le.id_login;
    
# wyświetla wizyty lekarza
create or replace view lekarz_wizyta as
SELECT 
	w.id_wizyta,
    l.login,
    l.haslo,
    le.imie as imie_l,
    le.nazwisko as nazwisko_l,
    p.imie,
    p.nazwisko,
    w.data_wizyty,
    c.nazwa_choroby
FROM
    lekarz AS le
        LEFT JOIN
    wizyta AS w ON le.id_lekarz = w.id_lekarz
        LEFT JOIN
    login AS l ON l.id_login = le.id_login
        LEFT JOIN
    choroba AS c ON w.id_choroba = c.id_choroba
        LEFT JOIN
    pacjent AS p ON p.id_pacjent = w.id_pacjent;

# pobiera id pacjenta
create or replace view id_pacjent as
select l.login, l.haslo, p.id_pacjent, p.imie, p.nazwisko from login as l  join pacjent as p on l.id_login = p.id_login;

#pobiera wizyty pacjenta
create or replace view deleteWizyta as
SELECT 
    p.id_pacjent, l.login, l.haslo, w.id_wizyta, p.imie, p.nazwisko, w.data_wizyty, c.nazwa_choroby as choroba, le.imie as imie_lekarza, le.nazwisko as nazwisko_lekarza 
FROM
    pacjent AS p
        LEFT JOIN
    wizyta AS w ON p.id_pacjent = w.id_pacjent
        LEFT JOIN
    choroba AS c ON w.id_choroba = c.id_choroba left join login as l on l.id_login = p.id_login left join lekarz as le on le.id_lekarz = w.id_lekarz;