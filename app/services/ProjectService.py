import sqlite3
from flask import render_template, redirect, url_for, request, flash
from app.models.Project import Project
import json


class ProjectService:

    def get_projects(self):
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM projects')
        rows = cursor.fetchall()
        projects = []
        for row in rows:
            name, desc = row
            project = Project(name, desc)
            projects.append(project)
        cursor.close()
        conn.close()
        return projects

    def add_project(self, request):
        data = json.loads(request.data)
        name = data['name']
        desc = data['desc']
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO projects (name, desc) VALUES (?, ?)', (name, desc))
        conn.commit()
        cursor.close()
        conn.close()
        flash('project added successfully!', 'success')

    def edit_project(self, request):
        data = json.loads(request.data)
        name = data['name']
        desc = data['desc']
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE projects SET  desc = ? WHERE name = ?', (desc,name))
        conn.commit()
        cursor.close()
        conn.close()
        flash('project edited successfully!', 'success')
    
    def delete_project(self, request):
        name = json.loads(request.data)['name']
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('delete from projects where name = ?', (name,))
        conn.commit()
        cursor.close()
        conn.close()
        flash('project deleted successfully!', 'success')

