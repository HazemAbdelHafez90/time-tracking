import sqlite3
from flask import render_template, redirect, url_for, request, flash
from app.models.User import User
from app.models.Entry import Entry
import json
import time

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
        data = json.loads(request.data)
        name = data['name']
        username = data['username']
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


    def get_user_etntries(self,username):
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user_entries where user_name =?',(username,))
        rows = cursor.fetchall()
        entries = []
        for row in rows:
            id, project_name,user_name,time, entry_date ,comments= row
            entry = Entry(id,user_name,project_name,time, entry_date,comments)
            entries.append(entry)
        cursor.close()
        conn.close()
        return entries

    def add_user_entry(self, selected_user,request):
        data = json.loads(request.data)
        project = data['project']
        time = data['time']
        date = data['date']
        comments = data['comments']
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO user_entries (project_name, user_name , time,entry_date,comments) VALUES (?,?,?,?,?)', (project, selected_user,time,date,comments))
        conn.commit()
        cursor.close()
        conn.close()
        flash('user added successfully!', 'success')

    def edit_user_entry(self, request):
        data = json.loads(request.data)
        project = data['project']
        time = data['time']
        date = data['date']
        comments = data['comments']
        id = data['id']
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE user_entries SET  project_name=? ,time=?,entry_date=?,comments=?  WHERE entry_id = ?', (project,time,date,comments,id))
        conn.commit()
        cursor.close()
        conn.close()
        flash('user entry edited successfully!', 'success')
    
    def delete_user_entry(self, request):
        id = json.loads(request.data)['id']
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('delete from user_entries where entry_id = ?', (id,))
        conn.commit()
        cursor.close()
        conn.close()
        flash('entry deleted successfully!', 'success')

    def get_all_users_etntries(self):
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user_entries')
        rows = cursor.fetchall()
        entries = []
        for row in rows:
            id, project_name,user_name,time, entry_date ,comments= row
            entry = Entry(id,user_name,project_name,time, entry_date,comments)
            entries.append(entry)
        cursor.close()
        conn.close()
        return entries