🖼️ Image Scrapping Web Application
A simple web-based image scrapper that allows users to search for a keyword and retrieve images based on that query. Built using Flask for the backend and basic HTML for the frontend.

📁 Project Structure
Img_scrapping/
├── Backend/
│   ├── main.py
│   └── static/
│       └── Images/   # Contains downloaded images
├── Frontend/
│   └── templates/
│       └── index.html
├── Requirement.txt

🚀 Features
Keyword-based image scraping

Dynamic image display in the frontend

Lightweight design using Flask and HTML

Downloaded images stored locally in the static/Images/ directory

⚙️ Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/Image_scrapping.git
cd Image_scrapping/Img_scrapping
Create a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the dependencies

bash
Copy
Edit
pip install -r Requirement.txt
🧪 Usage
Run the backend server

bash
Copy
Edit
cd Backend
python main.py
Open the frontend
Navigate to http://127.0.0.1:5000/ in your web browser.

Search for images
Enter a keyword, and the app will scrape and display related images.

🛠️ Built With
Python

Flask

BeautifulSoup

Requests

HTML/CSS (for frontend UI)

📸 Example
The static/Images/ folder will populate with scraped images like:

python-repl
Copy
Edit
0.jpg
1.jpg
...
📄 License
This project is licensed under the MIT License.
