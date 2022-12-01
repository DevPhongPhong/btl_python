from flask import Flask, jsonify,request, render_template,session,redirect, url_for
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import utils,sqlite3,psycopg2,psycopg2.extras
 
app = Flask(__name__)
app.secret_key = 'any random string'
CORS(app, resources={r"/*": {"origins": "*"}})
 
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
 
@app.route('/category', methods=['GET'])    
def category():
    return render_template('category.html')
 
@app.route('/category/<id>', methods=['GET'])    
def postListByCategoryId(id):
    return render_template('postlist.html')
 
@app.route('/post', methods=['GET'])    
def postlist():
    return render_template('postlist.html')
 
@app.route('/post/<id>', methods=['GET'])    
def post(id):
    return render_template('post.html')
 
@app.route('/contact', methods=['GET'])    
def contact():
    return render_template('contact.html')
 
@app.route('/admin/submitpost', methods=['GET'])    
def submitpost():
    if 'username' in session:
        return render_template('submitpost.html')
    else:
        return redirect(url_for('adminlogin'))
    

@app.route('/admin/submitcategory', methods=['GET'])    
def submitcategory():
    if 'username' in session:
        return render_template('submitcategory.html')
    else:
       return redirect(url_for('adminlogin'))
    

@app.route('/admin/changecategory/<id>', methods=['GET'])    
def changecategory(id):
    if 'username' in session:
        return render_template('changecategory.html')
    else:
        return redirect(url_for('adminlogin'))
   

@app.route('/admin/changepost/<id>', methods=['GET'])    
def changepost(id):
    if 'username' in session:
        return render_template('changepost.html')
    else:
        return redirect(url_for('adminlogin'))
    

@app.route('/error', methods=['GET'])    
def error():
    return render_template('404.html')
 
@app.route('/admin/login', methods=['GET'])    
def adminlogin():
    if 'username' not in session:
        return render_template('adminlogin.html')
    else:
        return redirect(url_for('adminindex'))

@app.route('/admin/home', methods=['GET'])    
def adminindex():
    if 'username' in session:
        return render_template('adminindex.html')
    else:
        return redirect(url_for('adminlogin'))
    



# post
 
@app.route('/api/post', methods=['GET'])
def api_get_posts():
    return jsonify(utils.get_post())
 
@app.route('/api/post/<int:id_post>', methods=['GET'])
def api_get_post(id_post):
    return jsonify(utils.get_post_by_id(id_post))
 
@app.route('/api/post/add',  methods = ['POST'])
def api_add_post():
    if 'username' in session:
        post = request.json
        return jsonify(utils.add_post(post))
    else:
        resp = jsonify({'message' : 'Unauthorized'})
        resp.status_code = 401
        return resp
@app.route('/api/post/update/<int:id_post>',  methods = ['PUT'])
def api_update_post(id_post):
    if 'username' in session:
        data = request.json
        return jsonify(utils.update_post(id_post,data))
    else:
        resp = jsonify({'message' : 'Unauthorized'})
        resp.status_code = 401
        return resp
 
@app.route('/api/post/delete/<int:id_post>',  methods = ['DELETE'])
def api_delete_post(id_post):
    if 'username' in session:
        return jsonify(utils.delete_post(id_post))
    else:
        resp = jsonify({'message' : 'Unauthorized'})
        resp.status_code = 401
        return resp
 
# category
 
@app.route('/api/category', methods=['GET'])
def api_get_categories():
    return jsonify(utils.get_category())
 
@app.route('/api/category/<int:id_category>', methods=['GET'])
def api_get_category(id_category):
    return jsonify(utils.get_category_by_id(id_category))
 
@app.route('/api/category/add',  methods = ['POST'])
def api_add_category():
    if 'username' in session:
        print(request.json)
        category = request.json
        return jsonify(utils.add_category(category))
    else:
        resp = jsonify({'message' : 'Unauthorized'})
        resp.status_code = 401
        return resp
@app.route('/api/category/update/<int:id_category>',  methods = ['PUT'])
def api_update_category(id_category):
    if 'username' in session:
        data = request.json
        return jsonify(utils.update_category(id_category, data))
    else:
        resp = jsonify({'message' : 'Unauthorized'})
        resp.status_code = 401
        return resp
 
@app.route('/api/category/delete/<int:id_category>',  methods = ['DELETE'])
def api_delete_category(id_category):
    if 'username' in session:
        return jsonify(utils.delete_category(id_category))
    else:
        resp = jsonify({'message' : 'Unauthorized'})
        resp.status_code = 401
        return resp
 
# Some functions
 
@app.route('/api/post/get-three-post-latest',methods=['GET'])
def api_get_three_post_latest():
    return jsonify(utils.get_three_post_latest())
 
@app.route('/api/post/get-three-post-random',methods=['GET'])
def api_get_three_post_random():
    return jsonify(utils.get_three_post_random())
 
@app.route('/api/post/get-five-post-highest-viewcount',methods=['GET'])
def api_get_five_post__highest_viewcount():
    return jsonify(utils.get_five_post_highest_viewcount())
 
@app.route('/api/post/get-five-category-random',methods=['GET'])
def api_get_five_category_random():
    return jsonify(utils.get_five_category_random())
 
@app.route('/api/post/category/<int:id_category>', methods=['GET'])
def api_get_list_post_same_category(id_category):
    return jsonify(utils.get_list_post_same_category(id_category))
 
#login
 
@app.route('/api/logged')
def home():
    if 'username' in session:
        username = session['username']
        return jsonify({'message' : 'You are already logged in', 'username' : username})
    else:
        resp = jsonify({'message' : 'Unauthorized'})
        resp.status_code = 401
        return resp
 
@app.route('/api/login',methods = ["POST"])
def login():
    print('11111111111111111111111111111')
    data = request.json
    username = data['username']
    password = data['password']
    conn = sqlite3.connect("data/database.db")
    cur = conn.cursor()
    sql = """
    SELECT 
    username, password
    FROM user
    WHERE username = ? and password = ?
    """
    cur.execute(sql,(username,password))
    row = cur.fetchone()
    if row is None :
        return jsonify({'message': 'Bad Request - invalid password'})
    else:
        session['username'] = username
        return jsonify({'message': 'You are logged in successfully'})
 
@app.route('/api/logout',methods=["GET"])
def logout():
    if 'username' in session:
        session.pop('username', None)
    return jsonify({'message' : 'You successfully logged out'})
 
 
# test
@app.route('/api/test',methods=['GET'])
def testget():
    return "hello"
 
@app.route('/api/test/<id>',methods=['GET'])
def testgetid(id):
    return id
 
@app.route('/api/test',methods=['POST'])
def testpost():
    return request.json   
 
if __name__ == "__main__":
    app.run(debug=True)