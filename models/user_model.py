import os
import sqlite3

class UserModel:
    DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'users.db'))

    @staticmethod
    def get_connection():
        return sqlite3.connect(UserModel.DB_PATH)


    @staticmethod
    def create_user(name, email, password):
        conn = UserModel.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_users():
        conn = UserModel.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return users

    @staticmethod
    def get_user_by_id(user_id):
        conn = UserModel.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        return user

    @staticmethod
    def get_user_by_email(email):
        conn = UserModel.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()
        return user

    @staticmethod
    def update_user(user_id, data):
        conn = UserModel.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (data['name'], data['email'], user_id))
        conn.commit()
        conn.close()
        return UserModel.get_user_by_id(user_id)

    @staticmethod
    def delete_user(user_id):
        conn = UserModel.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()
        return True if cursor.rowcount > 0 else False

    @staticmethod
    def search_users_by_name(name):
        conn = UserModel.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
        users = cursor.fetchall()
        conn.close()
        return users
