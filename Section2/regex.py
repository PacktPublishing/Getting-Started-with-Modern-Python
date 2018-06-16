import re

print(re.match("[0-9a-f]","a"))
print(re.match("[0-9a-f]{2}","aa"))
print(re.match("[0-9a-f]{2}","ab"))
print(re.match("(?:0x|#)?((?:[0-9a-f]{2}){1,3})","0xa0"))
print(re.match("(?:0x|#)?((?:[0-9a-f]{2}){1,3})(?=[^0-9a-f]|$)","0xa0a"))
print(re.match("(?:0x|#)?((?:[0-9a-f]{2}){1,3})(?=[^0-9a-f]|$)","0xa0a4p"))
print(re.match("(?:0x|#)?((?:[0-9a-f]{2}){1,3})(?=[^0-9a-f]|$)","0xa0a4aa"))

print(re.match("([a-z])\\1","aa"))
print(re.match("([a-z])\\1","ab"))
print(re.match("([a-z])\\1\\1","bbc"))
print(re.match("([a-z])\\1\\1","bbb"))

pat="<([a-z]+)([^<]+)*(?:>(.*?)</\\1>|\s+ />)"
html_text = """
<div class="container">
     <img src="qed" />
</div>
<div class="panel" data-bind="some_value" data-for="$v in vals">
    <span class="msg"><a href="#" class="btn">A Message</a>
</div>
<span class="awesome">asd</span>
"""

print(re.findall(pat,html_text,re.MULTILINE|re.DOTALL))

print(re.sub("(['\"])(.*)(container|panel|btn)(.*)\\1","\\1\\2m-\\3\\4\\1",html_text))
