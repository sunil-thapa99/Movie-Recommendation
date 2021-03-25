from flask import Flask, request, render_template, send_from_directory, jsonify
import spacy

app = Flask(__name__)

@app.route("/test", methods=["POST"])
def test():
    input_data = request.form['review']
    loaded_model = spacy.load("model_artifacts")
    parsed_text = loaded_model(input_data) # Generate prediction
    if parsed_text.cats["pos"] > parsed_text.cats["neg"]:
        prediction = "Positive"
        score = parsed_text.cats["pos"]
    else:
        prediction = "Negative"
        score = parsed_text.cats["neg"]
    return jsonify(prediction=prediction, score=score)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6007, debug=True)
