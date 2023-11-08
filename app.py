<<<<<<< HEAD
from flask import Flask, render_template, request

app = Flask(__name__)

def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

# Make a homepage
@app.route('/')
def homepage():
    return render_template('base.html', name = "Tina", aboutMe = readDetails("static/aboutMe.txt"))

@app.route('/hello/<name>')
def hello(name):
# return render_template('name.html', Sname = name) 
# The first argument is the name of the template file. In this case, it's 'name.html'. This file should be located in the templates folder.
# The second argument is a keyword argument that passes data to the template.  
    listOfNames = [name, "Yoyo", "Yennifer"]
    return render_template('name.html', Sname = name,  nameList = listOfNames) 

@app.route('/form', methods=['GET', 'POST'])
def formDemo(name = None):
    if request.method == 'POST':
        name=request.form['Sname'] # assign the name retrieved from form to name
    return render_template('form.html', name=name)


if __name__ =="__main__":
=======
from flask import Flask, render_template, request

app = Flask(__name__)

def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

# Make a homepage
@app.route('/')
def homepage():
    return render_template('base.html', name = "Tina", aboutMe = readDetails("static/aboutMe.txt"))

@app.route('/hello/<name>')
def hello(name):
# return render_template('name.html', Sname = name) 
# The first argument is the name of the template file. In this case, it's 'name.html'. This file should be located in the templates folder.
# The second argument is a keyword argument that passes data to the template.  
    listOfNames = [name, "Yoyo", "Yennifer"]
    return render_template('name.html', Sname = name,  nameList = listOfNames) 

@app.route('/form', methods=['GET', 'POST'])
def formDemo(name = None):
    if request.method == 'POST':
        name=request.form['Sname'] # assign the name retrieved from form to name
    return render_template('form.html', name=name)


if __name__ =="__main__":
>>>>>>> bd4a2d6ccbc7368663675a2d322650a0ebf6064b
    app.run(debug=True) 