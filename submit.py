from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
  # read the existing JSON file and parse its contents
  with open('data.json', 'r') as f:
    data = json.load(f)

      # access the applications data stored in the 'applications' key of the dictionary
    applications = data['applications']

# iterate through the list of applications and print each application's data
    for application in applications:
        print(application)

  # add the form data to the dictionary
  form_data = {
    'forename': request.form['forename'],
    'surname': request.form['surname'],
    'email': request.form['email'],
    'year-of-study': request.form['year-of-study'],
    'course': request.form['course'],
    'personal-statement': request.form['personal-statement']
  }
  data['applications'].append(form_data)

  # write the updated dictionary back to the JSON