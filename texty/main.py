import why
import texty.why_not as why_not
from why import upper as UP
from texty.why_not import Texty

text1 = why.title('this is just a test')
print(text1)

text2 = why_not.Texty()
print(text2.upper('attention, this is just a test'))

print(UP('lorem ipsum lorem ipsum'))

txt = Texty()
print(txt.lower('THIS IS PYTHON!!!'))

print(why.splitify('this is a test string to split apart...'))
