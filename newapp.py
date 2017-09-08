import sys
import os
import pyperclip

from PyQt4 import QtGui, QtCore
#from PyQt4 import QtGui

 
class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        QtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        global xval
        global yval
        global resox
        global resoy
        
        xval = 400/2
        yval = 600
        
        resox, resoy = (1920,1080)
        
        self.setGeometry(int(resox-xval),int((resoy-yval)/2),int(xval),int(yval))
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))


        openEditor = QtGui.QAction("&Editor", self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

        extractAction = QtGui.QAction("&Close Application", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave the app')
        extractAction.triggered.connect(self.close_application)

        openFile = QtGui.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        saveFile = QtGui.QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(extractAction)

        editorMenu = mainMenu.addMenu('&Editor')
        editorMenu.addAction(openEditor)
        editorMenu.addAction(saveFile)
       
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Paste Text 1", self)
        #btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.clicked.connect(self.copy_text1)
        btn.resize(100,100)
        #btn.resize(btn.minimumSizeHint())
        btn.move((xval-(100))/2,100)

        extractAction = QtGui.QAction( 'Quit',self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)


        ##to add icon to fontChoice
        #fontChoice = QtGui.QAction(QtGui.QIcon('ss.png'),'Yeye2',self)
        fontChoice = QtGui.QAction('Font',self)
        fontChoice.triggered.connect(self.font_choice)
        #self.toolBar = self.addToolBar("Font")
        self.toolBar.addAction(fontChoice)

        
        #checkBox = QtGui.QCheckBox('Enlarge Window',self)

        checkBox.move(0,25+50)
        # checkBox.toggle()
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QtGui.QPushButton("Download",self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)


        print(self.style().objectName())
        #self.styleChoice = QtGui.QLabel("Windows Vista", self)

        #comboBox = QtGui.QComboBox(self)
        #comboBox.addItem("motif")
        #comboBox.addItem("Windows")
        #comboBox.addItem("cde")
        #comboBox.addItem("Plastique")
        #comboBox.addItem("Cleanlooks")
        #comboBox.addItem("windowsvista")

        #comboBox.move(50,250)
        #self.styleChoice.move(50,150)
        #comboBox.activated[str].connect(self.style_choice)
 
        self.show()

    def style_choice(self,text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def copy_text1(self,fo):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = dir_path + r'\txts\wwe.txt'
        fo = open(path, 'r').read()
        pyperclip.copy(fo)
        print("Clipboard contents: ",fo)

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.setGeometry(int(resox-xval*2),int((resoy-yval)/2),int(xval*2),int(yval))
        self.textEdit.paste()
        
    def file_save(self):
        #name = QtGui.QFileDialog.getSaveFileName(self, "Save File")
        bse = 'wwe.txt'
        name = os.getcwd() + '\\txts\\' + bse
        #print(name)
        #file = open(name,'w')
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        print('Saving File')
        print(text)
        file.write(text)
        file.close()
        self.textEdit.close() 
        self.setGeometry(int(resox-xval),int((resoy-yval)/2),int(xval),int(yval))
        
    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, "Open File")
        file = open(name,'r')

        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)
            

    
    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)
            

        
    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)


    
    def close_application(self):

    #pop up box
        choice = QtGui.QMessageBox.question(self, 'Quit', "Would you like to quit application?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Quitting App")
            sys.exit()
        else:
            pass
        
    def enlarge_window(self, state):
         
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)
            

        
        
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()

#window = QtGui.QWidget()
#window.setGeometry(50, 50, 500, 300)
#window.setWindowTitle("PyT")

#window.show()
