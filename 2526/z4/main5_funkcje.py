
# Często dany fragment kodu chcemy wykorzystać wielokrotnie - pomagają nam w tym funkcje.
# Powiedzmy, że chcemy używać wielokrotnie kodu służącego do znajdowania mediany trzech liczb (patrz przykład 1)

# Słówko def mówi, że deklarujemy właśnie funkcję
# Po def następuje nazwa funkcji
# Następnie podane są argumenty funkcji, czyli wartości, które funkcja ma jakoś "przetworzyć"
# Następnie mamy dwukropek, po którym zaczyna się ciało funkcji
def mediana(a, b, c):
    # Ciało funkcji musi być wcięte względem słówka def
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    # Zwracamy wartość środkową, czyli medianę; ktoś wywołujący funkcję może odczytać zwracaną wartość
    return b

# użycie funkcji, nazywane wywołaniem funkcji
# zwróconą wartość można wypisać
print(mediana(5, 3, 1))
# można też przypisać do zmiennej
ret = mediana(2, 1, 7)
print(ret)