import sqlite3

connection = sqlite3.connect("poems.db")
cursor = connection.cursor()

cursor.execute("create table poems (poem_title text, poem_author text, poem_text text)")

release_list = [
    ('The Road Not Taken', 'Robert Frost', 'Two roads diverged in a yellow wood, And sorry I could not travel both...'),
    ('Ozymandias', 'Percy Bysshe Shelley', 'I met a traveller from an antique land Who said: Two vast and trunkless legs of stone...'),
    ('Daffodils', 'William Wordsworth', 'I wandered lonely as a cloud That floats on high o''er vales and hills...'),
    ('Sonnet 18', 'William Shakespeare', 'Shall I compare thee to a summer''s day? Thou art more lovely and more temperate...'),
    ('The Raven', 'Edgar Allan Poe', 'Once upon a midnight dreary, while I pondered, weak and weary...')
]

cursor.executemany("insert into poems values (?,?,?)", release_list)

for row in cursor.execute("select * from poems"):
    print(row)

connection.close()