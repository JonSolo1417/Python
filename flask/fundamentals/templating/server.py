from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/hello/<string:vocab>/<string:color1>/<string:color2>')                           
def hello_world(vocab,color1,color2):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', word = vocab , number = 16, color1=color1,color2=color2)  
    

@app.route('/render_list')
def list():
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)



if __name__=="__main__":
    app.run(debug=True)                   

