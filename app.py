from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime   # Import datetime module to get the current date and time


app = Flask(__name__)

# SQLite Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoid unnecessary warnings

db = SQLAlchemy(app)

# Define a User Model
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno}{self.title}"
    
@app.route('/', methods=['GET','POST'])
def hellp_world():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo=Todo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
        
    aLLTodo=Todo.query.all()
    return render_template('index.html',aLLTodo=aLLTodo)

@app.route('/show')
def products():
    aLLtodo=Todo.query.all()
    print(aLLtodo)
    return 'Hello, World!'


# Create Database and Tables
with app.app_context():
    db.create_all()
    print("Database and tables created!")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
