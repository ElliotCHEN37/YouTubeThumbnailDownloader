import sys
import requests
from PyQt5 import QtGui, QtWidgets
from pytube import YouTube
from ui_main import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon(':/img/resources/YTTDL-LOGO.png'))
        self.ui.pushButton_dl.clicked.connect(self.download_thumbnail)

    def download_thumbnail(self):
        try:
            youtube_url = self.ui.Lineedit_URL.text()
            yt = YouTube(youtube_url)
            thumbnail_url = yt.thumbnail_url

            response = requests.get(thumbnail_url)
            if response.status_code == 200:
                save_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, self.tr("Save Thumbnail"), "", self.tr("Images (*.png *.jpg)"))
                if save_path:
                    with open(save_path, 'wb') as f:
                        f.write(response.content)
                    print("Thumbnail downloaded successfully at:", save_path)
                    QtWidgets.QMessageBox.information(self, self.tr("Success"), self.tr("Thumbnail downloaded successfully at: ") + save_path)
                else:
                    print("Failed to download thumbnail.")
                    QtWidgets.QMessageBox.critical(self, self.tr("Warning"), self.tr("Failed to download thumbnail."))
        except Exception as e:
            print("Error downloading thumbnail:", str(e))
            QtWidgets.QMessageBox.critical(self, self.tr("Error"), self.tr("Error downloading thumbnail: ") + str(e))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
