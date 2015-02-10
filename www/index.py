<%

from server.page import html, textStyle
from server.managers import sessionManager

html.initHTML(self)
html.beginHead(self)
html.endHead(self)
html.beginContent(self)
html.addTitle(self, textStyle.italic("IT WORKS"))

print __GET__['haha'][0]
print sessionManager.readSessionKey(self)

try:
    print sessionManager.get(self, 'haha')

except Exception as e:
    print "exp " + str(e) + "-)"


try:

    sessionManager.set(self, 'haha', __GET__['haha'][0])
except Exception as e:
    print "exp " + str(e) + "-)"

<!-- PERL USAGE -->
<pl%

use area qw( areaOfCircle );

$areaOfFirstCircle = areaOfCircle(5);
print "The area of the circle is: $areaOfFirstCircle <br>";


print "Hello world of Perl command line". "<br>";
print "Hello world of Perl command line2";
%pl>




html.beginForm(self, "form2")
html.formAddInput(self, "text")
html.formAddSubmit(self, "manda")
html.endForm(self)

html.endContent(self)
html.endHtml(self)




%>
