import uvicorn

from src.escola_api.api.v1 import aluno_controller
from src.escola_api.database.banco_dados import Base, engine
from src.escola_api.api.v1 import curso_controller
from src.escola_api.app import app

Base.metadata.create_all(bind=engine)
app.include_router(curso_controller.router)
app.include_router(aluno_controller.router)


# @router.get("/")
# def index():
#     return {"mensagem": "Olá mundo"}
#
#
# @router.get("/calculadora")
# def calculadora(numero1: int, numero2: int):
#     soma = numero1 + numero2
#     return {"soma": soma}
#
#
# # http://127.0.0.1:8000/processar-cliente?nome=Pedro&sobrenome=Pascal&idade=27
# @router.get("/processar-cliente")
# def processar_dados_cliente(nome: str, idade: int, sobrenome: str):
#     # nome_completo => snake_case
#     # NomeCompleto => PascalCase
#     # nomeCompleto => camelCase
#     # nome-completo => kebab-case
#     nome_completo = nome + " " + sobrenome
#     ano_nascimento = datetime.now().year - idade  # from datetime import datetime
#
#     if ano_nascimento >= 1990 and ano_nascimento < 2000:
#         decada = "decada de 90"
#     elif ano_nascimento >= 1980 and ano_nascimento < 1990:
#         decada = "decada de 80"
#     elif ano_nascimento >= 1970 and ano_nascimento < 1980:
#         decada = "decada de 70"
#     else:
#         decada = "decada abaixo de 70 ou acima de 90"
#
#     return {
#         "nome_completo": nome_completo,
#         "ano_nascimento": ano_nascimento,
#         "decada": decada,
#     }


# class CursoTradicional:
#     def __init__(self, id: int, nome: str, sigla: str):
#         self.id = id
#         self.nome = nome
#         self.sigla = sigla
# from dataclasses import dataclass, field


if __name__ == "__main__":
    uvicorn.run("main:app")
