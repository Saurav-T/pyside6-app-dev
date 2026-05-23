import requests
import webbrowser
import sys

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QPushButton, QLabel, QComboBox
)

class Article:
    def __init__(self, title, description, url, source):
        self.title = title
        self.description = description
        self.url = url
        self.source = source

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://newsapi.org/v2/top-headlines"

class NewsApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("News Reader App")
        self.setGeometry(100, 100, 900, 500)

        self.articles = []

        self.init_ui()
        self.load_news()

    def init_ui(self):
        layout = QVBoxLayout()

        # Top controls
        top_bar = QHBoxLayout()

        self.category_box = QComboBox()
        self.category_box.addItems([
            "technology", "business", "sports",
            "health", "entertainment", "science"
        ])

        self.refresh_btn = QPushButton("Refresh")
        self.refresh_btn.clicked.connect(self.load_news)

        top_bar.addWidget(self.category_box)
        top_bar.addWidget(self.refresh_btn)

        # Main layout
        main_layout = QHBoxLayout()

        # List of news
        self.news_list = QListWidget()
        self.news_list.itemClicked.connect(self.show_article)

        # Detail panel
        self.title_label = QLabel("Title")
        self.desc_label = QLabel("Description")
        self.open_btn = QPushButton("Open in Browser")
        self.open_btn.clicked.connect(self.open_article)

        right_panel = QVBoxLayout()
        right_panel.addWidget(self.title_label)
        right_panel.addWidget(self.desc_label)
        right_panel.addWidget(self.open_btn)

        main_layout.addWidget(self.news_list)
        main_layout.addLayout(right_panel)

        layout.addLayout(top_bar)
        layout.addLayout(main_layout)

        self.setLayout(layout)

    def load_news(self):
        category = self.category_box.currentText()

        self.articles = fetch_news(category=category)

        self.news_list.clear()

        for article in self.articles:
            self.news_list.addItem(article["title"])

    def show_article(self, item):
        index = self.news_list.currentRow()
        article = self.articles[index]

        self.current_url = article["url"]

        self.title_label.setText(article["title"])
        self.desc_label.setText(article["description"] or "No description")

    def open_article(self):
        if hasattr(self, "current_url"):
            webbrowser.open(self.current_url)
    

def fetch_news(category="technology", country="us"):
    params = {
        "apiKey": API_KEY,
        "category": category,
        "country": country
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return []
    
    data = response.json()

    articles = []

    for item in data.get("articles", []):
        articles.append({
            "title": item.get("title"),
            "description": item.get("description"),
            "url": item.get("url"),
            "source": item.get("source", {}).get("name")
        })

    return articles

app = QApplication(sys.argv)

window = NewsApp()
window.show()

sys.exit(app.exec())
