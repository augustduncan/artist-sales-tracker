import sqlite3
from pathlib import Path

DB = Path("art.db")  

SCHEMA = """
    CREATE TABLE inventory (
        item_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        size TEXT, --dropdown menu
        category TEXT, --dropdown menu
        production_cost REAL,
        base_price REAL,
        min_price REAL,
        max_price REAL
            CHECK(max_price>=min_price | min_price IS NULL), --idk
        quantity INTEGER NOT NULL DEFAULT 0

    );

    CREATE TABLE transaction (
        transaction_id INTEGER PRIMARY KEY,
        item_id INTEGER NOT NULL REFERENCES inventory(item_id),
        event_id INTEGER REFERENCES event(event_id),
        customer_id INTEGER REFERENCES customer(customer_id),
        quantity INTEGER NOT NULL DEFAULT 1,
        amount_paid REAL NOT NULL,
        method TEXT,
        date TEXT,
        note TEXT

    );

    CREATE TABLE event (
        event_id INTEGER PRIMARY KEY,
        name TEXT,
        location TEXT,
        fee REAL
    );

    CREATE TABLE customer (
        customer_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        number TEXT

    );
"""

TEST_DATA = """
    INSERT INTO inventory(name, size, category, production_cost, min_price, max_price, quanitity)
    VALUES ();

    INSERT INTO 
    VALUES ();

    INSERT INTO 
    VALUES ();

    INSERT INTO 
    VALUES ();



"""


def connect():
    if not DB.exists():
        build = sqlite3.connect(DB)
        build.executescript(SCHEMA)
        build.commit()
        build.close()
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def reset():
    DB.unlink(missing_ok=True)