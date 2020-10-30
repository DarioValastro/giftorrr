from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/contactUs/')
def contact_Us():
    return render_template('contactUs.html')


@app.route('/aboutUs/')
def about_Us():
    return render_template('aboutUs.html')

if __name__ == '__main__':
    app.run(debug=True)
