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
            CHECK(max_price >= min_price OR min_price IS NULL), 
        quantity INTEGER NOT NULL DEFAULT 0
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

    CREATE TABLE transactions (
        transaction_id INTEGER PRIMARY KEY,
        event_id INTEGER REFERENCES event(event_id),
        customer_id INTEGER REFERENCES customer(customer_id),
        date TEXT,
        note TEXT
    );

    CREATE TABLE sale (
        sale_id INTEGER PRIMARY KEY,
        transaction_id INTEGER REFERENCES transactions(transaction_id),
        item_id INTEGER NOT NULL REFERENCES inventory(item_id), --dropdown
        quantity INTEGER NOT NULL DEFAULT 1,
        amount_paid REAL NOT NULL, --autofill with basepricce
        method TEXT
    );
"""

TEST_DATA = """
    INSERT INTO inventory(name, size, category, production_cost, base_price, min_price, max_price, quantity)
    VALUES
        ('cat sticker', '3x3', 'sticker', 2.50, NULL, 3, 5, 40),
        ('warren wilson hoodie', 'medium', 'clothing', 17, 35, NULL, NULL, 10),
        ('sparkly keychain', '2x3', 'keychain', 5, 8.50, NULL, NULL, 12),
        ('artist sales tracker promotional poster', '8x5', 'print', 1.50, NULL, 5, 15, 20);

    INSERT INTO event(name, location, fee)
    VALUES 
        ('winter sale', 'warren wilson college', NULL),
        ('hypothetical asheville artist convention', 'downtown asheville', 200);

    INSERT INTO customer(name, email, number)
    VALUES 
        ('august duncan', 'august@email.com', '864-775-1234'),
        ('jackie yeargin', 'jackie@email.com', NULL);

    INSERT INTO transactions(event_id, customer_id, date)
    VALUES
        (1, 2, '2026-11-22'),
        (1, 2, '2026-11-22'),
        (2, 1, '2026-11-04'),
        (2, NULL, '2026-11-15');

    INSERT INTO sale(transaction_id, item_id, quantity, amount_paid, method)
    VALUES 
        (1, 4, 2, 12.75, 'cash'),
        (2, 2, 1, 17, 'cash'),
        (3, 1, 1, 35, 'card'),
        (NULL, 1, 1, 10, 'venmo'),
        (4, 3, 15, 1, 'venmo'),
        (4, 3, 15, 2, 'venmo');
"""


def connect():
    if not DB.exists(): 
        build = sqlite3.connect(DB)
        build.executescript(SCHEMA)
        #can toggle the following on and off as needed:
        build.executescript(TEST_DATA)
        build.commit()
        build.close()
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def reset():
    DB.unlink(missing_ok=True)