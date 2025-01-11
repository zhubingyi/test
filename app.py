from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 用列表临时存储商品（实际应用中应该使用数据库）
products = []

# 前台展示页面 - 商品列表
@app.route('/')
def front_page():
    return render_template('front.html', products=products)

# 前台商品详情页
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    if 0 <= product_id < len(products):
        product = products[product_id]
        return render_template('product_detail.html', product=product)
    return redirect(url_for('front_page'))

# 后台管理页面
@app.route('/admin')
def admin_page():
    return render_template('admin.html', products=products)

# 后台添加商品
@app.route('/admin/add', methods=['POST'])
def add_product():
    if request.method == 'POST':
        product = {
            'name': request.form.get('name', ''),
            'price': float(request.form.get('price', 0)),
            'image_url': request.form.get('image_url', ''),
            'description': request.form.get('description', ''),
            'detail': request.form.get('detail', '')
        }
        products.append(product)
    return redirect(url_for('admin_page'))

if __name__ == '__main__':
    app.run(debug=True) 