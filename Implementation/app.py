from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_field_name(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

@app.route('/', methods=['GET'])
def index():
    honeypot_name = generate_field_name()
    return render_template('index.html', honeypot_name=honeypot_name)

@app.route('/submit', methods=['POST'])
def submit():
    honeypot_name = request.form.get('honeypot_name')
    honeypot_value = request.form.get(honeypot_name)
    fake_field = request.form.get('fake_field')
    checkbox = request.form.get('trap_checkbox')
    bot_textbox = request.form.get('bot_textbox')
    time_taken = int(request.form.get('start_time') or 0)

    if honeypot_value or fake_field or checkbox or bot_textbox:
        return render_template("index.html", message="❌ Form blocked: Bot behavior detected", success=False, honeypot_name=generate_field_name())
    elif time_taken < 3000:
        return render_template("index.html", message="❌ Form blocked: Submitted too quickly", success=False, honeypot_name=generate_field_name())
    else:
        return render_template("index.html", message="✅ Form submitted successfully!", success=True, honeypot_name=generate_field_name())

if __name__ == '__main__':
    app.run(debug=True)
