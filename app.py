from flask import Flask, render_template, request
from predict import predict_image
import os

app = Flask(__name__, static_folder="static")

UPLOAD_FOLDER = "static/upload"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)

            label, confidence = predict_image(file_path)
            return render_template("index.html", image=file_path, label=label, confidence=confidence)

    return render_template("index.html", image=None)

if __name__ == "__main__":
    app.run(debug=True)
