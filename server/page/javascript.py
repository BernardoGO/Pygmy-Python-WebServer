__author__ = 'bernardo'


began = False

def beginScript(self):
    global began
    if began == False:
        began = True
        print ("<script>\n")


def endScript(self, initState = False):
    global began
    if began == True and initState == False:
        began = False
        print ("</script>\n")

def redirect(self, link):
    initState = began
    beginScript(self)
    print('window.location.href = \"'+link+'\";')
    endScript(self)

def alert(self, text):
    initState = began
    beginScript(self)
    print ('alert("'+text+'");')
    endScript(self)