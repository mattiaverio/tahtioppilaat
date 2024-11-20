## Tahtioppilaat
[![GHA workflow Badge](https://github.com/PieniiSienii/tahtioppilaat/workflows/CI/badge.svg)](https://github.com/Pieniisienii/tahtioppilaat/actions)
[![codecov](https://codecov.io/gh/PieniiSienii/tahtioppilaat/graph/badge.svg?token=0N8NYQEJWQ)](https://codecov.io/gh/PieniiSienii/tahtioppilaat)

README:ssa tulee löytyä ainakin seuraavat asiat:
Linkit backlogeihin (backlogeista tulee olla luettavissa olevat versiot julkisessa internetissä)
Linkki CI-palveluun
Linkki sovelluksen toimivaan versioon (jos sovellus on verkossa)
Jos kyse työpöytäsovelluksesta, tulee ohjelmalle olla asennus- ja käyttöohje
Työlle tulee määritellä lisenssi https://help.github.com/articles/licensing-a-repository/
Lue [täältä](https://ohjelmistotuotanto-hy.github.io/flask/) lisää.

[Backlog linkki](https://docs.google.com/spreadsheets/d/1tfCgtgHHC6YhraJJi992deDDh6dO0IaimUXH1h2Ntps/edit?gid=0#gid=0)

Definition of done: 

Ohjelma toimii niin kuin user story kuvaa, koodia on testattu, jonka jälkeen löydetyt ongelmat korjattu.


Käyttöohje:

Kloonaa repositorio

Lataa poetry: pip install poetry

Lataa riippuvuudet: poetry install

Luo .env tiedosto, josta löytyy DATABASE_URL, TEST_ENV ja SECRET_KEY

Luo virtuaaliympäristö:poetry shell

Käynnistä ohjelma: python3 index.py

