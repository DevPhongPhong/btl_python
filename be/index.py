from flask import Flask, jsonify,request, render_template,session
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import utils,sqlite3,psycopg2,psycopg2.extras

app = Flask(__name__)
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

@app.route('/submitpost', methods=['GET'])    
def submitpost():
    return render_template('submitpost.html')

@app.route('/error', methods=['GET'])    
def error():
    return render_template('404.html')

@app.route('/admin/login', methods=['GET'])    
def adminlogin():
    return render_template('adminlogin.html')

@app.route('/admin/home', methods=['GET'])    
def adminhome():
    return render_template('adminhome.html')

# post

@app.route('/api/post', methods=['GET'])
def api_get_posts():
    return jsonify(utils.get_post())

@app.route('/api/post/<int:id_post>', methods=['GET'])
def api_get_post(id_post):
    return jsonify(utils.get_post_by_id(id_post))

@app.route('/api/post/add',  methods = ['POST'])
def api_add_post():
    post = request.json()
    return jsonify(utils.add_post(post))
@app.route('/api/post/update',  methods = ['PUT'])
def api_update_post():
    post = request.json()
    return jsonify(utils.update_post(post))

@app.route('/api/post/delete/<id>',  methods = ['DELETE'])
def api_delete_post(id_post):
    return jsonify(utils.delete_post(id_post))

# category

@app.route('/api/category', methods=['GET'])
def api_get_categories():
    return jsonify(utils.get_category())

@app.route('/api/category/<int:id_category>', methods=['GET'])
def api_get_category(id_category):
    return jsonify(utils.get_category_by_id(id_category))

@app.route('/api/category/add',  methods = ['POST'])
def api_add_category():
    category = request.json()
    return jsonify(utils.add_category(category))
@app.route('/api/category/update',  methods = ['PUT'])
def api_update_category():
    category = request.json()
    return jsonify(utils.update_category(category))

@app.route('/api/category/delete/<int:id_category>',  methods = ['DELETE'])
def api_delete_category(id_category):
    return jsonify(utils.delete_category(id_category))

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
@app.route('/api/check')
def home():
    passhash = generate_password_hash('admin')
    print(passhash)
    if 'username' in session:
        username = session['username']
        return jsonify({'message' : 'You are already logged in', 'username' : username})
    else:
        resp = jsonify({'message' : 'Unauthorized'})
        resp.status_code = 401
        return resp
  
@app.route('/api/login', methods=['POST'])
def login():
    conn = sqlite3.connect("data/database.db")
    _json = request.json()
    _username = _json['username']
    _password = _json['password']
    print(_password)
    # validate the received values
    if _username and _password:
        #check user exists          
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
          
        sql = "SELECT * FROM useraccount WHERE username=%s"
          
        cursor.execute(sql, (username,))
        row = cursor.fetchone()
        username = row['username']
        password = row['password']
        if row:
            if check_password_hash(password, _password):
                session['username'] = username
                cursor.close()
                return jsonify({'message' : 'You are logged in successfully'})
            else:
                resp = jsonify({'message' : 'Bad Request - invalid password'})
                resp.status_code = 400
                return resp
    else:
        resp = jsonify({'message' : 'Bad Request - invalid credendtials'})
        resp.status_code = 400
        return resp
          
@app.route('/api/logout',methods=["GET"])
def logout():
    if 'username' in session:
        session.pop('username', None)
    return jsonify({'message' : 'You successfully logged out'})

if __name__ == "__main__":
    app.run(debug=True)