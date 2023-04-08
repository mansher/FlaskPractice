from flask import Flask
app =  Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route('/drinks')
def getDrinks():
    return {'drinks':"drinks data"}




if __name__=='__main__':
    app.run()