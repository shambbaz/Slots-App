# Käytetään Python 3.13 -imagea
FROM python:3.13-slim

# Asetetaan työskentelyhakemisto
WORKDIR /app

# Kopioidaan riippuvuudet ja asennetaan ne
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopioidaan kaikki projektin tiedostot konttiin
COPY . .

# Varmistetaan, että tietokanta on olemassa
RUN python -c "from database import create_database; create_database()"

# Asetetaan komento, jolla käynnistetään peli
CMD ["python", "main.py"]
