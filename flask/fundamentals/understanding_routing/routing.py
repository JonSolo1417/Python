from flask import Flask
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def sayHello():
    print('says hello world')
    return 'Hello World!'

@app.route('/dojo')
def sayDojo():
    print('says dojo')
    return 'Dojo'

@app.route('/say/<string:name>')
def sayName(name):
    print('says hello name')
    return 'Hello ' + name

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num,word):
    print ('repeats num times')
    return (word +" ")* int(num)

@app.errorhandler(404)
def notFound(e):
    return 'Page not found yo'





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.