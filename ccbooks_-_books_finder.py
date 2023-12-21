from cat.mad_hatter.decorators import tool
import json
import requests

@tool(return_direct=True)
def ccbooks(isbn, cat):
    """Very useful for looking up information about books by entering only the isbn of the book.
    The user input is the isbn code.
    Generally, the isbn code consists of 13 or 10 digits"""

    req = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:"+str(isbn))
    res=req.json()
    if(res["totalItems"]==0):
        bookResult="Libro non trovato"
    else:
        selflink=res["items"][0]["selfLink"]
        reqSelf=requests.get(selflink)
        resBook=reqSelf.json()
        bookTitle=resBook["volumeInfo"]["title"]
        bookAuthors=resBook["volumeInfo"]["authors"][0]
        bookPublisher=resBook["volumeInfo"]["publisher"]
        bookPublisherDate=str(resBook["volumeInfo"]["publishedDate"])
        bookDescription=resBook["volumeInfo"]["description"]
        bookIsbn=str(isbn)
        bookCategories=resBook["volumeInfo"]["categories"][0]
        bookPageCount=str(resBook["volumeInfo"]["pageCount"])
        bookImage=resBook["volumeInfo"]["imageLinks"]["thumbnail"]
        bookLanguage=resBook["volumeInfo"]["language"]
        bookGoogleLink=resBook["volumeInfo"]["previewLink"]
        bookResult="<br><img src='"+bookImage+"' ><br><b>Titolo:</b> "+bookTitle+"<br><b>Autore:</b> "+bookAuthors+"<br><b>Casa Editrice:</b> "+bookPublisher+"<br><b>Data di pubblicazione:</b> "+bookPublisherDate+"<br><b>Descrizione:</b> "+bookDescription+"<br><b>ISBN:</b> "+bookIsbn+"<br><b>Genere:</b> "+bookCategories+"<br><b>Numero di pagine:</b> "+bookPageCount+"<br><b>Lingua:</b> "+bookLanguage+"<br><b>Link libro:</b> <a href='"+bookGoogleLink+"'>Clicca QUI</a>"

    return bookResult
