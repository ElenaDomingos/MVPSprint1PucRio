from pydantic import BaseModel
from typing import Optional, List
from model.patrimonio import Patrimonio


class PatrimonioSchema(BaseModel):
    """ Define como um novo patrimonio a ser inserido deve ser representado
    """
    nome: str = "cadeira"
    quantidade: Optional[int] = 12
    valor: float = 125.50,
    fabricante: str = "Nova lar",
    modelo: str = "Cadeira gamer",
    setor: str = "TI"


class PatrimonioBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do patrimonio.
    """
    nome: str = "Teste"


class ListagemPatrimoniosSchema(BaseModel):
    """ Define como uma listagem de patrimonios será retornada.
    """
    patrimonios: List[PatrimonioSchema]


def apresenta_patrimonios(patrimonios: List[Patrimonio]):
    """ Retorna uma representação do patrimonio seguindo o schema definido em
        patrimonioViewSchema.
    """
    result = []
    for patrimonio in patrimonios:
        result.append({
            "nome": patrimonio.nome,
            "quantidade": patrimonio.quantidade,
            "valor": patrimonio.valor,
            "fabricante": patrimonio.fabricante,
            "modelo": patrimonio.modelo,
            "setor": patrimonio.setor
        })

    return {"patrimonios": result}


class PatrimonioViewSchema(BaseModel):
    """ Define como um patrimonio será retornado: patrimonio + comentários.
    """
    pk_patrimonio: int = 1
    nome: str = "Cadeira"
    quantidade: Optional[int] = 2
    valor: float = 125.50,
    fabricante: str = "Moveis legais",
    modelo: str = "Cadeira normal",
    setor: str = "financeiro"


class PatrimonioDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesagem: str
    nome: str


def apresenta_patrimonio(patrimonio: Patrimonio):
    """ Retorna uma representação do patrimonio seguindo o schema definido em
        patrimonioViewSchema.
    """
    return {
        "pk_patrimonio": patrimonio.pk_patrimonio,
        "nome": patrimonio.nome,
        "quantidade": patrimonio.quantidade,
        "valor": patrimonio.valor,
        "fabricante": patrimonio.fabricante,
        "modelo": patrimonio.modelo,
        "setor": patrimonio.setor
    }
