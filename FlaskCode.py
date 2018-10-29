from flask import Flask, render_template

app = Flask(__name__) #name of program pulled from the name of the file

@app.route('/')  #I can follow route if I know what to do if people land there.
def hello():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1 style="color:purple">About Us</h1>'

app.run()('0.0.0.0') #makes you accessible via your ip address and loopback

#bootstrap helps make it look better