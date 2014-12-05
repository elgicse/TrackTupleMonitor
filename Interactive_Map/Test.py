import bokeh.plotting as bk
from bokeh.charts import Histogram
from bokeh.objects import HoverTool
from bokeh.plotting import curplot
from collections import OrderedDict
from IPython.display import Image

i = Image(filename='../ST/doodle.png')


bk.output_file("Test.html",title = "Test Title")


xs = [0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7]

ys = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2]

zeros = [0] * len(xs)
ones = [0.5] * len(xs)

data = {}
for d in xs:
    data[str(d)] = d**2


bk.rect(xs,    # x-coordinates
         ys,    # y-coordinates
         ones,  # widths
         ones,  # heights
         fill_color="steelblue",
         tools = "hover")

hover = curplot().select(dict(type=HoverTool))
hover.tooltips = OrderedDict([
    ("index", "$index"),
    ("(x,y)", "($x, $y)"),
    ("radius", "@radius"),
    ("fill color", "$color[hex, swatch]:fill_color"),
    ("foo", "@foo"),
    ("bar", "@bar"),
])


bk.hold()

bk.save()
bk.show()

#hist = Histogram(data, bins=5, filename = "Test.html")
#hist.show()
