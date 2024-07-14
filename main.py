import random
import string
import qrcode
from io import BytesIO
from flask import Flask, render_template, redirect, request, send_file

app = Flask(__name__)
shortened_urls = {}

def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(length))
    return short_url

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        short_url = generate_short_url()
        while short_url in shortened_urls:
            short_url = generate_short_url()
        shortened_urls[short_url] = long_url
        return render_template("index.html", short_url=f"{request.url_root}{short_url}", qr_code_url=f"{request.url_root}qr/{short_url}")
    return render_template("index.html")

@app.route("/qr/<short_url>")
def get_qr_code(short_url):
    long_url = shortened_urls.get(short_url)
    if long_url:
        img = qrcode.make(long_url)
        img_buffer = BytesIO()
        img.save(img_buffer, "PNG")
        img_buffer.seek(0)
        return send_file(img_buffer, mimetype="image/png")
    else:
        return "URL not found", 404

@app.route("/<short_url>")
def redirect_url(short_url):
    long_url = shortened_urls.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found", 404

if __name__ == "__main__":
    app.run(debug=True)