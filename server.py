from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)
def store_data(data):
    with open('database2.csv', mode='a',newline='') as database2:
        email = data['E-mail']
        about = data['Subject']
        Text = data['Text']
        spamwriter = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([email, about, Text])
@app.route('/')
def homepage():
    return render_template("index.html")
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            store_data(data)
            return redirect('/thnku.html')
        except:
            return 'ERROR:info wasn\'t saved to database :('
    else:
        return 'Form Submission:Failed :( '
