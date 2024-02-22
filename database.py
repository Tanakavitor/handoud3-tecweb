import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self,banco):
        self.conn = sqlite3.connect(banco + '.db')
        self.conn.execute("""
    CREATE TABLE IF NOT EXISTS note (
        id INTEGER PRIMARY KEY,
        title TEXT,
        content TEXT NOT NULL 
    );
""")
    def add(self, note):
        id = note.id
        title = note.title
        content = note.content
        self.conn.execute("""INSERT INTO note (title, content) VALUES (?, ?)""", (title, content))
        self.conn.commit()
    def get_all(self):
        cursor = self.conn.execute("""SELECT id, title, content FROM note""")
        return [Note(id, title, content) for id, title, content in cursor]
        
    def update(self, entry):
        id = entry.id
        title = entry.title
        content = entry.content
        self.conn.execute("""UPDATE note SET title = ?, content = ? WHERE id = ?""", (title, content, id))
        self.conn.commit()

    def delete(self, id):
        self.conn.execute("""DELETE FROM note WHERE id = ?""", (id,))
        self.conn.commit()