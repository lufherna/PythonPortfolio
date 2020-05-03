from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

# you can pass username to function below
@app.route('/index.html')
def hello_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# function that will write data to a txt file of our choice
def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
# data has to be passed in as a list
		csv_writer.writerow([email,subject,message])

# new route that'll help us with the contact page
# get means the browser wants to send info
# post
# the request.form.to_dict() creates a dictionary with all our info
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	try:
	    	data = request.form.to_dict()
	    	print(data)
	    	write_to_csv(data)
	    	return redirect('/thankyou.html')
	    # except:
	    # 	return 'Did not Save correctly'
	else:
	   	return 'Something went wrong. Try again though'