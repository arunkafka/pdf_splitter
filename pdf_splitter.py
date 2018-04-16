'--------Author Arun------------'
'-------Created 03.04.2018-----'
from PyPDF2 import PdfFileReader, PdfFileWriter
import re


def pdf_splitter(wordpattern): 
    pdfFileObj = PdfFileReader(open('filename.pdf', "rb")) # file path.
    pdf_writer = PdfFileWriter()
    pagenumber = pdfFileObj.getNumPages()
    startpage = [] # number of start pages for the subfile or newfile which is created by splitting the pdf base on some pattern/text/content.
    naming = []

    for i in range(1, pagenumber):
        page = pdfFileObj.getPage(i)
        content = (page.extractText())
        if (re.search((wordpattern), content)):
            startpage.append(i)
            name = re.search(wordpattern, content)
            naming.append(name.group())
    print(startpage)

    for k in range(0, (len(startpage))):
            try:
                x, y = startpage[k], startpage[k + 1]

                for m in range(x, y):
                    page = pdfFileObj.getPage(m)
                    pdf_writer.addPage(page)
            except:
                print("Reached Last page")
                for m in range(y, pagenumber):
                    page = pdfFileObj.getPage(m)
                    pdf_writer.addPage(page)
            newpdf = (open('newfilenames%s.pdf' % naming[k], "wb"))# The nefiles/subfiles are created here.
            pdf_writer.write(newpdf)
            newpdf.close
            pdf_writer = PdfFileWriter()


if __name__ == "__main__":
    pdf_splitter('/d{4}') #give some word pattern or word with which you want to split the file.
                          #--For example I have give /d{4},which means pdf file will split into new files  at places where 4 digit numbers are there.
