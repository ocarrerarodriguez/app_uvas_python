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

    data = [["", '1', '2', '3', '4', '5', '6', '7', '8','9','10','11','12','13','14','15'],
            ['mical', '11', '12', '13', '14','','','','','','',''],
            ['branda', '21', '22', '23', '24','','','','','','',''],
            ['30', '31', '32', '33', '34','','','','','','','']]

    t = Table(data, x * [0.5 * inch], y * [0.4 * inch])
    t.setStyle(TableStyle([('ALIGN',        (x, y), (0, 0), 'CENTER'),
                           ('TEXTCOLOR',    (x, y), (0, 0), colors.black),
                           ('VALIGN',       (x, y), (0, 0), 'MIDDLE'),
                           ('INNERGRID',    (0, 0), (-1, -1), 0.25, colors.black),
                           ('BOX',          (0, 0), (-1, -1), 0.25, colors.black),
                           ]))

    elements.append(t)
    # write the document to disk
    doc.build(elements)


