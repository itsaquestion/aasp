from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)

classes = ["金融1班", "金融2班", "电商师1班", "电商师2班"]

@app.route('/')
def index():
    return render_template('index.html', classes=classes)


import re

def secure_filename_custom(filename):
    # 允许字母、数字、下划线和中文字符
    filename = re.sub(r'[^a-zA-Z0-9_\u4e00-\u9fa5]', '', filename)
    return filename

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    student_id = request.form['student_id']
    student_name = request.form['student_name']
    
    # 获取原文件的扩展名并保留
    _, file_extension = os.path.splitext(file.filename)
    
    # 使用自定义的secure_filename_custom函数
    filename = f'{secure_filename_custom(student_id)}_{secure_filename_custom(student_name)}{file_extension}'
    
    class_name = request.form['class_name']
    
    # 创建 'submissions/班级/<日期>' 文件夹
    date_str = datetime.now().strftime('%Y%m%d')
    submission_path = os.path.join('submissions', class_name, date_str)
    if not os.path.exists(submission_path):
        os.makedirs(submission_path)
    
    # 保存文件到指定文件夹
    file.save(os.path.join(submission_path, filename))
    return "File uploaded successfully"

if __name__ == '__main__':
    app.run(debug=True)
