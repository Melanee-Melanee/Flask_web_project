from datetime import datetime
from flask import Flask,render_template,request,redirect
from models import db, EmployeeModel
from datetime import datetime

app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()
 
@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html', datetime_ = datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))

@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html') #'createpage.html')
 
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['fullname']
        age = request.form['age']
        position = request.form['position']
        # print(type(eval(employee_id)), type(eval(age)))
        try:
            if type(eval(employee_id)) is int and type(eval(age)) is int:
                employee = EmployeeModel(employee_id=employee_id, name=name, age=age, position = position)
                db.session.add(employee)
                db.session.commit()
                return redirect('/data')
        except:            
            return render_template('createpage.html') #'createpage.html')
 

@app.route('/data') 
def RetrieveList():
    employees = EmployeeModel.query.all()
    return render_template('datalist.html',employees = employees)
 
 
@app.route('/data/<int:id>')
def RetrieveEmployee(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if employee:
        return render_template('data.html', employee = employee)
    return f"Employee with id ={id} Doenst exist"
 
 
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            name = request.form['fullname']
            age = request.form['age']
            position = request.form['position']
            employee = EmployeeModel(employee_id=id, name=name, age=age, position = position)
            db.session.add(employee)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Employee with id = {id} Does nit exist"
 
    return render_template('update.html', employee = employee)
 
 
@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')
 
if __name__ == '__main__':
    app.run(debug=True)#, host='localhost', port=5000) # 


