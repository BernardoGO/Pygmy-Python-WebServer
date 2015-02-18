__author__ = 'bernardo'

def __addMeta(meta, text):
    text = text.replace("\n","<br />")
    return "<" + meta + ">" + text + "</" + meta + ">"



def bold(txt):
	txt = txt.replace("\n","<br />")
	return "<strong>"+txt+"</strong>"
def emphasized(txt):
	txt = txt.replace("\n","<br />")
	return "<em>"+txt+"</em>"

def b(txt):
    return __addMeta("b", txt)
def i(txt):
    return __addMeta("i", txt)

def small(text):
    return __addMeta("small", text)
def mark(text):
    return __addMeta("mark", text)
def deleted(txt):
    return __addMeta("del", txt)
def ins(txt):
    return __addMeta("ins", txt)
def sub(txt):
    return __addMeta("sub", txt)
def deleted(txt):
    return __addMeta("del", txt)

def underline(txt):
	txt = txt.replace("\n","<br />")
	return "<u>"+txt+"</u>"
def link(txt,to,idd="",cssclass=""):
	txt = txt.replace("\n","<br />")
	return "<a href='"+to+"' id='"+idd+"' class='"+cssclass+"'>"+txt+"</a>"

def li(txt):
	txt = txt.replace("\n","<br />")
	return "<li>"+txt+"</li>"

def ol(txt):
    return __addMeta("ol", txt)

def ul(txt):
    return __addMeta("ul", txt)
