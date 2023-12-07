import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices

import requests
from PIL import Image

class YouTubeThumbnailDownloader(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Thumbnail Downloader GUI v1.2")
        self.setGeometry(100, 100, 600, 270)
        self.setFixedSize(374, 196)

        self.initUI()

    def initUI(self):
        self.label = QLabel("Welcome to YouTube Thumbnail Downloader", self)
        self.label.setGeometry(30, 20, 321, 20)
        
        self.video_id_entry = QLineEdit(self)
        self.video_id_entry.setText("Paste your YouTube video ID here:")
        self.video_id_entry.setGeometry(30, 50, 321, 30)

        self.download_button = QPushButton("Download", self)
        self.download_button.setCursor(Qt.PointingHandCursor)
        self.download_button.setGeometry(30, 90, 321, 30)
        self.download_button.clicked.connect(self.download_image)

    def download_image(self):
        video_id = self.video_id_entry.text() or self.lineEdit.text()
        if video_id:
            url = f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'
            res = requests.get(url)

            # Open a file dialog to choose the download directory
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "JPEG files (*.jpg);;All Files (*)")

            if file_path:
                with open(file_path, 'wb') as f:
                    f.write(res.content)
                QMessageBox.information(self, "Download Successful", "Image downloaded successfully!")
            else:
                QMessageBox.information(self, "Download Cancelled", "Image download was cancelled.")
        else:
            QMessageBox.warning(self, "Error", "Please enter a Video ID.")

    def open_browser(self, event):
        QDesktopServices.openUrl(QUrl("https://github.com/ElliotCHEN37/YouTubeThumbnailDownloader"))  # Replace with your desired URL

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = YouTubeThumbnailDownloader()
    mainWin.show()
    sys.exit(app.exec_())
