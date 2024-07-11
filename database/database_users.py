import sqlite3

class Users:

    db = sqlite3.connect("users.db")
    cursor = db.cursor()

    def create_db(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users ( 
                number INTEGER PRIMARY KEY AUTOINCREMENT,
                uid INTEGER, 
                username TEXT)""") 
        self.db.commit()

    async def check_user(self, msg):
        user_exists = self.cursor.execute(f"SELECT * FROM users WHERE uid = {msg.from_user.id}").fetchone()
        if user_exists:
            pass
        else:
            self.cursor.execute(f"INSERT INTO users (uid, username) VALUES ({msg.from_user.id}, '{msg.from_user.username}')")

        self.db.commit()

    async def clear_db(self, msg): #Если используется msg, то необходимо передавать callback.message заместо msg
        self.cursor.execute("DELETE FROM users")
        self.cursor.execute(f"INSERT INTO users (uid, username) VALUES ({msg.from_user.id}, '{msg.from_user.username}')")
        self.db.commit()
        await msg.message.answer(f"""База данных очищена!""")
        
