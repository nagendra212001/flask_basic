from flask import Flask,render_template
FAI=Flask(__name__)

@FAI.route('/hai')
def hai():
    return 'i am sending the string through the flask'

@FAI.route('/wish/<data>')
def wish(data):
    return  f'happy birthday {data}'

@FAI.route('/first')
def first():
    return render_template('first.html')


if __name__=='__main__':
    FAI.run(debug=True,host='192.168.43.249',port=5001)