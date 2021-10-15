from flask import Flask, render_template, request,send_file
from forms import MyForm
from extract import extract_data


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
def hello_world():
    return "<p>Welcome to the App </p>"


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    default_value = '0'
    state = request.form.get('state', default_value)
    city = request.form.get('city', default_value)
    zip_code = request.form.get('zip_code', default_value)
    if(city != "" and state != "" and len(state) == 2):
        extract_data(city, state)
        return send_file("extract_df.csv",
                     mimetype='text/csv',
                     attachment_filename="extract_df.csv",
                     as_attachment=True)
    return render_template("login.html",title='Login', form=form)

