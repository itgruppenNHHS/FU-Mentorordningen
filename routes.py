from flask import Flask, render_template, request
from flask_mail import Mail, Message
from forms import ContactForm


# Ha en keys.gitignore fil med google app-password i mappa
keys = []
with open("keys.gitignore", "r") as f:
    for line in f:
        keys.append(line[:-1])
    f.close()

app = Flask(__name__)
app.secret_key = keys[0]

# add mail server config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'aae.joachim@gmail.com'
app.config['MAIL_PASSWORD'] = keys[0]

mail = Mail(app)

@app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            return 'Please fill in all fields <p><a href="/contact">Try Again!!!</a></p>'
        else:
            msg = Message("Anonym Postkasse: " + form.emne.data,
                          sender='NHHS-Postkasse@nhhs.no',
                          recipients=['anders.dovran@gmail.com', 'aae.joachim@gmail.com', 'Mari.ls96@hotmail.com', 'fridhelenhop@hotmail.com'])
            msg.body = """
            Emne: %s,
            Melding: %s
            """ % (form.emne.data, form.message.data)
            mail.send(msg)
            return "Successfully  sent message!"
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)