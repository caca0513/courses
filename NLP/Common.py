import spacy
from tabulate import tabulate
from spacy import displacy

def Render(data, style='ent'):
    displacy.render(data, style=style, jupyter=True)