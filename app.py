from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to store tasks
todo_list = []

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list, enumerate=enumerate)  # Pass enumerate to template

# Route for adding a new task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        todo_list.append(task)
    return redirect(url_for('index'))

# Route for deleting a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(todo_list):
        todo_list.pop(task_id)
    return redirect(url_for('index'))

# Route for marking task as completed
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(todo_list):
        todo_list.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)