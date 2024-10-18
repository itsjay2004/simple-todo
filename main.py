from flask import Flask, render_template
app=Flask(__name__)

# # This is because jinja's and vue's delimiter is clasing "{{ }}" 
# # So changed the jinja's delimiter from "{{ 'variable' }}" to "[[ 'variable' ]]" 
# app.jinja_env.variable_start_string = '[['
# app.jinja_env.variable_end_string = ']]'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<name>')
def hello(name):
    text = f"hwllo there {name}"
    return text

@app.route('/python/<int:id>')
def python(id):
    text = f"the number is {id}"
    return text

@app.route('/admin')
def hello_admin():
    return "Hello ADMIN"

@app.route('/guest/<guest>')
def hello_guest(guest):
   return f'Hello {guest} as Guest'

@app.route('/result/<int:marks>')
def result(marks):
    return render_template("result.html", marks=marks)



app.run(debug=True)