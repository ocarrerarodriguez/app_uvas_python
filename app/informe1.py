import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors, styles
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
def informe_gsm(archivo,datos,x,y):
    #TTFont(nombre, archivo)

    print(datos)
    pdfmetrics.registerFont(TTFont('verdana', 'verdana.ttf'))

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name ='center',  alignment=TA_CENTER, fontSize=36,fontName="verdana"))

    doc = SimpleDocTemplate(archivo, pagesize=A4)
    # container for the 'Flowable' objects
    elements = []

    ptitulo1 = '<font size=36>ADENEIRA</font>'
    ptitulo2= '<font size=36>el mejor albariño</font>'
    ptitulo3 = '<font size=36>que puedas imaginar</font>'

    elements.append(Paragraph(ptitulo1, styles["center"]))
    elements.append(Spacer(1, 36))

    elements.append(Paragraph(ptitulo2, styles["center"]))
    elements.append(Spacer(1, 36))

    elements.append(Paragraph(ptitulo3, styles["center"]))
    elements.append(Spacer(1, 36))

    data = [[datos[1][0], datos[1][1], datos[1][2], datos[1][3], datos[1][4], datos[1][5], datos[1][6], datos[1][7], datos[1][8], datos[1][9], datos[1][10], datos[1][11], datos[1][12], datos[1][13], datos[1][14], datos[1][15]],
            [ datos[2][0], datos[2][1], datos[2][2], datos[2][3], datos[2][4], datos[2][5], datos[2][6], datos[2][7], datos[2][8], datos[2][9], datos[2][10], datos[2][11], datos[2][12], datos[2][13], datos[2][14], datos[2][15]],
            [ datos[3][0], datos[3][1], datos[3][2], datos[3][3], datos[3][4], datos[3][5], datos[3][6], datos[3][7], datos[3][8], datos[3][9], datos[3][10], datos[3][11], datos[3][12], datos[3][13], datos[3][14], datos[3][15]],
            [ datos[4][0], datos[4][1], datos[4][2], datos[4][3], datos[4][4], datos[4][5], datos[4][6], datos[4][7], datos[4][8], datos[4][9], datos[4][10], datos[4][11], datos[4][12], datos[4][13], datos[4][14], datos[4][15]],
            [ datos[5][0], datos[5][1], datos[5][2], datos[5][3], datos[5][4], datos[5][5], datos[5][6], datos[5][7], datos[5][8], datos[5][9], datos[5][10], datos[5][11], datos[5][12], datos[5][13], datos[5][14], datos[5][15]],
            [ datos[6][0], datos[6][1], datos[6][2], datos[6][3], datos[6][4], datos[6][5], datos[6][6], datos[6][7], datos[6][8], datos[6][9], datos[6][10], datos[6][11], datos[6][12], datos[6][13], datos[6][14], datos[6][15]],
            [ datos[7][0], datos[7][1], datos[7][2], datos[7][3], datos[7][4], datos[7][5], datos[7][6], datos[7][7], datos[7][8], datos[7][9], datos[7][10], datos[7][11], datos[7][12], datos[7][13], datos[7][14], datos[7][15]],
            [ datos[8][0], datos[8][1], datos[8][2], datos[8][3], datos[8][4], datos[8][5], datos[8][6], datos[8][7], datos[8][8], datos[8][9], datos[8][10], datos[8][11], datos[8][12], datos[8][13], datos[8][14], datos[8][15]]]
    print("x:"+str(x),"y:"+str(y))

    t = Table(data)
    t.setStyle(TableStyle([('ALIGN',        (x, y), (0, 0), 'CENTER'),
                           ('TEXTCOLOR',    (x, y), (0, 0), colors.black),
                           ('VALIGN',       (x, y), (0, 0), 'MIDDLE'),
                           ('INNERGRID',    (0, 0), (-1, -1), 0.25, colors.black),
                           ('BOX',          (0, 0), (-1, -1), 0.25, colors.black),
                           ]))


    elements.append(t)
    # write the document to disk
    doc.build(elements)


