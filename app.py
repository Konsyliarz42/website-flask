from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("base.html")

@app.route('/mypage/me')
def show_me():
    return render_template("me.html")

@app.route('/mypage/contact')
def show_contact():
    return render_template("contact.html")

@app.route('/mypage/contact', methods=['POST'])
def message():
    print(request.form)
    return redirect("/mypage/contact")