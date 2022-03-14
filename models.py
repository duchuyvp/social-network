import sqlite3
from os import path

ROOT = path.dirname(path.abspath(__file__))


def create_post(name, post):
    conn = sqlite3.connect(path.join(ROOT, "database.db"))
    c = conn.cursor()
    c.execute("INSERT INTO posts (name, content) VALUES (?, ?)", (name, post))
    conn.commit()
    conn.close()


def get_posts():
    conn = sqlite3.connect(path.join(ROOT, "database.db"))
    c = conn.cursor()
    c.execute("SELECT * FROM posts")
    posts = c.fetchall()
    conn.close()
    return posts
