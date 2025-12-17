from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Here you would typically send an email or save to database
        # For this portfolio, we'll just flash a success message
        flash(f"Thank you {name}! Your message has been received.", "success")
        return redirect(url_for('index', _anchor='contact'))

if __name__ == '__main__':
    app.run(debug=True)
