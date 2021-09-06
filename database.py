import sqlite3

class Note(object):
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content

class Database(object):

     def __init__(self, filename):
          self.filename = filename+'.db'
          self.conn = sqlite3.connect(self.filename)
          self.note = self.conn.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);")

     def add(self, Note):
          self.conn.execute(f"INSERT INTO note (title, content) VALUES ('{Note.title}', '{Note.content}');")
          self.conn.commit()	
     
     def get_all(self):
          listaNotes = []
          cursor = self.conn.execute("SELECT id, title, content FROM note")
          for linha in cursor:
               ID = linha[0]
               TITLE = linha[1]
               CONTENT = linha[2]

               NOTE = Note(ID, TITLE, CONTENT)
               listaNotes.append(NOTE)
               
          return listaNotes
     
     def update(self, entry):
          self.conn.execute(f"UPDATE note SET title = '{entry.title}', content = '{entry.content}' WHERE id = '{entry.id}'")
          self.conn.commit()

     def delete(self, note_id):
          self.conn.execute(f"DELETE FROM note WHERE id = '{note_id}'")
          self.conn.commit()



