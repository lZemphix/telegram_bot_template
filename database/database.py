import sqlite3

class Users():

    def __init__(self):
        self.db = sqlite3.connect("users.db")
        self.cursor = self.db.cursor()

    def create_db(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users ( 
                number INTEGER PRIMARY KEY AUTOINCREMENT,
                uid INTEGER, 
                username TEXT)""") 
        self.save()

    async def clear_db(self, callback):
        self.cursor.execute("DELETE FROM users") #TODO: edit execute
        # self.cursor.execute(f"INSERT INTO users (uid, username, age, gender, connect, microphone, description, games, active_timer, ban_days) VALUES ({callback.from_user.id}, 'unknown', 0, 'unknown', 'unknown', 'unknown','none', 'none', 60, 0)")
        self.save()
        await callback.message.answer(f"""База данных очищена!""")
        
    def save(self):
        self.db.commit()
        self.db.close

Users().create_db()