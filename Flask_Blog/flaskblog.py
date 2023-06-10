from flask import Flask, render_template
app = Flask(__name__) # setting app to an instance of a Flask class
# __name__ is a special variable in python, just a name of the module
# __name__ will be equal to __main__

posts = [
    {
        'author': 'Chan Woo Song',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/") # decorator: adding functionalities to existing
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

# when you run this script here, "flaskblog.py", it will be '__main__'
# if you import this script somewhere else and run it, 
# it will not be '__main__'
if __name__ == '__main__': 
    app.run(debug=True)
    
    