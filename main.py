from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)

# In case a session need to be implemented
random_byte = bytes(str(datetime.now().timestamp()), 'ascii')
app.config['SECRET_KEY'] = random_byte


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dynamic_route/<id_num>")
def dynamic_route(id_num):
    return render_template("dynamic-route-example.html", num=id_num)


@app.route("/template_form")
def template_form():
    return render_template("template-form.html")


@app.route("/template_form/post", methods=['POST'])
def template_form_post():
    form = request.form
    something = form.get('typeSomething')
    print(something)
    flash(something)
    return redirect(url_for('template_form'))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
