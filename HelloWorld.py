from flask import Flask
#Just Wrote a basic python code to test whether flask was working or not 
#Had no prior experience in MySqlServer and all
Myapp = Flask(__name__)

@Myapp.route("/")
def helloWorld():
    return "Hello World!"

if (__name__ == "__main__"):
     Myapp.run(port = 5000)


