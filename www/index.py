<%

import html
import sessionManager


html.initHTML(self)
html.beginHead(self)
html.endHead(self)
html.beginContent(self)
html.addTitle(self, textStyle.italic("IT WORKS"))

print __GET__['haha'][0]


print sessionManager.get(self, 'haha')
sessionManager.set(self, 'haha', __GET__['haha'][0])
html.beginForm(self, "form2")
html.formAddInput(self, "text")
html.formAddSubmit(self, "manda")
html.endForm(self)

html.endContent(self)
html.endHtml(self)

%>

