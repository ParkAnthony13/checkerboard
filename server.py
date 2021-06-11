from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',rows=8, cols=8)

@app.route('/4')
def four():
    return render_template('index.html',rows=4, cols=8)

@app.route('/<int:height>/<int:length>')
def custom(height, length):
    return render_template('index.html',rows=height, cols=length)

@app.route('/<int:height>/<int:length>/<light>/<dark>')
def custom_color(height, length, light, dark):
    return render_template('index.html',rows=height, cols=length, color1=light, color2=dark)

if __name__=="__main__":
    app.run(debug=True)