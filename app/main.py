import os


from flask import Flask, request, redirect, render_template, session, url_for, g

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='devIAm')  # Needed for session tracking
  # Note flask does CLIENT session data storage!  Watch data sizes!


@app.route('/', methods=['GET','POST'])
def calculate():
  t = {'r': 0, 'c': 0}   # josh
  if request.method == 'POST':
    t['a'] = request.form['a']
    t['b'] = request.form['b']
  elif 'a' in request.args:
    t['a'] = request.args.get('a')
    t['b'] = request.args.get('b') 
  row = int(t['b'])
  col = int(t['a'])


  # Update the number of visits
  # session is a dict which persists.  Stored in client cookie (no local storage)

  return render_template('index.html', t = t, rows = row, cols = col) # Send t to the template

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Enable on all devices so Docker works!