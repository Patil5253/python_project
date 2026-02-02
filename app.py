from flask import Flask, render_template, request
from recommendation import recommend_products

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    search_product = ""

    if request.method == "POST":
        search_product = request.form.get("product")
        recommendations = recommend_products(search_product)

    return render_template(
        "index.html",
        recommendations=recommendations,
        search_product=search_product
    )

if __name__ == "__main__":
    app.run(debug=True)


