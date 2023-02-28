import datetime

def tootajad():
    n = int(input("Sisestage tööliste hulk: "))
    работники = []
    год_рождения = []
    for i in range(n):
        имя = input(f"Sisestage nimi töötliste n{i+1}: ")
        год = int(input(f"Sisestage töötaja sünniaasta n{i+1}: "))
        работники.append(имя)
        год_рождения.append(год)
    return работники, год_рождения


def пенсионеры():
    работники, год_рождения = tootajad()
    текущий_год = datetime.datetime.now().year
    пенсионеры = [работники[i] for i in range(len(работники)) if текущий_год - год_рождения[i] >= 60]
    print("Список пенсионеров:")
    for пенсионер in пенсионеры:
        print(пенсионер)


def keskmine_vanus():
    работники, год_рождения = tootajad()
    текущий_год = datetime.datetime.now().year
    возрасты = [текущий_год - год_рождения[i] for i in range(len(работники))]
    средний_возраст = sum(возрасты) / len(работники)
    print(f"Keskmine töötaja vanus on {средний_возраст:.1f} aastat")


while True:
    print("Valige tegevus:")
    print("1 - Sisestage töötajate arv ja nende aasta")
    print("2 - Pensionäride nimekiri")
    print("3 - Leidke töötajate keskmine vanus")
    print("0 - Välju")
    valik = int(input("Sisestage number koos sobiva toiminguga: "))
    if valik == 1:
        tootajad()
    elif valik == 2:
        пенсионеры()
    elif valik == 3:
        keskmine_vanus()
    elif valik == 0:
        break
    else:
        print("Vale valik, proovige uuesti!")    