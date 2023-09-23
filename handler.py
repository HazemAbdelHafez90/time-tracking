from flask import Flask, render_template, request, redirect, url_for, flash

from app.services.UserService import UserService

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'
app.config['WTF_CSRF_ENABLED'] = False
app.secret_key = 'SecretKey'
userService = UserService()


@app.route('/users', methods=["GET", "POST", "PUT", "DELETE"])
def handle_user_request():
    if (request.method == "GET"):
        return userService.get_users()
    elif (request.method == "POST"):
        return userService.add_user(request)
    elif (request.method == "PUT"):
        return userService.edit_user(request)


@app.route('/user/entries', methods=["GET", "POST", "PUT", "DELETE"])
def handle_user_entries_request():
    return render_template('entries.html')



# @app.route('/edit/<int:id>', methods=['GET', 'POST'])
# def edit(id):
#     conn = sqlite3.connect('my_database.db')
#     cursor = conn.cursor()
#     if request.method == 'POST':
#         new_title = request.form['title']
#         new_author = request.form['author']
#         cursor.execute('UPDATE books SET title=?, author=? WHERE id=?', (new_title, new_author, id))
#         conn.commit()
#         conn.close()
#         flash('Book updated successfully!', 'success')
#         return redirect(url_for('index'))
#     cursor.execute('SELECT * FROM books WHERE id=?', (id,))
#     book = cursor.fetchone()
#     conn.close()
#     return render_template('edit.html', book=book)


# @app.route('/delete/<int:id>')
# def delete(id):
#     conn = sqlite3.connect('my_database.db')
#     cursor = conn.cursor()
#     cursor.execute('DELETE FROM books WHERE id=?', (id,))
#     conn.commit()
#     conn.close()
#     flash('Book deleted successfully!', 'success')
#     return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
