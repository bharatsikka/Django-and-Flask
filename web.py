from flask import Flask, jsonify, abort

app = Flask(__name__)
from function_doc import geturl_doc
from function_docx import geturl_docx
import re
str = '.doc'
@app.route('/url/<path:url>', methods=['GET'])
def check(url):
    test = url.find(str)

    try:
        str2 = url.__getitem__(test + 4)
        if(str2 == 'x'):
            ob1 = geturl_docx(url)
            return jsonify(ob1)
    except:
        ob2 = geturl_doc(url)
        return jsonify(ob2)

@app.route('/add/<int:a>,<int:b>', methods=['GET'])
def add(a,b):
    a = a
    b= b
    sum = a+b
    return jsonify(a+b)



if __name__ == '__main__':
    app.run(debug=True, host='10.97.157.174')