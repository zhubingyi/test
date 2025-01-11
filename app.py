from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 用列表临时存储描述（实际应用中应该使用数据库）
descriptions = []

# 前台展示页面
@app.route('/')
def front_page():
    return render_template('front.html', descriptions=descriptions)

# 后台管理页面
@app.route('/admin')
def admin_page():
    return render_template('admin.html', descriptions=descriptions)

# 后台添加描述的处理
@app.route('/admin/add', methods=['POST'])
def add_description():
    if request.method == 'POST':
        description = request.form.get('description')
        if description:
            descriptions.append(description)
    return redirect(url_for('admin_page'))

if __name__ == '__main__':
    app.run(debug=True) 