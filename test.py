import spacy

def test(input_data):
    # input_data = request.form['review']
    print(input_data)
    loaded_model = spacy.load("model_artifacts")
    parsed_text = loaded_model(input_data) # Generate prediction
    if parsed_text.cats["pos"] > parsed_text.cats["neg"]:
        prediction = "Positive"
        score = parsed_text.cats["pos"]
    else:
        prediction = "Negative"
        score = parsed_text.cats["neg"]
    print(prediction, score)

if __name__ == "__main__":
    review = 'Only Uwe Boll would assume that the moviegoing public craved a trashy Lord of the Rings rip-off starring Burt Reynolds and Matthew Lillard, and only he could then manage to make such a potentially riotous endeavor so humorless.'
    test(review)


