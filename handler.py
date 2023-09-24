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
    if (request.method == "POST"):
        userService.add_user(request)
        return "User added successfully"
    elif (request.method == "PUT"):
        return update_user(request)
    elif (request.method == "DELETE"):
        userService.delete_user(request)
        return "User deleted successfully"
    
@app.route('/', methods=["GET"])
def handle_home_request():
    selected_user = request.cookies.get('selectedUser')
    if(selected_user):
        return handle_user_entries_request(selected_user)
    else:
        users= userService.get_users()
        return render_template('index.html',users=users)



@app.route('/admin')
def handle_admin_request():
    users= userService.get_users()
    projects=projectService.get_projects()
    users_entries=userService.get_all_users_etntries()
    return render_template('admin.html', users=users , projects=projects,users_entries=users_entries)
 
@app.route('/user/entries/<username>',methods=["GET"])   
def handle_user_entries_request(username):
    projects=projectService.get_projects()
    entries=userService.get_user_etntries(username)
    return render_template('entries.html',entries = entries , projects=projects)

@app.route('/user/entries/',methods=["POST","PUT","DELETE"])
def handle_update_user_entries_request():
    if (request.method == "POST"):
        selected_user = request.cookies.get('selectedUser')
        userService.add_user_entry(selected_user,request)
        return "User Entry is added successfully"
    elif(request.method=='PUT'):
        userService.edit_user_entry(request)
        return "User Entry is updated successfully"
    elif(request.method=='DELETE'):
        userService.delete_user_entry(request)
        return "User Entry is Deleted successfully"


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
