import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap
from ui_form import Ui_Widget
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

# Authentification Spotify
auth = {
    "client_id": "your_client_id",
    "client_secret": "your_secret_id",
    "redirect_uri": "your_callbacl_url",
    "scope": "user-read-playback-state"
}

spotifyObject = Spotify(auth_manager=SpotifyOAuth(
    client_id=auth["client_id"],
    client_secret=auth["client_secret"],
    redirect_uri=auth["redirect_uri"],
    scope=auth["scope"],
))

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Spotify overlay")

        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.progressBar.setStyleSheet("""
            QProgressBar {
                border: none;
                border-radius: 5px;
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #b6359c, stop:1 #ef0a6a);
                margin : 0px;
                paddin : 0px;
            }
            QProgressBar::chunk {
                background-color: white;
                width: 20px;

            }
        """)


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_music_name)
        self.timer.start(1000)

        self.update_music_name()

    def update_music_name(self):
        try:
            data = spotifyObject.current_user_playing_track()
            if data is not None and 'item' in data:
                artist_name = data['item']['artists'][0]['name']
                track_name = data['item']['name']
                duration_ms = data['item']['duration_ms']
                progress_ms = data['progress_ms']
                image_url = data['item']['album']['images'][0]['url']

                self.ui.musicName.setText(track_name)
                self.ui.artistName.setText(artist_name)
                self.ui.progressBar.setValue(progress_ms)
                self.ui.progressBar.setMaximum(duration_ms)

                # PixMap musicImage
                pixmap = QPixmap()
                pixmap.loadFromData(self.download_image(image_url))
                self.ui.musicImage.setPixmap(pixmap)

            else:
                self.ui.musicName.setText("Aucune musique en cours.")
        except Exception as e:
            self.ui.musicName.setText(f"Erreur lors de la récupération : {str(e)}")

    def download_image(self, url):
        import requests
        response = requests.get(url)
        return response.content if response.status_code == 200 else None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
