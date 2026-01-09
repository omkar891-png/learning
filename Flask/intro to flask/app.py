#importing thr flask module in the project is mandatory
from flask import Flask
#creating an instance of the Flask class
app = Flask(__name__)
#route() function of the Flask class is a decorator
#  which tells the application which URL should call the associated function
@app.route('/')
def hello_world():
    return 'Hello, World!'  
@app.route('/about')
def about():
    return 'This is the about page.'
#run() method of Flask class runs the application on the local development server
if __name__ == '__main__':
    app.run(debug=True)