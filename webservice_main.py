
from flask import Flask, jsonify, abort

app = Flask(__name__)
from function_doc import geturl_doc
from function_docx import geturl_docx
@app.route('/url/<path:url>', methods=['GET'])
def check(url):
    attr = url[-3:]
    if attr == 'doc':
        ob1 = geturl_doc(url)
    elif attr == 'ocx':
        ob2 = geturl_docx(url)
        
        
        if str(url).__contains__('docx'):
            ob1 = geturl_docx(url)
            return jsonify(ob1)
            return jsonify('This is a docx file')
    if str(url).__contains__('doc'):
         ob2 = geturl_doc(url)
         return jsonify(ob2)
         return jsonify('this is a doc file')
    elif attr == 'lsx':
         ob1 = geturl_xlsx(url)
         return jsonify(ob1)
    elif attr == 'ptx':
         ob1 = geturl_pptx(url)
         return jsonify(ob1)
    elif attr == 'xls':
         ob1 = geturl_xls(url)
         return jsonify(ob1)
    elif attr == 'ppt':
         ob1 = geturl_ppt(url)
         return jsonify(ob1)

if __name__ == '__main__':
    app.run(debug=True, host='10.97.157.174')

