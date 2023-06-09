from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', title='Home')
  

@app.route('/about')
def about():
  return render_template('about.html', title='About')
  

@app.route('/form', methods=['GET', 'POST'])
def form():
    name = None
    Class = None
    email = None
    house = None
    message = None
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        Class = request.form.get('Class')
        house = request.form.get('house')
        message = request.form.get('message')
        with open('data.txt', 'a') as file:
          file.write(name + ' ' + Class + ' '+ email + ' ' + house + ' ' + message + '\n')
        return render_template('thankyou.html', title='Thank You', name=name, email=email, Class=Class, house=house, message=message)
    return render_template('form.html', title='Feedback Form')
    

app.run(host='0.0.0.0', port=81)
