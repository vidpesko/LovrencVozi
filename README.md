
# LovrencVozi

  

Spletna aplikacija za obveščanje o prostih terminih za vozniški izpit

  

## Strani:

  

> Opomba: strani (URL povezve) ni nujno, da so enake spodnjim imenom.

  

1.  **main:** glavni vmesnik s povezavami/gumbi za navigacijo po celi strani.

2.  **add-reminder:** stran, kjer dodaš opomnik. Uporabnik lahko določi, katere kategorije ga zanimajo

3.  **edit / list -reminders:** pregled nad vsemi opomniki. Uporabnik lahko spremeni ali izbriše opomnik.

4.  **edit-reminder/>>id<<:** stran za urejanje opomnika (enaka stran kot za **add-reminder**

5.  **Vse povezano s uporabniki:** vpis/registracija uporabnika, nadzor nad računom (izbris, sprememba gesla, pozabljeno geslo), šifriranje uporabniških podatkov

  

## 1. main

  

Glavna vstopna točka v aplikacijo.

  

**Zahteve:**

- Če nisi prijavljen: gumb *Dodaj opomnik*, gumb *Prijavi se* in sporočilo, da nisi prijavljen. Kljub temo, da nisi prijavljen lahko dodaš opomnik. To povej uporabniku

- Če si prijavljen: gumb *Seznam opomnikov*

- Gumb *Prijavi se* na vrhu aplikacije. Gumb zamenja uporabniški ime, če je uporabnik že prijavljen

  

## 2. add-reminder

  

Stran za dodajanje opomnikov.

  

**Zahteve:**

- Vsa ustrezna polja za filtriranje po terminih - lokacija dropdown, kategorije, vrsta/tip

- Če nisi prijavljen, imaš polje za email naslov, če si prijavljen, pa imaš ta polje že zapoljnen s uporabniškim email naslovom

  

**Logika:**

- Ko pošlješ email s novim datumom, spodaj dodaš možnost odjave. Tako se bo anonimni uporabnik odjavil.

  

## 3. edit / list -reminders

  

Seznam vseh opomnikov, ki jih je uporabnik ustvaril. Stran je dostopna le, če si prijavljen.

  

**Zahteve:**

- Če ima uporabnik opomnike, pokažeš seznam opomnikov, če jih nima, pokažeš sporočilo.

- Vsak opomnik ima: gumb *uredi* -> preusmeritev v **edit-reminder/>>id<<** in gumb *izbriši*

  

## 4. edit-reminder/>>id<<

  

Stran za urejanje opomnikov. Strukturno enaka kot stran **add-remainder** , le da ima polja zapolnjena s podatki o opomniku.

  

## 5. Uporabniki

  

Implementiraj kasneje, zaenkrat anonimni uporabniki zadoščajo


## API Referenca

> Zgornje strani bodo implementirane v REACT front-end-u. Preko tega API bo react komuniciral s strežnikom.

1. **reminder/**

## 1. reminder/

- **Tip:** GET, POST

- **(GET Query) Parametri:** email

- **(POST Body) Parametri:** email, tip, kategorije, območje, lokacija, trenutni-datum

- **Vrne:** Event model(s)

- **Opis:** GET vrne vse opomnike, POST ustvari novega

## 2. 