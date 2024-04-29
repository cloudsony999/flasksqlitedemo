from flask import Flask, render_template,request
import sqlite3 as s

conn=s.connect('students.sqlite',check_same_thread=False)

cur=conn.cursor()
app=Flask(__name__)

@app.route("/")
def call():
    return render_template('data.html')

@app.route("/db")
def process():
    name=request.args.get("n")
    sub=request.args.get("s")
    dur=int(request.args.get("d"))
    ph=int(request.args.get("p"))
    cur.execute("insert into entry values(?,?,?,?)",(name,sub,dur,ph))
    conn.commit()
    return "<body bgcolor='yellow' text='red'><h1><center>Data Entry complete</center></h1></body>"

if __name__=='__main__':
    app.run(debug=True)


    