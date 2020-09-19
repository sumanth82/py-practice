# create a web app, which asks user to enter a string or a word as an input in the GUI.
# Once the input is entered, it should write a file webapp.txt to the local workspace
# 

##### ALTERNATIVE SOLUTION 

import flask
from flask import *

app=Flask(__name__)

html = """

<div class="form">
<form action="{{url_for('sent')}}" method="POST">
<input title="Your email address will be safe with us." placeholder="Enter a line" type="text" name="line" required> <br>
<button class="go-button" type="submit"> Submit </button>
</form>
</div>

"""

@app.route('/')

def index():
    return render_template_string(html)

@app.route("/sent", methods=['GET', 'POST'])
def sent():
    line=None 
    if request.method=='POST':
        line = request.form['line']
        with open('user_input_flask.txt', 'a+') as file:
            file.write(line + '\n')
        return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
