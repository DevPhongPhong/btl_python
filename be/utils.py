import sqlite3
import datetime as dt
import os
from flask import request
# post

def add_post(post):
    added_post = {}
    try:
        conn = sqlite3.connect("data/database.db")
        cur = conn.cursor()
        sql = """
        INSERT INTO post(title,sub_content,full_content,main_image,image,author,
        viewcount,created_time,category,tag,id_category)
        VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cur.execute(sql,(post['title'],post['sub_content'],post['full_content'],post['main_image'],post['image'],post['author'],post['viewcount'],post['created_time'],post['category'],post['tag'],post['id_category'],))
        conn.commit()
        added_post = get_post_by_id(cur.lastrowid)
    except:
        conn().rollback()
    finally:
        conn.close()
    
    return added_post

def get_post():
    posts = []
    try:
        conn = sqlite3.connect("data/database.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM post")
        rows = cur.fetchall()
        for i in rows:
            post = {}
            post["id"] = i["id"],
            post["title"] = i["title"]
            post["sub_content"] = i["sub_content"],
            post["full_content"] = i["full_content"],
            post["main_image"] = i["main_image"],
            post["image"] = i["image"],
            post["author"] = i["author"],
            post["viewcount"] = i["viewcount"],
            post["created_time"] = i["created_time"],
            post["category"] = i["category"],
            post["tag"] = i["tag"],
            post["id_category"] = i["id_category"]
            posts.append(post)
    except:
        posts = []
    
    return posts

def get_post_by_id(id_post):
    post = {}
    try:
        conn = sqlite3.connect("data/database.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM post WHERE id = ?",(id_post,))
        row = cur.fetchone()
        post["id"] = row["id"],
        post["title"] = row["title"]
        post["sub_content"] = row["sub_content"],
        post["full_content"] = row["full_content"],
        post["main_image"] = row["main_image"],
        post["image"] = row["image"],
        post["author"] = row["author"],
        post["viewcount"] = row["viewcount"],
        post["created_time"] = row["created_time"],
        post["category"] = row["category"],
        post["tag"] = row["tag"],
        post["id_category"] = row["id_category"]
    except:
        post = {}
    
    return post

def update_post(id_post, data):
    updated_post = {}
    try:
        conn = sqlite3.connect("data/database.db")
        cur = conn.cursor()
        sql = """
        UPDATE post SET title = ?, sub_content = ?, full_content = ?, main_image = ?,
        image = ?, author = ?, viewcount = ?, created_time = ?,
        category = ?, tag = ?, id_category = ? WHERE id = ?
        """
        
        cur.execute(sql,(data["title"],data['sub_content'],data['full_content'],data['main_image'],data['image'],data['author'],data['viewcount'],data['created_time'],data['category'],data['tag'],data['id_category'],id_post,))
        conn.commit()
        updated_post = get_post_by_id(id_post)
    except:
        conn.rollback()
        updated_post = {}
    finally:
        conn.close()
        
    return updated_post

def delete_post(id_post):
    try:
        conn = sqlite3.connect("data/database.db")
        cur = conn.cursor()
        sql = """
        DELETE from post
        WHERE id = ?
        """
        cur.execute(sql,(id_post,))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

# category

def add_category(category):
    added_category = {}
    try:
        conn = sqlite3.connect("data/database.db")
        cur = conn.cursor()
        sql = """
        INSERT INTO category(name,main_image)
        VALUES(?, ?)
        """
        cur.execute(sql,(category["name"],category["main_image"],))
        conn.commit()
        added_category = get_category_by_id(cur.lastrowid)
    except:
        conn().rollback()
    finally:
        conn.close()
    
    return added_category

def get_category():
    categories = []
    try:
        conn = sqlite3.connect("data/database.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM category")
        rows = cur.fetchall()
        for i in rows:
            category = {}
            category["id"] = i["id"],
            category["name"] = i["name"],
            category["main_image"] = i["main_image"],
            categories.append(category)
    except:
        categories = []
    
    return categories

def get_category_by_id(id_category):
    category = {}
    try:
        conn = sqlite3.connect("data/database.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM category WHERE id = ?",(id_category,))
        row = cur.fetchone()
        category["id"] = row["id"],
        category["name"] = row["name"],
        category["main_image"] = row["main_image"],
    except:
        category = {}
    
    return category

def update_category(id_category, data):
    updated_category = {}
    try:
        conn = sqlite3.connect("data/database.db")
        cur = conn.cursor()
        sql = """
        UPDATE category SET name = ?, main_image = ?
        WHERE id = ?
        """
        name = data["name"]
        main_image = data["main_image"]
        
        cur.execute(sql,(name,main_image,id_category))
        conn.commit()
        updated_category = get_category_by_id(id)
    except:
        conn.rollback()
        updated_category = {}
    finally:
        conn.close()
        
    return updated_category

def delete_category(id_category):
    try:
        conn = sqlite3.connect("data/database.db")
        cur = conn.cursor()
        sql = """
        DELETE from category
        WHERE id = ?
        """
        cur.execute(sql,(id_category,))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

# Some functions

def get_three_post_latest():
    posts = []
    try:
        conn = sqlite3.connect("data/database.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM post ORDER BY created_time desc LIMIT 3")
        rows = cur.fetchall()
        for i in rows:
            post = {}
            post["id"] = i["id"],
            post["title"] = i["title"],
            post["sub_content"] = i["sub_content"],
            post["full_content"] = i["full_content"],
            post["main_image"] = i["main_image"],
            post["image"] = i["image"],
            post["author"] = i["author"],
            post["viewcount"] = i["viewcount"],
            post["created_time"] = i["created_time"],
            post["category"] = i["category"],
            post["tag"] = i["tag"],
            post["id_category"] = i["id_category"]
            posts.append(post)
    except:
        posts = []
    
    return posts

def get_three_post_random():
    posts = []
    try:
        conn = sqlite3.connect("data/database.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM post ORDER BY RANDOM() LIMIT 3")
        rows = cur.fetchall()
        for i in rows:
            post = {}
            post["id"] = i["id"],
            post["title"] = i["title"],
            post["sub_content"] = i["sub_content"],
            post["full_content"] = i["full_content"],
            post["main_image"] = i["main_image"],
            post["image"] = i["image"],
            post["author"] = i["author"],
            post["viewcount"] = i["viewcount"],
            post["created_time"] = i["created_time"],
            post["category"] = i["category"],
            post["tag"] = i["tag"],
            post["id_category"] = i["id_category"]
            posts.append(post)
    except:
        posts = []
    
    return posts

def get_five_post_highest_viewcount():
    posts = []
    try:
        conn = sqlite3.connect("data/database.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM post ORDER BY viewcount desc LIMIT 5")
        rows = cur.fetchall()
        for i in rows:
            post = {}
            post["id"] = i["id"],
            post["title"] = i["title"],
            post["sub_content"] = i["sub_content"],
            post["full_content"] = i["full_content"],
            post["main_image"] = i["main_image"],
            post["image"] = i["image"],
            post["author"] = i["author"],
            post["viewcount"] = i["viewcount"],
            post["created_time"] = i["created_time"],
            post["category"] = i["category"],
            post["tag"] = i["tag"],
            post["id_category"] = i["id_category"]
            posts.append(post)
    except:
        posts = []
    
    return posts

def get_five_category_random():
    categories = []
    try:
        conn = sqlite3.connect("data/database.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM category ORDER BY RANDOM() LIMIT 5")
        rows = cur.fetchall()
        for i in rows:
            category = {}
            category["id"] = i["id"],
            category["name"] = i["name"],
            category["main_image"] = i["main_image"],
            categories.append(category)
    except:
        categories = []
    
    return categories

def get_list_post_same_category(id_category):
    posts = []
    try:
        conn = sqlite3.connect("data/database.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        sql = """
        SELECT p.id,p.title,p.sub_content,p.full_content,p.main_image,p.image,p.author,p.viewcount,p.created_time, p.category,p.tag,p.id_category
        FROM post p INNER JOIN category c
        ON p.id_category = c.id and c.id = ?
        """
        cur.execute(sql,(id_category,))
        rows = cur.fetchall()
        for i in rows:
            post = {}
            post["id"] = i["id"],
            post["title"] = i["title"]
            post["sub_content"] = i["sub_content"],
            post["full_content"] = i["full_content"],
            post["main_image"] = i["main_image"],
            post["image"] = i["image"],
            post["author"] = i["author"],
            post["viewcount"] = i["viewcount"],
            post["created_time"] = i["created_time"],
            post["category"] = i["category"],
            post["tag"] = i["tag"],
            post["id_category"] = i["id_category"]
            posts.append(post)
    except:
        posts = []
    
    return posts

# login


if __name__ == "__main__":
    pass
