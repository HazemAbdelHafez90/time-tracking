import sqlite3
from flask import render_template, redirect, url_for, request, flash
from app.models.User import User
import json


class UserService:

    def get_users(self):
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        users = []
        for row in rows:
            username, name = row
            user = User(username, name)
            users.append(user)
        cursor.close()
        conn.close()
        return users

    def add_user(self, request):
        name = request.form['name']
        username = request.form['username']
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, username) VALUES (?, ?)', (name, username))
        conn.commit()
        cursor.close()
        conn.close()
        flash('user added successfully!', 'success')

    def edit_user(self, request):
        data = json.loads(request.data)
        name = data['name']
        username = data['username']
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET  name = ? WHERE username = ?', (name,username))
        conn.commit()
        cursor.close()
        conn.close()
        flash('user edited successfully!', 'success')
    
    def delete_user(self, request):
        username = json.loads(request.data)['username']
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('delete from users where username = ?', (username,))
        conn.commit()
        cursor.close()
        conn.close()
        flash('user deleted successfully!', 'success')

