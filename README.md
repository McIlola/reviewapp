# Ravintolaarvostelu
Sovellus jossa käyttäjä voi kirjautua sisään ja jättää arvostelun johonkin listalla olevaan ravintolaan. Käyttäjällä on mahdollisuus antaa tähtiä sekä kirjoittaa arvostelu. Arvosteluja voi lukea, sekä muita käyttäjiä voi hakea.
### Nykytilanne
- Sovellukseen voi luoda käyttäjän, kirjautua sisään ja kirjautua ulos.
- Ravintoloihin voi tällä hetkellä jättää arvosteluja jotka näkyvät sivulla.
- Arvostelujen keskiarvo ja määrä näkyy sivulla.
- Pystyy antaamaan kehotuksia uusien ravintoloiden lisäämiseen.
- Pystyy hakemaan muitten käyttäjiä nimellä ja seuraamaan heitä.
- Pystyy katsomaan omaa ja muitten profiilia jossa lukee heidän antamat arvostelut, kehotukset ja ketä he seuraavat.

## Testaus
### Fly.io
Sovellus lisätty fly.io:n (https://reviewapptsoha.fly.dev/) ei välttämättä toimi.
### Paikallistestaus
Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:
```
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
```
Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla
```
python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
```
Määritä vielä tietokannan skeema komennolla
```
psql < schema.sql
```
Nyt voit käynnistää sovelluksen komennolla
```
flask run
```
