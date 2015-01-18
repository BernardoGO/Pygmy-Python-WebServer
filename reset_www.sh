rm -r www/* www/.*
echo "<%

from server.page import html, textStyle
from server.managers import sessionManager

html.initHTML(self)
html.beginHead(self)
html.endHead(self)
html.beginContent(self)
html.addTitle(self, textStyle.italic(\"IT WORKS\"))

html.endContent(self)
html.endHtml(self)

%>" >> www/index.py
