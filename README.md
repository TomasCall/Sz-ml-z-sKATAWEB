Ez egy számlázási weboldal amellyel a KATA-s vállalkozó nyomon tudja követni hogy milyen számlákat állított ki és hogy azokat a számlákat a megrendelők kifizették-e már.
A felhasznló tud számlákat létrehozni.
A felhasználó meg tudja nézni hogy az egyes megrendelőknek milyen értékben állított már ki összesen számlát az adott évben.

2021.10.02-2021.10.03:
Elkészítettem a belépési és a regisztrációs oldalt
A Frontend része teljesen készen van
Az adatbázisban már egy tábla megvan a felhasználói regisztrációs adatokkal (felhasználónév,email,jelszó) A másik táblával ami a számla adatokat tartalmazza még nem foglalkoztam.
Regisztrációnál az adatokat már el tudom tárolni de a jelszó még nincs hash-elve ezt a következő update alkalmával orvosolom.
Bejelentkezés nem működik még ezt a következő update alkalmával orvosolni fogom.

2021.10.02-2021.10.10:
Létrehoztam egy alap köszöntő oldalt ami akkor válik elérhetővé ha a felhasználó regisztrált vagy bejelentkezett.

2021.10.11-2021.10.17:
A Bejelentkezés és a Regisztráció már működik de még van mit csiszolni rajta.
Elkészült a számla bevitele oldal és egy demo a számlák lekérdezéséhez/módosításához(Itt kicsit elakadtam a dizájn nem akar összejönni de igyekszem kiküszöbölni a következő héten).

2021.10.17-2021.11.07:
Létrehoztam egy új adattáblát a számlák bevitelére.
Az egyes felhasználók le tudják kérni a számláikat a megfelelő oldalon és a táblázat a megfelelő színre szineződik a lekérdezett értékek alapján.
A Táblázat kapott egy új sokkal dizájnosabb kinézetet.
A Táblázat soraira kattintva a sorok értékeit a jobb oldalt lévő formba töltjük.(Még a frissítés nem működik de a következő commit alkalmával ez is javítva lesz)

2021.11.07-2021.11.21:
Elkészült a cégek oldal, még lehet lesznek benne változtatások de az csak az adott év nézésrée vontakozik, és lehet a táblázat jobban lesz igazítva.
Elkészült a bills insert oldal backend része teljesen továbbá optimalizálva lett a backend oldal. Frontenden még lesznek finomhangolások.
A jelszó mostmár hash-elve van tárolva
