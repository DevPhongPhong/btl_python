from flask import Flask, jsonify,request, render_template
from flask_cors import CORS
import utils

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/category', methods=['GET'])    
def category():
    return render_template('category.html')

@app.route('/post', methods=['GET'])    
def postlist():
    return render_template('postlist.html')

@app.route('/post/<id>', methods=['GET'])    
def post(id):
    return render_template('post.html')

@app.route('/contact', methods=['GET'])    
def contact():
    return render_template('contact.html')

@app.route('/sumitpost', methods=['GET'])    
def submitpost():
    return render_template('submitpost.html')

# post

@app.route('/api/post', methods=['GET'])
def api_get_posts():
    return jsonify(utils.get_post())

@app.route('/api/post/<id>', methods=['GET'])
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

@app.route('/api/category/<id>', methods=['GET'])
def api_get_category(id_category):
    return jsonify(utils.get_category_by_id(id_category))

@app.route('/api/category/add',  methods = ['POST'])
def api_add_category():
    return  request.json()
    return jsonify(utils.add_category(category))
@app.route('/api/category/update',  methods = ['PUT'])
def api_update_category():
    category = request.json()
    return jsonify(utils.update_category(category))

@app.route('/api/category/delete/<id>',  methods = ['DELETE'])
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