from flask import Flask, render_template, request, redirect,url_for,session
import mysql.connector
import os

app = Flask(__name__)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Pasbalis1",
    database = "SAATH"
)

mycursor = mydb.cursor()

app.secret_key = os.urandom(24)

@app.route('/')
def home_page():
    return render_template("login_signup_page.html")

@app.route('/donsignup', methods= ['POST', 'GET'])
def don_signup():
    if request.method == 'POST':
        user = request.form
        #username = user.get("username")
        uemail = user.get("don_email2")
        upassword = user.get("don_password2")
        uadd_lat = "a"
        uadd_lon = "b"
        #age = int(user.get("user_age"))
        #gender = user.get("user_gender")
        sql = "INSERT INTO donators(email, password, addr_lat, addr_lon) VALUES (%s, %s, %s, %s)"
        val = (uemail, upassword, uadd_lat, uadd_lon)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("map.html")

@app.route('/mobsignup', methods= ['POST', 'GET'])
def mob_signup():
    if request.method == 'POST':
        user = request.form
        #username = user.get("username")
        uemail = user.get("mob_email2")
        upassword = user.get("mob_password2")
        uadd_lat = "a"
        uadd_lon = "b"
        #age = int(user.get("user_age"))
        #gender = user.get("user_gender")
        sql = "INSERT INTO mobile(email, password, addr_lat, addr_lon) VALUES (%s, %s, %s, %s)"
        val = (uemail, upassword, uadd_lat, uadd_lon)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("login_signup_page.html")


@app.route('/ngosignup', methods= ['POST', 'GET'])
def ngo_signup():
    if request.method == 'POST':
        user = request.form
        #username = user.get("username")
        uemail = user.get("ngo_email2")
        upassword = user.get("ngo_password2")
        uadd = user.get("ngo_address")
        #age = int(user.get("user_age"))
        #gender = user.get("user_gender")
        sql = "INSERT INTO ngo(email, password, address) VALUES (%s, %s, %s)"
        val = (uemail, upassword, uadd)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("map.html")


@app.route('/donlogin', methods= ['POST', 'GET'])
def don_login():
    if request.method == 'POST':
        result = request.form
        uemail = result.get("don_email1")
        upass = result.get("don_password1")
        sql = "SELECT * FROM donators WHERE email= %s and password= %s;"
        mycursor.execute(sql, (uemail, upass))
        res = mycursor.fetchone()
        if res :
            # sql = "SELECT username FROM donator WHERE email= %s;"
            # mycursor.execute(sql, (uemail,))
            # res = mycursor.fetchall()
            session['user']= uemail
            return render_template("don_dashboard.html", result = session['user'])
            #flash('Logged in Succesfully..!')

        else:
            return render_template("login_signup_page.html")
            #flash('Invalid Credentials.. Please try again..!!')

@app.route('/moblogin', methods= ['POST', 'GET'])
def mob_login():
    if request.method == 'POST':
        result = request.form
        uemail = result.get("mob_email1")
        upass = result.get("mob_password1")
        sql = "SELECT * FROM mobile WHERE email= %s and password= %s;"
        mycursor.execute(sql, (uemail, upass))
        res = mycursor.fetchone()
        if res :
            # sql = "SELECT username FROM user WHERE email= %s;"
            # mycursor.execute(sql, (uemail,))
            # res = mycursor.fetchall()
            session['user']= uemail
            return render_template("mob_dashboard.html", result = session['user'])
            #flash('Logged in Succesfully..!')

        else:
            return render_template("login_signup_page.html")
            #flash('Invalid Credentials.. Please try again..!!')

@app.route('/ngologin', methods= ['POST', 'GET'])
def ngo_login():
    if request.method == 'POST':
        result = request.form
        uemail = result.get("ngo_email1")
        upass = result.get("ngo_password1")
        sql = "SELECT * FROM ngo WHERE email= %s and password= %s;"
        mycursor.execute(sql, (uemail, upass))
        res = mycursor.fetchone()
        if res :
            # sql = "SELECT username FROM user WHERE email= %s;"
            # mycursor.execute(sql, (uemail,))
            # res = mycursor.fetchall()
            session['user']= uemail
            return render_template("ngo_dashboard.html", result = res)
            #flash('Logged in Succesfully..!')

        else:
            return render_template("login_signup_page.html")
            #flash('Invalid Credentials.. Please try again..!!')






@app.route('/chat', methods = ['POST','GET'])
def chat():
    if 'user' in session:
        return render_template("chat.html", result = session['user'])
    else:
        return render_template("login_signup_page.html")



# @app.route('/confirm_pick', methods = ['POST', 'GET'])
# def confirm_pick():
#     if 'user' in session:
#         return render_template("confirm_pick.html", result = result)


@app.route('/tologin')
def tologin():
    session.pop('user', None)
    return render_template("after_logout.html")


@app.route('/map', methods = ['POST', 'GET'])
def map():
    result = request.form
    return render_template("login_signup._page.html")




# @app.route('/don_donate', methods = ['POST','GET'])
# def don_donate():
#     if 'user' in session:
#         return render_template("don_donate.html")
#     else:
#         return render_template("login_signup_page.html")

# @app.route('/donate', methods = ['POST', 'GET'])
# def donate():
#     if 'user' in session:
#         result = request.form
#         type = result.get("")
#

# @app.route('/chat', methods=['POST','GET'])
# def reviews():
#     if 'user' in session:
#         if request.method == 'POST':
#             input = request.form
#             uemail = session['user']
#             umsg = input.get("input_val")
#             sql = "INSERT INTO chat(email, msg) VALUES(%s, %s);"
#             mycursor.execute(sql, (uemail, umsg))
#             mydb.commit()
#             sql = "SELECT email, msg FROM chat;"
#             mycursor.execute(sql)
#             result = mycursor.fetchall()
#             return render_template("chat.html", result= result)
#     else:
#         return render_template("login_signup.html")

# @app.route('/load_chat', methods=['POST', 'GET'])
# def load_chat():
#     if user in session:
#         if request.method == 'GET':
#             last_chat_id = request.form.get("last_chat_id")
#             sql = "SELECT * FROM chat WHERE cid>%s;"
#             mycursor.execute(sql, (last_chat_id, ))
#             result = mycursor.fetchall()
#
#

# @app.route('/send_msg')
# def send_msg():
#     if user in session:
#
#         return render_template("reviews.html")
#     else:
#         return render_template("login_signup.html")
#


if __name__ == '__main__':
    my_ip='192.168.42.167'
    app.run(host=my_ip, port='8000', debug=True)