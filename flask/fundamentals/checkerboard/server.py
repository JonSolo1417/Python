from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/')                           
def index():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', row=8, col = 8, col1='blue', col2='red')  

@app.route('/<int:num>')  
def row(num):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', row=num, col = 8, col1='blue', col2='red')   
    
@app.route('/<int:row>/<int:col>')  
def rowCol(row,col):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', row=row, col = col, col1='blue', col2='red') 

@app.route('/<int:row>/<int:col>/<string:col1>/<string:col2>')  
def sizeAndColor(row,col,col1,col2):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', row=row, col = col, col1=col1,col2=col2)  
    
if __name__=="__main__":
    app.run(debug=True)         