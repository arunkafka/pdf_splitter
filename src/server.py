from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello():
    return "hello arun here"

if __name__=="__main__":
    app.run()