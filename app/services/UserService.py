import sqlite3
from flask import render_template, redirect, url_for, request, flash
from app.models.User import User


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
        conn.close()
        return render_template('index.html', users=users)

    def add_user(self, request):
        name = request.form['name']
        username = request.form['username']
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, username) VALUES (?, ?)', (name, username))
        conn.commit()
        conn.close()
        flash('user added successfully!', 'success')
        return redirect(url_for('index'))

    def edit_user(self, request):
        name = request.form['name']
        username = request.form['username']
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE user SET username = ?, name = ? WHERE id = ?', (username, name, username))
        conn.commit()
        conn.close()
        flash('user added successfully!', 'success')
        return redirect(url_for('index'))
