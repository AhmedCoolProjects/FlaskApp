'''

python

virual env = pip install Virtualenv


front end = html + css

micro framework = flask => routes , jinja(blocks + basic python) , views(pages ), models(db) , templates(folder = html), static (folder = css + js + images), server local(port 3000), 

backend = python h



schema = 
  file .py (base)
  templates(folder , file .html)
  static(folder, file .css)


app.py => python file, python, python app.py, 


methods post get 
get = get data avoir data
post = post data  send data


input (data)     button (submit)    => send data (post)


page (data)   post => send data, no get => we cant desplay this page


django 

flask installation => fcts methods tools (hidden)

django => db pages (admin) pagr(auth)  page (edit delete)  pages (forms )  fcts ...
django => project = many apps 
project(store online) = apps = (auth + )
 page urls (routes)
 page views (fcts)
 page models (db)


input (content(data) => progile.html )

'''

from flask import Flask, render_template, request, session
app = Flask(__name__)
def pluss(x):
  x = int(x)
  return x*2
go = [1,2,3,2,15,15,18,48,1,418,18,5,818,5]
@app.route('/', methods=['GET','POST']) 
def home(): 
  if request.method == 'POST':
    name = request.form['name']
    age = request.form['age']
    return render_template('profile.html', age=go, name=name)
  else:
    return render_template('home.html')
if __name__ == "__main__":
 app.run(debug=True)
