from flask import Flask, render_template, request # type: ignore
from converter import text_to_morse

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_text = request.form.get("user_text", "")
        morse_result = text_to_morse(user_text)
        return render_template("index.html", user_text=user_text, morse_result=morse_result)
    return render_template("index.html", user_text="", morse_result="")

if __name__ == "__main__":
    app.run(debug=True)
