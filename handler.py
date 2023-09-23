from flask import Flask, render_template, request, redirect, url_for, flash

from app.services.UserService import UserService
from app.services.ProjectService import ProjectService

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'
app.config['WTF_CSRF_ENABLED'] = False
app.secret_key = 'SecretKey'
userService = UserService()
projectService = ProjectService()
users = []
projects =[]


@app.route('/users', methods=["GET", "POST","PUT","DELETE"])
def handle_user_request():
    if (request.method == "GET"):
        users= userService.get_users()
        return render_template('index.html',users=users)
    elif (request.method == "POST"):
        userService.add_user(request)
        return "User added successfully"
    elif (request.method == "PUT"):
        return update_user(request)
    elif (request.method == "DELETE"):
        userService.delete_user(request)
        return "User deleted successfully"


@app.route('/admin')
def handle_admin_request():
    users= userService.get_users()
    projects=projectService.get_projects()
    return render_template('admin.html', users=users , projects=projects)
    
@app.route('/user/entries', methods=["GET", "POST", "PUT", "DELETE"])
def handle_user_entries_request():
    return render_template('entries.html')
   

@app.route('/projects', methods=["POST","PUT","DELETE"])
def handle_projects_request():
    if (request.method == "POST"):
        projectService.add_project(request)
        return "Project added successfully"
    elif (request.method == "PUT"):
        return update_project(request)
    elif (request.method == "DELETE"):
        projectService.delete_project(request)
        return "Project deleted successfully"


def update_user(request):
    updated_data = request.get_json()
    userService.edit_user(request)
    for user in users:
        if user['username'] == updated_data['username']:
            user = updated_data
    return "Row updated successfully"


def update_project(request):
    updated_data = request.get_json()
    projectService.edit_project(request)
    for project in projects:
        if project['name'] == updated_data['name']:
            project = updated_data
    return "Row updated successfully"



if __name__ == '__main__':
    app.run(debug=True)
