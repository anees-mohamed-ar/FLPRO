import sqlite3
from rich.console import Console
from time import sleep

console = Console()

DATABASE_FILE = "flpro_database.db"

def initialize_database():
    """Initialize the SQLite database and create tables if not exists."""
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    # Create table for original data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS original_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age_encrypted TEXT,
            age_decrypted INTEGER,
            income_encrypted TEXT,
            income_decrypted REAL,
            transactions_encrypted TEXT,
            transactions_decrypted INTEGER
        )
    """)

    # Create table for operated data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS operated_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age_encrypted TEXT,
            age_decrypted INTEGER,
            income_encrypted TEXT,
            income_decrypted REAL,
            transactions_encrypted TEXT,
            transactions_decrypted INTEGER
        )
    """)

    connection.commit()
    connection.close()
    sleep(2)
    console.print("[bold green]Database initialized successfully![/bold green]")
    sleep(2)

def insert_original_data(name, age_encrypted, age_decrypted, income_encrypted, income_decrypted, transactions_encrypted, transactions_decrypted):
    """Insert user-provided data into the original_data table."""
    console.print("[bold cyan]Uploading the Raw/Original Data entered by User[/bold cyan]")
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO original_data (name, age_encrypted, age_decrypted, income_encrypted, income_decrypted, transactions_encrypted, transactions_decrypted)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, age_encrypted, age_decrypted, income_encrypted, income_decrypted, transactions_encrypted, transactions_decrypted))

    connection.commit()
    connection.close()
    sleep(2)
    console.print("[bold green]Original data inserted into the database![/bold green]")
    sleep(2)

def insert_operated_data(name, age_encrypted, age_decrypted, income_encrypted, income_decrypted, transactions_encrypted, transactions_decrypted):
    """Insert client-operated data into the operated_data table."""
    console.print("[bold cyan]Uploading the Operated Data[/bold cyan]")
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO operated_data (name, age_encrypted, age_decrypted, income_encrypted, income_decrypted, transactions_encrypted, transactions_decrypted)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, age_encrypted, age_decrypted, income_encrypted, income_decrypted, transactions_encrypted, transactions_decrypted))

    connection.commit()
    connection.close()
    sleep(2)
    console.print("[bold green]Operated data inserted into the database![/bold green]")
    sleep(2)

def fetch_original_data():
    """Fetch all original data."""
    sleep(2)
    console.print("[bold cyan]Fetching the Raw/Original Data from Database[/bold cyan]")
    sleep(2)
    connection = sqlite3.connect(DATABASE_FILE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM original_data")
    data = cursor.fetchall()

    connection.close()
    return data

def fetch_operated_data():
    """Fetch all operated data."""
    sleep(2)
    console.print("[bold cyan]Fetching the Operated Data from Database[/bold cyan]")
    sleep(2)
    connection = sqlite3.connect(DATABASE_FILE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM operated_data")
    data = cursor.fetchall()

    connection.close()
    return data
