__author__ = 'bernardo'

def __addMeta(meta, text):
    text = text.replace("\n","<br />")
    return "<" + meta + ">" + text + "</" + meta + ">"



def bold(txt):
	txt = txt.replace("\n","<br />")
	return "<strong>"+txt+"</strong>"
def italic(txt):
	txt = txt.replace("\n","<br />")
	return "<em>"+txt+"</em>"
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
