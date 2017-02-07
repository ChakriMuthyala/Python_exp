import os    
import pdfkit
pdfkit.from_file("C:\\Users\\user\Desktop\\table.html", "out.pdf")
os.startfile("out.pdf", "print")
