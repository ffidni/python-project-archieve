from mode_list import *

class TypingMenu(QWidget):

	def __init__(self):
		super().__init__()
		self.w, self.h = 900, 600
		self.setMinimumSize(self.w, self.h)
		self.resize(self.w, self.h)
		self.init_ui()

	def init_ui(self):
		self.timer = 10
		self.text_counter = 0
		self.old_input = ""
		self.setObjectName("Main")
		self.setup_widget()
		self.setup_layout()
		self.setup_stylesheet()
		self.installEventFilter(self)

	def setup_widget(self):
		self.title = QLabel("10 Seconds Test")
		self.modes = TypingModes(self)
		self.text = QTextEdit("This is a short paragraph, actually this is a sentence.")
		self.input = QLineEdit("Type here to start")
		self.reset_btn = QPushButton("Reset")

		self.title.setFont(QFont("MS Shell Dlg", 38))
		self.text.setFixedSize(350, 120)
		self.text.setFont(QFont("Arial", 13))
		self.text.setReadOnly(True)
		self.text.setTextInteractionFlags(Qt.NoTextInteraction)
		self.input.setFont(QFont("Arial", 13))
		self.input.setFixedSize(350, 40)
		self.input.installEventFilter(self)
		self.input.textChanged.connect(self.changed_event)
		self.timer_display = QLabel(self.timer_format(self.timer))
		self.timer_display.setObjectName("Timer")
		self.timer_display.setFont(QFont("MS Shell Dlg 2", 10))
		self.timer_display.setFixedSize(80, 30)
		self.timer_display.setAlignment(Qt.AlignCenter)
		self.reset_btn.setFont(QFont("MS Shell Dlg 2", 10))
		self.reset_btn.setFixedSize(80, 35)
		self.reset_btn.setObjectName("Reset")
		self.reset_btn.setCursor(QCursor(Qt.PointingHandCursor))

	def setup_layout(self):
		self.main_layout = QVBoxLayout()
		self.hor_layout = QHBoxLayout()
		self.type_area = QVBoxLayout()
		self.input_layout = QHBoxLayout()

		self.hor_layout.addSpacing(50)
		self.hor_layout.addWidget(self.modes.list)
		self.hor_layout.addWidget(self.modes.dismiss_btn)
		self.type_area.addSpacing(120)
		self.type_area.addWidget(self.title, alignment=Qt.AlignCenter)
		self.type_area.addSpacing(60)
		self.type_area.addWidget(self.text, alignment=Qt.AlignCenter)
		self.type_area.addSpacing(30)
		self.type_area.addWidget(self.input, alignment=Qt.AlignCenter)
		self.type_area.addSpacing(30)
		self.input_layout.addWidget(self.timer_display, alignment=Qt.AlignRight)
		self.input_layout.addWidget(self.reset_btn, alignment=Qt.AlignLeft)
		self.type_area.addLayout(self.input_layout)
		self.type_area.addSpacing(100)
		self.hor_layout.addLayout(self.type_area)
		self.hor_layout.addSpacing(0)
		self.main_layout.addSpacing(20)
		self.main_layout.addLayout(self.hor_layout)
		self.setLayout(self.main_layout)

	def timer_format(self, secs):
		return "{:02d}:{:02d}".format(*divmod(secs, 60))

	def changed_event(self, value):
		if not value and not self.text_counter:
			print("B")
		else:
			#print(len(value), len(self.old_input))
			if len(value) < len(self.old_input):
				self.text_counter -= 1
			else:
				text = self.text.toPlainText()[self.text_counter]
				#print("A")
				if value and value[-1] == text:
					print(value[-1], text)
					if value[-1] == ' ' and text == ' ':
						self.input.clear()
						self.old_input = ""
					#print("Y")
				elif value and not value[-1] == text:
					pass
					#print("N")

				self.text_counter += 1
				if self.old_input:
					self.old_input = value
		

	def expand_size(self):
		if not self.modes.list.isHidden():
			self.modes.list.setFixedSize(300*self.w_factor, 398*self.h_factor)
			self.modes.list.setFont(QFont("Arial", 19*self.h_factor))
			self.modes.dismiss_btn.setFixedSize(32*self.w_factor, 32*self.h_factor)
			self.modes.dismiss_btn.setIconSize(QSize(32*self.w_factor, 32*self.h_factor))
			self.title.setFont(QFont("MS Shell Dlg", 38*self.w_factor))
			self.text.setFixedSize(350*self.w_factor, 80*self.h_factor)
			self.input.setFixedSize(350*self.w_factor, 40)
			#self.type_area.itemAt(0).changeSize(0, 120*self.h_factor)
			#self.type_area.itemAt(4).changeSize(0, 30)
			#self.type_area.itemAt(8).changeSize(0, 100*self.h_factor)
		else:
			self.title.setFont(QFont("MS Shell Dlg", 50*self.h_factor))
			self.text.setFixedSize(372*self.w_factor, 90*self.h_factor)
			self.input.setFixedSize(372*self.w_factor, 40)
			#self.reset_btn.setFixedSize(112*self.w_factor, 42*self.h_factor)
			#self.reset_btn.setFont(QFont("MS Shell Dlg 2", 11*self.h_factor))
			#self.type_area.itemAt(0).changeSize(0, (120-(40))*self.h_factor)
			#self.type_area.itemAt(4).changeSize(0, 5*self.h_factor)
			#self.type_area.itemAt(8).changeSize(0, (100-(48))*self.h_factor)
		self.timer_display.setFixedSize(80*self.w_factor, 30*self.h_factor)
		self.timer_display.setFont(QFont("MS Shell Dlg 2", 12*self.h_factor))
		self.reset_btn.setFixedSize(80*self.w_factor, 30*self.h_factor)
		self.reset_btn.setFont(QFont("MS Shell Dlg 2", 10*self.h_factor))

	def setup_stylesheet(self):
		self.setStyleSheet("""#Main{
							  	background: #e1d4bb;
							  }
							  QLabel{
							  	color: #333333;
							  }
							  #Reset{
							  	background: #d94141;
							  	color: white;
							  	border-radius: 4px;
							  	border: 1px solid black;
							  }
							  #Dismiss{
							  	background: transparent;
							  	border: none;
							  }
							  #Timer{
							  	background: #3488ef;
							  	color: white;
							  	border-radius: 4px;
							  	border: 1px solid black;
							  }
							  QLineEdit{
							  	color: lightgray;
							  }
							  QListWidget{
							  	color: #e7e7e7;
							  	background: #c7922b;
							  	border-radius: 4px;
							  	border: 1px solid black;
							  }
							  """)

	def eventFilter(self, obj, event):
		if event.type() == QEvent.MouseButtonPress:
			if event.button() == Qt.LeftButton:
				if obj == self.input:
					if self.input.text() == "Type here to start":
						self.input.clear()
						self.input.setStyleSheet("color: black;")
				else:
					if not self.input.text():
						self.input.setText("Type here to start")
						self.input.setStyleSheet("color: lightgray;")
					self.input.clearFocus()

		return super().eventFilter(obj, event)

	def resizeEvent(self, event):
		self.w_factor = self.width() / self.w
		self.h_factor = self.height() / self.h

		self.expand_size()



		

if __name__ == '__main__':
    app = QApplication(argv)
    win = TypingMenu()
    win.show()
    exit(app.exec_())