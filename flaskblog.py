from flask import Flask, render_template,url_for
app = Flask(__name__)

posts = [
	{
		  'author':'Yaw Precious',
		  'title': 'Ghana our Home',
		  'date_posted': 'April 21, 2019',
		  'content': 'Article 1'
	
	},
	{
		  'author': 'Felix Tetteh',
		  'title': 'Kakum National Park',
		  'date_posted': 'April 22, 2019',
		  'content': 'Article 2'

	}

]





@app.route("/")
def index():
	return render_template('index.html', posts=posts)


@app.route("/about")
def about():
	return render_template('about.html', title='About')

if __name__=='__main__':
	app.run(debug=True)	