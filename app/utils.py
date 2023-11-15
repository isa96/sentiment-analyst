from flask import render_template


# render page 404
def page_not_found(e):
    return render_template("404.html")

# convert sentiment array to string
def convert_sentiment(predict):
    """
    convert int to string
    """
    if predict == 0:
        return "NEGATIVE"
    elif predict == 1:
        return "POSITIVE"
    else:
        return "NEUTRAL"