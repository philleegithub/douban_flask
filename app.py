from flask import Flask,render_template
import pymysql

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def home():
    return ('index.html')

@app.route('/movie')
def movie():
    datalist = []
    db = pymysql.connect(host='localhost',user='root',password='root',port=3306,charset='utf8')
    cursor = db.cursor()
    cursor.execute('use text;')
    sql = "select * from top250;"
    cursor.execute(sql)
    data = cursor.fetchall()
    for item in data:
        datalist.append(item)
    db.close()
    return render_template('movie.html',movies=datalist)

@app.route('/score')
def score():
    count = []
    sorce = []
    db = pymysql.connect(host='localhost',user='root',password='root',port=3306,charset='utf8')
    cursor = db.cursor()
    cursor.execute('use text;')
    sql = "select mark,count(mark) from top250 group by mark order by mark;"
    cursor.execute(sql)
    data = cursor.fetchall()
    for item in data:
        sorce.append(item[0])
        count.append(item[1])
    db.close()
    return render_template('score.html',count=count,sorce=sorce)

@app.route('/word')
def word():
    return render_template('word.html')

@app.route('/team')
def team():
    return render_template('team.html')


if __name__ == '__main__':
    app.run()
