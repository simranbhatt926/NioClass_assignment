import sqlite3
conn = sqlite3.connect('application.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    join_date TEXT NOT NULL
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amount REAL,
    transaction_date TEXT,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
)
''')


users = [
    (1, 'Amit', 'amit@gmail.com', '2024-11-01'),
    (2, 'Mohit', 'mohit@gmail.com', '2024-03-12'),
    (3, 'Simran', 'simran@gmail.com', '2024-02-09')
]
cur.executemany('INSERT INTO users VALUES (?, ?, ?, ?)', users)


transactions = [
    (1, 1, 100.0, '2024-05-01'),
    (2, 2, 200.0, '2024-05-15'),
    (3, 3, 300.0, '2024-02-20')
]
cur.executemany('INSERT INTO transactions VALUES (?, ?, ?, ?)', transactions)


conn.commit()
conn.close()

print("Database initialized and seeded with sample data.")
