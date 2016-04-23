# -*- coding: utf-8 -*-
import Tkinter
import sys
from Tkconstants import END

from kmpCleanPackage.MainWordsExtractor import MainWordsExtractor
from kmpCleanPackage.PostPredictor import PostPredictor
from kmpCleanPackage.TextCleaner import TextCleaner
from kmpCleanPackage.autivivify_list import autovivify_list

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
        self.entry = Tkinter.Text(self, height=18   )
        self.entry.grid(column=0, row=0, sticky='EW')

        button = Tkinter.Button(self, text=u"Предсказать!", command=self.onTextEntered)
        button.grid(column=1, row=0)

        self.mainWordsString = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=self.mainWordsString, anchor="w")
        label.grid(column=0, row=1, columnspan=2, sticky='EW')

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=self.labelVariable, anchor="w")
        label.grid(column=0, row=2, columnspan=2, sticky='EW')

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, True)

    def onTextEntered(self):
        new_post_text = self.entry.get(1.0, END)
        clean_text = TextCleaner.cleanText(new_post_text)
        main_words = MainWordsExtractor.extract(clean_text)
        self.mainWordsString.set("Main words : " + main_words)
        result = PostPredictor.predict(main_words)
        self.labelVariable.set("Result : " + str(result))

if __name__ == "__main__":
    app = NetworkWorkVisualiser(None)
    app.title('Post predictor')
    app.mainloop()
