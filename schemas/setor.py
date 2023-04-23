from pydantic import BaseModel
from typing import List
from model.setor import Setor


class SetorSchema(BaseModel):
    """ Define como um novo setor a ser inserido deve ser representado
    """
    nome: str = "financeiro"


def apresenta_setor(setor: Setor):
    """ Retorna uma representação do patrimonio seguindo o schema definido em
        patrimonioViewSchema.
    """
    return {
        "id": setor.id,
        "nome": setor.nome
    }


def apresenta_setores(setores: List[Setor]):
    """ Retorna uma representação do patrimonio seguindo o schema definido em
        patrimonioViewSchema.
    """
    result = []
    for setor in setores:
        result.append({
            "nome": setor.nome,
        })

    return {"setores": result}
