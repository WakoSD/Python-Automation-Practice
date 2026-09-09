#First we need to install pip camelot-py. It is for extracting the info drom the PDF. But first we need to install 2 dependencies. 
#So in this order:
#pip install tk
#pip install ghostscript
#pip install camelot-py

#Then we need to import camelot
import camelot
#Here we read the file on the exact directory
tables = camelot.read_pdf(
    r"C:\Users\Gino\Documents\Repositorios_Github\Python-Automation-Practice\P1-Table Extraction\foo.pdf",
    pages="1",
    flavor="stream"
)

print(tables)
#Export to csv
tables.export(
    r"C:\Users\Gino\Documents\Repositorios_Github\Python-Automation-Practice\P1-Table Extraction\foo.csv", f="csv", compress=True)
tables[0].to_csv(
    r"C:\Users\Gino\Documents\Repositorios_Github\Python-Automation-Practice\P1-Table Extraction\foo.csv")