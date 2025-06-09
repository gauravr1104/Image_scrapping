from flask import Flask, render_template, request
import os
import requests
from bs4 import BeautifulSoup

app = Flask(__name__, template_folder="../Frontend/templates", static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def fetch_images():
    search_term = request.form["query"]
    image_directory = "static/Images"

    if os.path.exists(image_directory):
        for img in os.listdir(image_directory):
            os.remove(os.path.join(image_directory, img))
    else:
        os.makedirs(image_directory)

    headers = {"User-Agent": "Mozilla/5.0"}
    google_url = f"https://www.google.com/search?q={search_term}&tbm=isch"
    response = requests.get(google_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    image_tags = soup.find_all("img")[1:10]  # Skipping the logo
    saved_images = []

    for i, tag in enumerate(image_tags):
        img_src = tag.get("src")
        if img_src:
            img_content = requests.get(img_src).content
            filename = f"{i}.jpg"
            filepath = os.path.join(image_directory, filename)
            with open(filepath, "wb") as file:
                file.write(img_content)
            saved_images.append(filename)

    return render_template("result.html", images=saved_images, query=search_term)

if __name__== "__main__":
    app.run(host="localhost",
            port=3000)