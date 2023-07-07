from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

app.secret_key = 'i have no enemies'

@app.route('/')
def index():
    if 'key' in session:
        print('key exists')
        session['key'] += 1
        print(session['key'])
    else: 
        session['key'] = 1
        print(session['key'])
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def loop():
    session['key'] += 1
    return redirect('/')

@app.route('/destroy_session', methods = ['POST'])
def eat_cookies():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)