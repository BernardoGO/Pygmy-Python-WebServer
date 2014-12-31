__author__ = 'bernardo'
import config
from wstypes import HTMLVer



def InitHTML(self, htmltype = config.__HTML_VER__):

    if htmltype == HTMLVer.HTML4:
        print """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" >\n"""

    elif htmltype == HTMLVer.HTML5:
        print """<!DOCTYPE html>
			<html>\n"""

    else:
        print "ERROR: Function: InitHTML Error: expected HTML4 or HTML5, found "+str(htmltype)+" instead"
        sys.exit(0)


def beginHead(self):
    print "<head>\n"

def setTitle(self,title):
    print "<title>"+title+"</title>\n"

def endHead(self):
    print "</head>\n"


def beginContent(self):
	print "<body>\n"


def addParagraph(self,para,cssclass="",idd=""):
    para = para.replace("\n","<br />")
    print "<p id='"+idd+"' class='"+cssclass+"'>"+para+"</p>\n"
def newParagraph(self):
    print "<p>"
def endParagraph(self):
    print "</p>\n"


def addBlock(self,idd,name):
    print "<div id='"+idd+"' name='"+name+"'></div>"
def newBlock(self,idd,name="",cssclass=""):
    print "<div id='"+idd+"' class='"+cssclass+"' name='"+name+"'>\n"

def endBlock(self):
    print "</div>\n"

def addText(self,text):
    text = text.replace("\n","<br />")
    print text

def addTitle(self,txt,idd="",cssclass=""):
    print "<h1 class=\""+cssclass+"\" id=\""+idd+"\">"+txt+"</h1>"

def addSubTitle(self,txt,idd="",cssclass=""):
    print "<h2 class=\""+cssclass+"\" id=\""+idd+"\">"+txt+"</h2>"

def endContent(self):
    print "</body>\n"