from reportlab.graphics.shapes import *#报告制图形状
from reportlab.graphics.charts.lineplots import LinePlot#图表线状
from reportlab.graphics import renderPDF#渲染成PDF

drawing = Drawing(400,200)#绘图板大小

data = [
    (2018,5,113.2,114.2,112.2),
    (2018,6,112.8,115.8,109.2),
    (2018,7,111.2,116.7,106.2),
    (2018,8,109.1,131.2,99.2),
    (2018,9,105.6,94.5,84.8),
]

pred = [i[2] for i in data]
height = [i[3] for i in data]
low = [i[4] for i in data]
times = [i[0] + i[1]/12 for i in data]

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300

lp.data = [
    list(zip(times,pred)),
    list(zip(times,height)),
    list(zip(times,low))
]

lp.lines[0].strokeColor = colors.red
lp.lines[1].strokeColor = colors.green
lp.lines[2].strokeColor = colors.blue

drawing.add(lp)
renderPDF.drawToFile(drawing,"aaaa.pdf")