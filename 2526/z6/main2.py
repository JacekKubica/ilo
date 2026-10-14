# 3) Dany jest plik tekstowy (przykładowej) postaci
# kanapka: 2.50
# szarlotka: 1.50
# woda mineralna: 1.50
# Nazwy towarów mogą być wielowyrazowe, ale cena jest zawsze poprzedzona znakiem dwukropka.
# Napisz następujące funkcje
    # obliczanie ceny koszyka
    # dodawanie nowej pozycji do koszyka (na koniec)
    # usuwanie wybranej pozycji z koszyka (podajemy numer linii do usunięcia)
    # usuwanie wybranej pozycji z koszyka (podajemy nazwę towru do usunięcia)


def total_price(path):
    ret = 0
    #TODO
    # 0) Otworzyć plik i wczytać z niego dane
    with open(path, "r") as f:
        data = f.read()
    # 1) Przejść linia po linii (Wskazówka: użyć split z argumentem "\n")
    lines = data.split("\n")
    for l in lines:
        # 2) Każdą linię podzielić po znaku ":"
        temp = l.split(":")
        # 3) Drugą część linii (po dwukropku) skonwertować do float
        price = float(temp[1])
        # 4) Dodać otrzymany float do wartości zwracanej
        ret += price
    return ret

def new_item(path, name, price):
    with open(path, "a") as f:
        f.write(f"\n{name}: {price}")


def delete_item(path, line_number):
    with open(path, "r") as f:
        data = f.read()
    new_data = ""
    #TODO
    # 1) przejść linia po linii
    # 2) jeśli linia jest linią do usunięcia, nic nie robić
    # 3) w przeciwnym wypadku dopisać linię na koniec new_data
    with open(path, "W") as f:
        f.write(new_data)


new_item("data.txt", "jablko", "1.1")
tp = total_price("data.txt")
print(tp)