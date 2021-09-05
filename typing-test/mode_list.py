from packages import *

class TypingModes(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.setup_widget()
        self.setup_stylesheet()

    def setup_widget(self):
        self.list = QListWidget()
        self.dismiss_btn = QPushButton()

        self.list.addItem("10 Seconds Test")
        self.list.addItem("15 Seconds Test")
        self.list.addItem("30 Seconds Test")
        self.list.addItem("60 Seconds Test")
        self.list.setCurrentRow(0)
        self.list.setFont(QFont("Arial", 19))
        self.list.setSpacing(30)
        self.list.setFixedSize(300, 398)
        self.list.itemClicked.connect(self.change_mode)
        self.list.setCursor(QCursor(Qt.PointingHandCursor))
        self.dismiss_btn.setIcon(QIcon("Assets/dismiss.png"))
        self.dismiss_btn.setFixedSize(32, 32)
        self.dismiss_btn.setIconSize(QSize(32, 32))
        self.dismiss_btn.setStyleSheet("""background: transparent;""")
        self.dismiss_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.dismiss_btn.setObjectName("Dismiss")
        self.dismiss_btn.clicked.connect(self.dismiss_widget)
        self.dismiss_btn.setToolTip("Dismiss the option")

    def setup_stylesheet(self):
        self.list.setStyleSheet("""QListView:item:selected{
                                    background: pallate(Highlight);
                                    }""")

    def dismiss_widget(self):
        if self.list.isHidden():
            self.parent.hor_layout.insertWidget(1, self.list)
            self.parent.hor_layout.itemAt(0).changeSize(50, 0)
            self.list.show()
            self.parent.expand_size()
            self.dismiss_btn.setIcon(QIcon("Assets/dismiss.png"))
            self.dismiss_btn.setToolTip("Dismiss the option")
        else:
            self.parent.hor_layout.removeWidget(self.list)
            self.parent.hor_layout.itemAt(0).changeSize(0, 0)
            self.list.hide()
            self.parent.expand_size()
            self.dismiss_btn.setIcon(QIcon("Assets/show.png"))
            self.dismiss_btn.setToolTip("Show the option")

    def change_mode(self, event):
        mode = int(event.text().split()[0])
        row = self.list.currentRow()
        self.parent.timer = mode
        self.parent.title.setText(f"{mode} Seconds Test")
        self.parent.timer_display.setText(self.parent.timer_format(mode))