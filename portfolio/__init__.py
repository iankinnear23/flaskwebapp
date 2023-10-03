from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/fixtures")
def fixtures():
    return render_template("fixtures.html")

@app.route("/form", methods=['GET', 'POST'])
def form_submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"Received data: Name - {name}, Email - {email}"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
