import sqlite3
import random

conn = sqlite3.connect("results.db")
cursor = conn.cursor()

# Lisää 500 testikierrosta, joissa voitot riippuvat osittain saldosta
for i in range(500):
    balance = random.randint(50, 500)  # Satunnainen saldo
    winnings = int(balance * random.uniform(-0.3, 0.3))  # Voitto/tappio -30% - +30% saldosta
    cursor.execute("INSERT INTO game_results (balance, winnings) VALUES (?, ?)", (balance, winnings))

conn.commit()
conn.close()
print("✅ 500 uutta testikierrosta lisätty tietokantaan!")
