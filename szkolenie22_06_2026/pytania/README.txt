# 1. pakiety z modułami rozszerzenie modułów 

# 2. rozwinąć class i atrybut_domyślny


class KontoBankowe():
# jakis_atrybut_domyslny = 'jego wartosc'
# def __init__(self, imie, nazwisko='Kowalski'): # -->
#     self.imie = imie
#     self.nazwisko = nazwisko
# def dodaj(self,argument):
#     self.jakis_atrybut_domyslny.append(argument)


# k1 = KontoBankowe("Alicja", "Nowak")
# k2 = KontoBankowe("Damian")

# print('*'*40)
# print('Alicja')
# print(k1.imie,k1.nazwisko,k1.jakis_atrybut_domyslny)
# print('*'*40)
# print('Damian')
# print(k2.imie,k2.nazwisko,k2.jakis_atrybut_domyslny)

# k1.dodaj('bulka')

# print('*'*40)
# print('Alicja')
# print(k1.imie,k1.nazwisko,k1.jakis_atrybut_domyslny)
# print('*'*40)
# print('Damian')
# print(k2.imie,k2.nazwisko,k2.jakis_atrybut_domyslny)


# na listach też mi to nie działa tak, żeby atrybut_domyslny_1 był częścią wspólną:
class JakasKlasa():
    atrybut_domyslny_1 = ['default']
    def __init__(self):
        self.imie
        self.atrybut_domyslny_2 = []
k1 = JakasKlasa()
k2 = JakasKlasa()
k1.atrybut_domyslny_1 = [10]
print(f'k1.atrybut_domyslny_1 {k1.atrybut_domyslny_1}')
k1.atrybut_domyslny_2 = [20]
print(f'k1.atrybut_domyslny_2 {k1.atrybut_domyslny_2}')

print(f'k2.atrybut_domyslny_1 {k2.atrybut_domyslny_1}')
print(f'k2.atrybut_domyslny_2 {k2.atrybut_domyslny_2}')


# super
