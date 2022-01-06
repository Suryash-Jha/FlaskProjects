from flask import Flask, render_template, url_for, redirect, request
app= Flask(__name__)
@app.route("/count")
def index():
    f= open("count.txt", "r")
    count=int(f.read())
    f.close()

    count+=1

    f= open("count.txt", "w")
    f.write(str(count))
    f.close()

    return render_template("count.html", count=count)
@app.route("/")
def hey():
	# return "Hello"
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)