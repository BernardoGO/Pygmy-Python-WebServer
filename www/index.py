<%

import html

html.initHTML(self)
html.beginHead(self)
html.endHead(self)
html.beginContent(self)
html.addTitle(self, textStyle.italic("IT WORKS"))

html.beginForm(self, "form2")
html.formAddInput(self, "text")
html.formAddSubmit(self, "manda")
html.endForm(self)

html.endContent(self)
html.endHtml(self)

%>

