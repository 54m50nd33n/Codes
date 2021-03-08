import hashlib
import secrets
import sqlite3

db = sqlite3.connect("nerd.db")
c = db.cursor()


c.execute("CREATE TABLE Users(id integer PRIMARY KEY, Fname text, Lname text, password_salt BLOB, password BLOB)")

db.commit()


salt = secrets.token_hex(50)
fname = input("Fname:")
lname = input("Lname:")
password = input("Password:")


def hash_password(password):
    password = password.encode("utf-8")
    password = password+salt.encode("utf-8")
    hash_password = hashlib.sha256(password).hexdigest()
    datas = '''INSERT INTO  Users(fname, lname, password_salt, password) VALUES(?,?,?,?)'''
    c.execute(datas, (fname, lname, salt, hash_password))
    db.commit()

hash_password(password)


def check_pass(check_passwd):
    check_passwd = check_passwd.encode("utf-8")
    c.execute('''SELECT password_salt FROM Users WHERE id=1''')
    fsalt = c.fetchone()
    for fsalt in fsalt:
        fsalt = str(fsalt)
        print("password salt stored in the database")
        print("\n", fsalt, "\n")
    check_passwd = check_passwd+fsalt.encode("utf-8")
    hash = hashlib.sha256(check_passwd).hexdigest()
    print(hash)

    c.execute('''SELECT password FROM Users WHERE id=1''')
    psalt = c.fetchone()
    for psalt in psalt:
        print("hash password stored in the database")
        print("\n", psalt, "\n")
    if hash  == psalt:
        print("###########\ncorrect_password############")
    else:
        print("###########\nIncorrect Password##########")



check_password = input("Password:")
check_pass(check_password)
