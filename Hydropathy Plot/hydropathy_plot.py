# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hydropathy_plot.ui'
#
# Created: Wed Aug 13 18:25:39 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(608, 490)
        Form.setWindowOpacity(1.0)
        Form.setAutoFillBackground(False)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 4, 2, 1, 2)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 11))
        self.label.setBaseSize(QtCore.QSize(0, 9))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica World"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.spinBox_2 = QtGui.QSpinBox(Form)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.gridLayout.addWidget(self.spinBox_2, 5, 1, 1, 1)
        self.spinBox = QtGui.QSpinBox(Form)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.spinBox, 4, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 6, 0, 3, 4)
        self.textEdit = QtGui.QTextEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setFrameShape(QtGui.QFrame.StyledPanel)
        self.textEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.textEdit.setLineWidth(2)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Hydropathy graph plotting tool", None))
        self.comboBox.setItemText(0, _translate("Form", "Plot.ly", None))
        self.comboBox.setItemText(1, _translate("Form", "Matplotlib", None))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Paste protein sequence below:</span></p></body></html>", None))
        self.label_3.setText(_translate("Form", "Stepping number for sliding window", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#000000;\">Hydropathy Plot</span><br/><span style=\" font-size:10pt; font-weight:400; color:#555555;\">A tool for plotting a hydropapathy graph of a protein sequence.<br/>© 2014, Ismail Uddin, ismail.sameeuddin@gmail.com</span></p></body></html>", None))
        self.label_2.setText(_translate("Form", "Sliding window width (residues)", None))
        self.pushButton.setText(_translate("Form", "Plot graph", None))
        self.pushButton.clicked.connect(self.runScript)

    def runScript(self):
      from Bio_Seq import hydropathy
      window_size = int(self.spinBox.value())
      window_step = int(self.spinBox_2.value())
      seq = str(self.textEdit.toPlainText())

      window_id = []
      result = []
      range_seq = ((len(seq) // window_size) * window_size) - window_size
      window_content = []

      for i in range(0, range_seq, window_step):
        window_id.append(i)
        window = seq[i:i+window_size]
        window_content.append(window)
        hydr = hydropathy(window)
        result.append(hydr)
        


      #file = open('%s_Hydropathy_plot.CSV' % dna_id[seq_nr], 'w')
      #file.write('Window, ID, Hydropathy index (kJ/mol) \n')
      #for i in range(0, len(result), 1):
      #  file.write('%s, %s, %s \n' % (window_content[i], window_id[i], result[i]))
      #file.close()

      plotting_module = str(self.comboBox.currentText())

      if plotting_module == 'Matplotlib':
        import matplotlib.pyplot as plt
        #from matplotlib import style
        import matplotlib.collections as collections


        #style.use('ggplot')

        X = window_id
        Y = result

        plt.axhline(84)
        plt.text(0, 89, '84 kJ/mol threshold')
        plt.xlabel('First amino acid residue in window')
        plt.ylabel('Hydropathy index (free energy of transfer to water, kJ/mol)')
        plt.title('Hydropathy plot of %s aa window, stepping size of %s' % (window_size, window_step))
        plt.plot(X,Y, linewidth = 2)
        plt.show()

      else:

        # Use of plot.ly API to produce a scatter graph which is
        # uploaded online as a public graph to plot.ly servers.
        # This allows a scrolling / panning graph for very large
        # sequences which is more cumbersome to produce in MS Excel.

        import plotly.plotly as py
        from plotly.graph_objs import Figure, Data, Layout, Scatter, YAxis, XAxis

        # Enter username and API key credentials for access to
        # plot.ly servers. Credentials are provided free of charge
        # from http://plot.ly/ upon registration

        #           username     API key
        py.sign_in('USERNAME', 'API')

        trace1 = Scatter(x=window_id, y=result)
        my_data = Data([trace1])
        my_title = "Hydropathy plot of %s aa window, stepping size of %s" % (window_size, window_step)
        my_layout = Layout(title = my_title, xaxis=XAxis(title='First amino acid residue in window'), yaxis=YAxis(title='Hydropathy index (free energy of transfer to water, kJ/mol)'))
        my_fig = Figure(data=my_data, layout=my_layout)
        py.plot(my_fig, filename='Hydropathy_plot')



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
