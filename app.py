from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load Model
with open("models/disaster_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load Vectorizer
with open("models/tfidf_vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    tweet = request.form["tweet"]

    tweet_vector = vectorizer.transform([tweet])
    prediction = model.predict(tweet_vector)

    if prediction[0] == 1:
        result = "🚨 Disaster Tweet"
    else:
        result = "✅ Not a Disaster Tweet"

    return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)