import sqlite3 as sq
import pandas as pd
import streamlit

BANCO_DE_DADOS = "alunos.db"

class BancoDeDados:
    
    def __init__(self, nome_db = BANCO_DE_DADOS):
        self.nome = nome_db
    def ligar_banco(self):
        conexao = sq.connect(self.nome_db)
        cursor = conexao.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS alunos(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       nota1 REAL NOT NULL,
                       nota2 REAL NOT NULL,
                       nota3 REAL NOT NULL,
                       media REAL NOT NULL,
                       situacao TEXT NOT NULL)""")
        conexao.commit()
        return conexao, cursor