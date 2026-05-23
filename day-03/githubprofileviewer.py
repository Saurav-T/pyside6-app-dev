import sys
import requests
import webbrowser

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class GitHubViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GitHub Profile Viewer")
        self.setGeometry(200, 200, 800, 500)

        self.repos = []

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Top input section
        top_layout = QHBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter GitHub username")

        self.search_btn = QPushButton("Search")
        self.search_btn.clicked.connect(self.fetch_profile)

        top_layout.addWidget(self.username_input)
        top_layout.addWidget(self.search_btn)

        # Profile section
        profile_layout = QHBoxLayout()

        self.avatar_label = QLabel()
        self.avatar_label.setFixedSize(120, 120)
        self.avatar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.info_label = QLabel("User info will appear here")
        self.info_label.setWordWrap(True)

        profile_layout.addWidget(self.avatar_label)
        profile_layout.addWidget(self.info_label)

        # Repo list
        self.repo_list = QListWidget()
        self.repo_list.itemClicked.connect(self.open_repo)

        layout.addLayout(top_layout)
        layout.addLayout(profile_layout)
        layout.addWidget(QLabel("Repositories:"))
        layout.addWidget(self.repo_list)

        self.setLayout(layout)

    def fetch_profile(self):
        username = self.username_input.text().strip()

        if not username:
            QMessageBox.warning(self, "Error", "Please enter a username")
            return

        user_url = f"https://api.github.com/users/{username}"
        repo_url = f"https://api.github.com/users/{username}/repos"

        user_res = requests.get(user_url)
        repo_res = requests.get(repo_url)

        if user_res.status_code != 200:
            QMessageBox.warning(self, "Error", "User not found")
            return

        user_data = user_res.json()
        repo_data = repo_res.json()

        # Update profile info
        self.update_profile(user_data)

        # Update repos
        self.repo_list.clear()
        self.repos = []

        for repo in repo_data:
            name = repo["name"]
            url = repo["html_url"]

            self.repos.append(url)
            self.repo_list.addItem(name)

    def update_profile(self, data):
        name = data.get("name") or "No name"
        bio = data.get("bio") or "No bio"
        followers = data.get("followers", 0)
        following = data.get("following", 0)
        public_repos = data.get("public_repos", 0)

        info_text = f"""
Name: {name}
Bio: {bio}

Followers: {followers}
Following: {following}
Public Repos: {public_repos}
        """

        self.info_label.setText(info_text)

        # Load avatar
        avatar_url = data.get("avatar_url")

        if avatar_url:
            img_data = requests.get(avatar_url).content
            pixmap = QPixmap()
            pixmap.loadFromData(img_data)
            self.avatar_label.setPixmap(pixmap.scaled(
                120, 120, Qt.AspectRatioMode.KeepAspectRatio
            ))

    def open_repo(self, item):
        index = self.repo_list.currentRow()
        if index >= 0:
            webbrowser.open(self.repos[index])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GitHubViewer()
    window.show()
    sys.exit(app.exec())