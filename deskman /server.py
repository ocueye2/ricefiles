from flask import Flask, render_template, request, jsonify
import os

<<<<<<< HEAD
os.chdir("/home/ocueye/deskman")

app = Flask(__name__,"/static","static")
=======
<<<<<<< HEAD
<<<<<<< HEAD
os.chdir("/home/ocueye/deskman")

app = Flask(__name__,"/static","static")
=======
app = Flask(__name__)
>>>>>>> parent of f8d2921 (major updates)
=======
app = Flask(__name__)
>>>>>>> parent of f8d2921 (major updates)
>>>>>>> 01a4eca (fixed merge)

ITEMS = os.listdir("desktop")

print(ITEMS)

@app.route("/")
def index():
    return render_template("index.html", items=ITEMS)

@app.route("/select", methods=["POST"])
def select():
    data = request.json
    selected = data.get("item")
    if selected:
        print(f"Running: {selected}")
        with open(os.path.join("desktop",selected,"run")) as f:

            os.system(f"{f.read()} &")  # Run in background
    return jsonify({"status": "ok", "selected": selected})

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=False,port=2050)
=======
<<<<<<< HEAD
<<<<<<< HEAD
    app.run(debug=False,port=2050)
=======
    app.run(debug=True)
>>>>>>> parent of f8d2921 (major updates)
=======
    app.run(debug=True)
>>>>>>> parent of f8d2921 (major updates)
>>>>>>> 01a4eca (fixed merge)
