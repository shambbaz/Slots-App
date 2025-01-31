import sys
import os
import pytest
from unittest.mock import patch  # 🛠 Mockkausta varten

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Lisää pääkansio polkuun

from main import check_winnings, get_slot_machine_spin, deposit  # Importoi testattavat funktiot

def test_check_winnings():
    columns = [['A', 'A', 'A'], ['A', 'A', 'A'], ['A', 'A', 'A']]
    winnings, winning_lines = check_winnings(columns, 3, 10, {'A': 5})
    assert winnings == 150
    assert winning_lines == [1, 2, 3]

def test_get_slot_machine_spin():
    result = get_slot_machine_spin(3, 3, {"A": 2, "B": 4, "C": 6, "D": 8})
    assert len(result) == 3  # Varmistetaan, että generoidaan kolme saraketta

@patch('builtins.input', side_effect=['10'])  # 🛠 Mockataan input() palauttamaan "10"
def test_deposit(mock_input):
    assert deposit() == 10  # Nyt testi ei kysy käyttäjältä mitään
