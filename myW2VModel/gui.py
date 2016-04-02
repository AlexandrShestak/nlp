# -*- coding: utf-8 -*-
import Tkinter
from Tkconstants import END

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from gensim.models import Word2Vec
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.xml.networkreader import NetworkReader
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class NetworkWorkVisualiser(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        #self.entryVariable = Tkinter.StringVar()
        #self.entry = Tkinter.Text(self, textvariable=self.entryVariable)
        self.entry = Tkinter.Text(self, height=7)
        self.entry.grid(column=0, row=0, sticky='EW')

        button = Tkinter.Button(self, text=u"Предсказать!", command=self.onTextEntered)
        button.grid(column=1, row=0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=self.labelVariable, anchor="w")
        label.grid(column=0, row=1, columnspan=2, sticky='EW')

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, True)

    def onTextEntered(self):
        model_name = "clean_text_model"
        w2v_model = Word2Vec.load(model_name)
        new_post_text = self.entry.get(1.0, END)
        row_vector_array = []
        for w in new_post_text.split():
            if w in w2v_model.vocab:
                    row_vector_array.extend(w2v_model[w])
        net = NetworkReader.readFrom('trained_network1.xml')
        result = net.activate(row_vector_array[:100])
        print result
        self.labelVariable.set("Result : " + str(result))


if __name__ == "__main__":
    app = NetworkWorkVisualiser(None)
    app.title('Post predictor')
    app.mainloop()
