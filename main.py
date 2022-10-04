import pyttsx3


import PyPDF2


class Book:
    """
    Class to extract book pages
    """

    def __init__(self, name: str) -> None:
        """name is the name of the pdf file"""
        pdfFile = open(name, "rb")
        self.pdfReader = PyPDF2.PdfFileReader(pdfFile)
        self.page = self.pdfReader.numPages
        self.first_page = self.first_page_with_text()

    def get_page(self, page: int) -> str:
        return self.pdfReader.getPage(page).extractText().replace("\t", " ")

    def first_page_with_text(self) -> int:
        for i in range(self.page):
            pageObj = self.pdfReader.getPage(i)
            if pageObj.extractText().strip():
                return i
        return -1

    def extract_book(self) -> str:
        first_page = self.first_page_with_text()
        if first_page == -1:
            return ""

        return "".join(self.get_page(i) for i in range(first_page, self.page))


engine = pyttsx3.init()

book = Book("the-india-way.pdf")
engine.setProperty("voice", engine.getProperty("voices")[40].id)
for i in range(book.first_page, book.page):
    engine.say(book.get_page(i))
    engine.runAndWait()
    break
# for i,voice in enumerate(engine.getProperty('voices')):
#     engine.setProperty('voice', voice.id)
#     engine.say("Welcome to The India Way")
#     print(f"{voice.id} {voice.name} {str(i)}")
#     engine.runAndWait()


# voice = engine.getProperty('voices')[7]
# engine.setProperty('voice', voice.id)``
# for i, text in enumerate(texts, start=1):
#     engine.save_to_file(text, f"test{i}.mp3")
# engine.runAndWait()
# com.apple.speech.synthesis.voice.lekha Lekha 20
# com.apple.speech.synthesis.voice.rishi Rishi 32
# com.apple.speech.synthesis.voice.samantha Samantha 33
# com.apple.speech.synthesis.voice.tom.premium Tom 40
