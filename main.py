import datetime
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://ninopowski:nnikojdrug@newcluster.xdhrr.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE")
app.db = client.db1


#entries = []

@app.route("/", methods=["GET", "POST"])
def home():
    posts = app.db.MicroBlog.find({})
    if request.method == "POST":
        title = request.form["title"]
        text = request.form["field"]
        date = datetime.datetime.now().strftime("%b %Y")
        new_entry = {
            "title": title,
            "text": text,
            "date": date
        }
        #entries.append(new_entry)
        app.db.MicroBlog.insert_one(new_entry)
        return redirect(url_for('home'))
    return render_template("index.html", posts=posts)



if __name__ == "__main__":
    app.run(debug=True)