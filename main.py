import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class VideoThumbnail(QWidget):
    def __init__(self, thumbnail, duration, title, channel_logo, channel_name, views, time_ago):
        super().__init__()
        
        thumbnail_lebel = QLabel()
        pixmap = QPixmap(thumbnail)
        thumbnail_lebel.setPixmap(pixmap.scaled(320, 180, Qt.AspectRatioMode.KeepAspectRatio))
        thumbnail_lebel.setFixedSize(320, 180)
        
        duration_lebel = QLabel()
        duration_lebel.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        
        duration_lebel.setStyleSheet("background-color: black; color: white; padding:2px")
        
        thumbnail_container = QWidget()
        thumbnail_container_layout = QVBoxLayout()
        thumbnail_container_layout.addWidget(thumbnail_lebel)
        thumbnail_container_layout.addWidget(duration_lebel, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
        thumbnail_container.setLayout(thumbnail_container_layout)
        
        title_lebel = QLabel(title)
        title_lebel.setWordWrap(True)
        channel_logo_lebel = QLabel(channel_logo)
        pixmap = QPixmap(channel_logo)
        channel_logo_lebel.setPixmap(pixmap.scaled(320, 180, Qt.AspectRatioMode.KeepAspectRatio))
        channel_logo_lebel.setFixedSize(40, 40)
        channel_name_lebel = QLabel(channel_name)
        
        channel_info_layout = QHBoxLayout()
        channel_info_layout.addWidget(channel_logo_lebel)
        channel_info_layout.addWidget(channel_name_lebel)
        
        views_and_time_layout = QHBoxLayout()
        views_lebel = QLabel(views)
        time_ago_lebel = QLabel(time_ago)
        views_and_time_layout.addWidget(views_lebel)
        views_and_time_layout.addWidget(views_and_time_layout)
        
        video_layout = QVBoxLayout()