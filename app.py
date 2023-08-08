from flask import Flask, render_template
import sys
import os 
sys.path.append("project-2-excel-to-pdf-")
from main1 import names,result
list1=result[0]
major_functions=result[1]
causes=result[2]
img=result[3 ]
template_dir = os.path.abspath('project-2-excel-to-pdf-/templates')
app = Flask(__name__,template_folder=template_dir)
@app.route('/')
def index():
    print("yes working")
    return render_template('index_try.html', names=names)
@app.route('/output')
def output():
   return render_template('pdf_generate.html',List1=list1,function=major_functions,causes=causes,img=img)

app.run(host='0.0.0.0')