import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox, QMenu, QAction
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices, QClipboard
import requests

class YouTubeThumbnailDownloader(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Thumbnail Downloader - Waiting for user action")
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
        
        menubar = self.menuBar()
        
        file_menu = menubar.addMenu('File')
        
        paste_action = QAction('Paste YT Video ID', self)
        paste_action.triggered.connect(self.paste_text)
        file_menu.addAction(paste_action)
        
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        about_menu = menubar.addMenu('About')
        
        about_action = QAction('About', self)
        about_action.triggered.connect(self.show_about_dialog)
        about_menu.addAction(about_action)
        
        changelog_action = QAction('Changelog', self)
        changelog_action.triggered.connect(self.show_changelog_dialog)
        about_menu.addAction(changelog_action)
        
        sponsor_action = QAction('Sponsor', self)
        sponsor_action.triggered.connect(self.show_sponsor_dialog)
        about_menu.addAction(sponsor_action)
        
    def show_about_dialog(self):
        about_text = "YouTube Thumbnail Downloader Version 1.3.1 (01/31/24) By ElliotCHEN\n\nA simple YouTube Thumbnail download program written in PyQt5\n\nhttps://github.com/ElliotCHEN37/YouTubeThumbnailDownloader\n\nThis work is licensed under MIT License"
        QMessageBox.about(self, "About", about_text)

    def show_changelog_dialog(self):
        changelog_text = "v1.3.1 (01/30/24)\nNew\n-Add shortcut"
        QMessageBox.about(self, "Changelog", changelog_text)

    def show_sponsor_dialog(self):
        sponsor_text = "Currently N/A"
        QMessageBox.about(self, "Sponsor", sponsor_text)
        
    def paste_text(self):
        clipboard = QApplication.clipboard()
        clipboard_text = clipboard.text()

        self.video_id_entry.setText(clipboard_text)

    def download_image(self):
        video_id = self.video_id_entry.text() or self.lineEdit.text()
        if video_id:
            url = f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'
            res = requests.get(url)

            file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "JPEG files (*.jpg);;All Files (*)")

            if file_path:
                with open(file_path, 'wb') as f:
                    f.write(res.content)
                self.setWindowTitle("YouTube Thumbnail Downloader - Done")
                QMessageBox.information(self, "Download Successful", "Image downloaded successfully!")
            else:
                self.setWindowTitle("YouTube Thumbnail Downloader - Cancelled")
                QMessageBox.information(self, "Download Cancelled", "Image download was cancelled.")
        else:
            self.setWindowTitle("YouTube Thumbnail Downloader - Error")
            QMessageBox.warning(self, "Error", "Please enter a Video ID.")
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.download_image()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = YouTubeThumbnailDownloader()
    mainWin.show()
    sys.exit(app.exec_())
