__author__ = 'bernardo'



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