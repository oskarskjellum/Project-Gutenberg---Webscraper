Project Gutenberg – Webscraper

Dette prosjektet henter teksten fra en bok på Project Gutenberg og analyserer teksten ved hjelp av Python.

Krav

Du trenger:

Python
Git
Et virtuelt Python-miljø (venv)
Installere prosjektet

Klon prosjektet fra GitHub:

git clone https://github.com/oskarskjellum/Project-Gutenberg---Webscraper.git
cd Project-Gutenberg---Webscraper
Lage og aktivere venv

Lag et virtuelt Python-miljø:

python -m venv venv

Aktiver miljøet på Windows: ( venv\Scripts\activate )

På Mac/Linux: # source venv/bin/activate


Når venv er aktivert, skal du vanligvis se (venv) i starten av terminalen.

Installere pakkene

Installer alle nødvendige Python-biblioteker med:

( pip install -r requirements.txt )

requirements.txt inneholder:

requests
nltk
pytest

Hvis pip install -r requirements.txt ikke fungerer, kan pakkene installeres én etter én:

( pip install requests )
( pip install nltk )
( pip install pytest )

Du kan sjekke om pakkene er installert med:

( pip show requests )
( pip show nltk )
( pip show pytest )
