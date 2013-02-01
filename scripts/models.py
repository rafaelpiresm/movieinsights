# -*- coding: utf-8 -*-
import couchdb
from couchdb.mapping import TextField, IntegerField, DateTimeField, Document
from datetime import datetime
import nltk

__SERVER__ = 'dbscripts'
__CONTENT_BY_TITLE__ = 'content_by_title/content_by_title'
__CONTENT_BY_AUTHOR__ = 'content_by_author/content_by_author'
__AUTHORS__ = 'all_authors/all_authors'
__TITLES__ = 'all_titles/all_titles'


class Termo:    
    def __init__(self, _id, titulo, densidade):
        self._id = _id
        self.titulo = titulo
        self.densidade = densidade

class Script(Document): 
    title = TextField()
    author = TextField()
    content = TextField()
    date = DateTimeField(default=datetime.now())
    
    def __getServer__(self):        
        server = couchdb.Server()
        db = server[__SERVER__]
        return db


    def getScriptByid(self, script_id):
        db = self.__getServer__()
        return Script.load(db, script_id)
    
    def getScriptsComplexSearch(self, term):
        db = self.__getServer__()
        lista = []
        tokensTerms = nltk.word_tokenize(term)
        for row in db.view(name=__CONTENT_BY_TITLE__):
            script = Script.load(db, row.id)        
    
    def getAuthors(self, author):
        db = self.__getServer__()
        lista = []
        for r in db.view(name=__AUTHORS__):
            if author.lower() in str(r.value.encode('utf-8')).decode('utf-8').lower():
                lista.append(Script.load(db, r.id))
        return lista
    
    
    def getTitles(self, title):
        db = self.__getServer__()
        lista = []
        for r in db.view(name=__TITLES__):
            if title.lower() in str(r.value.encode('utf-8')).decode('utf-8').lower():
                lista.append(Script.load(db, r.id))        
        return lista
    
                
    def getScriptByTitle(self, title):
        db = self.__getServer__()
        lista = []
        for r in db.view(name=__CONTENT_BY_TITLE__, key=title):
            lista.append(Script.load(db, r.id))
        return lista
    

    def getScriptsByAuthors(self, author):
        db = self.__getServer__()
        lista = []
        for r in db.view(name=__CONTENT_BY_AUTHOR__, key=author):
            lista.append(Script.load(db, r.id))
        return lista
    def get_tokens(self, term):
        return nltk.word_tokenize(term)
    
    def getDensidadeTermos(self, term):
        db = self.__getServer__()        
        tokensTermos = self.get_tokens(term) 
        results = {}       
        for r in db.view(name=__CONTENT_BY_TITLE__):
            tokensTexto = self.get_tokens(r.value)
            fdist = nltk.FreqDist(tokensTexto)
            lista = []            
            for t in tokensTermos:
                termo = Termo(r.id, r.key, 100 * fdist[t] / len(tokensTexto))
                lista.append(termo)
            return { r.key:lista[0].densidade }            
        return results
