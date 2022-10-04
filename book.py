import PyPDF2
# pdfFile = open('the-india-way.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFile)
# print(pdfReader.numPages)
# # for i in range(10,pdfReader.numPages):
# #     pageObj = pdfReader.getPage(i)
# #     if pageObj.extractText().strip():
# #         print(len(pageObj.extractText()))
# #         print(pageObj.extractText().replace("     "," "))
# #         break
# hold = pdfReader.getPage(10).extractText().replace("\t"," ")
# print(hold)
class Book:
    def __init__(self,name:str) -> None:
        """name is the name of the pdf file"""
        pdfFile = open(name, 'rb')
        self.pdfReader = PyPDF2.PdfFileReader(pdfFile)
        self.page = self.pdfReader.numPages
    
    def get_page(self,page:int) -> str:
        return self.pdfReader.getPage(page).extractText().replace("\t"," ")
    
    def first_page_with_text(self) -> int:
        for i in range(self.page):
            pageObj = self.pdfReader.getPage(i)
            if pageObj.extractText().strip():
                return i
        return -1
    
    def extract_book(self)  -> str:
        first_page = self.first_page_with_text()
        if first_page == -1:
            return ""

        return "".join(self.get_page(i) for i in range(first_page,self.page))
            
