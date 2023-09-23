from flask import Flask, render_template, request, redirect, url_for, flash

from app.services.UserService import UserService

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'
app.config['WTF_CSRF_ENABLED'] = False
app.secret_key = 'SecretKey'
userService = UserService()
users = []


@app.route('/users', methods=["GET", "POST"])
def handle_user_request():
    if (request.method == "GET"):
        users= userService.get_users()
        return render_template('index.html', users=users)
    elif (request.method == "POST"):
        userService.add_user(request)
        return redirect(url_for('admin')) 


@app.route('/users/', methods=[ "PUT", "DELETE"])
def handle_update_user_request():
    if (request.method == "PUT"):
        return update_user(request)
    elif (request.method == "DELETE"):
        userService.delete_user(request)
        return "Row deleted successfully"



@app.route('/user/entries', methods=["GET", "POST", "PUT", "DELETE"])
def handle_user_entries_request():
    return render_template('entries.html')


   
def update_user(request):
    updated_data = request.get_json()
    userService.edit_user(request)
    for user in users:
        if user['username'] == updated_data['username']:
            user = updated_data
    return "Row updated successfully"



if __name__ == '__main__':
    app.run(debug=True)
