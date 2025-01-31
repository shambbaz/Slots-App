import sqlite3

def create_database():
    """Luo SQLite-tietokanta, jos sitä ei vielä ole."""
    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS game_results (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        balance INTEGER,
                        winnings INTEGER)''')
    conn.commit()
    conn.close()

def save_result(balance, winnings):
    """Tallentaa pelikierroksen lopputuloksen tietokantaan."""
    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO game_results (balance, winnings) VALUES (?, ?)", (balance, winnings))
    conn.commit()
    conn.close()
