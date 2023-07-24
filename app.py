import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle as pkl

app = Flask(__name__)
model = pkl.load(open('EmpRetention_model.pkl','rb'))

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
  last_evaluation = float(request.form.get('last_evaluation'))
  satisfaction = float(request.form.get('satisfaction'))
  last_evaluation_missing = 1 if last_evaluation == 0 else 0

  dept_list = ['IT','Missing','admin','engineering','finance','management','marketing','procurement','product','sales','support']
  dept = np.zeros(len(dept_list))
  dept.tolist()

  salary_list = ['high','low','medium']
  salary = np.zeros(len(salary_list))
  salary.tolist()

  index_dept = dept_list.index(request.form.get('department'))
  dept[index_dept] = 1

  index_salary = salary_list.index(request.form.get('salary'))
  salary[index_salary] = 1
  
  promoted = 1 if request.form.get('recently_promoted') == 'Yes' else 0
  complaint = 1 if request.form.get('complaint') == 'Yes' else 0

  a = [1,2,5,6]
  
  underperformer = 1 if (last_evaluation < 0.6) and (last_evaluation_missing == 0) else 0
  unhappy = 1 if satisfaction < 0.2 else 0
  overachiever = 1 if (last_evaluation > 0.8) & (satisfaction > 0.7) else 0
  hrs = float(request.form.get('hrs'))
  projects = float(request.form.get('projects'))
  tenure = float(request.form.get('tenure'))

  int_features = []
  int_features.insert(0,hrs)
  int_features.insert(1,complaint)
  int_features.insert(2,last_evaluation)
  int_features.insert(3,projects)
  int_features.insert(4,promoted)
  int_features.insert(5,satisfaction)
  int_features.insert(6,tenure)
  int_features.insert(7,last_evaluation_missing)
  int_features.insert(8,underperformer)
  int_features.insert(9,unhappy)
  int_features.insert(10,overachiever)
  int_features.extend(dept)
  int_features.extend(salary)


  int_features = np.array(int_features)

  mean = np.array([200.58,   0.14,   0.65,   3.79,   0.02,   0.62,   3.5 ,   0.1 ,
         0.29,   0.09,   0.18,   0.1 ,   0.05,   0.01,   0.19,   0.05,
         0.04,   0.06,   0.01,   0.06,   0.28,   0.15,   0.08,   0.49,
         0.43])
  std = np.array([49.86,  0.35,  0.27,  1.23,  0.14,  0.25,  1.46,  0.3 ,  0.45,
        0.29,  0.38,  0.29,  0.22,  0.11,  0.39,  0.22,  0.21,  0.23,
        0.11,  0.24,  0.45,  0.36,  0.27,  0.5 ,  0.5 ])

  int_features = (int_features-mean)/std  
  final_features = [int_features]
  prediction = model.predict(final_features)
  output = 'likely to leave' if prediction[0]==1 else 'not likely to leave'

  return render_template('index.html', prediction_text='The Employee is {}'.format(output))

if __name__ == '__main__':
  app.run(port=7000,debug=True)