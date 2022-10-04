import PyPDF2

class Book:
    """
    Class to extract book pages
    """
    def __init__(self,name:str) -> None:
        """name is the name of the pdf file"""
        pdfFile = open(name, 'rb')
        self.pdfReader = PyPDF2.PdfFileReader(pdfFile)
        self.page = self.pdfReader.numPages
        self.first_page = self.first_page_with_text()
    
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
            
