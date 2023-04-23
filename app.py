from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Patrimonio, Setor
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
patrimonio_tag = Tag(
    name="patrimonio", description="Adição, visualização e remoção de patrimonios à base")
setor_tag = Tag(
    name="setor", description="Adição de um setor à um patrimonios cadastrado na base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/patrimonio', tags=[patrimonio_tag],
          responses={"200": PatrimonioViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_patrimonio(form: PatrimonioSchema):
    """Adiciona um novo patrimonio à base de dados
    Retorna uma representação dos Patrimonios.
    """
    patrimonio = Patrimonio(
        nome=form.nome,
        quantidade=form.quantidade,
        valor=form.valor,
        fabricante=form.fabricante,
        modelo=form.modelo,
        setor=form.setor)
    logger.debug(f"Adicionando patrimonio de nome: '{patrimonio.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando patrimonio
        session.add(patrimonio)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado patrimonio de nome: '{patrimonio.nome}'")
        return apresenta_patrimonio(patrimonio), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Patrimonio de mesmo nome já salvo na base :/"
        logger.warning(
            f"Erro ao adicionar patrimonio '{patrimonio.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(
            f"Erro ao adicionar patrimonio '{patrimonio.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/patrimonios', tags=[patrimonio_tag],
         responses={"200": ListagemPatrimoniosSchema, "404": ErrorSchema})
def get_patrimonios():
    """Faz a busca por todos os patrimonio cadastrados
    Retorna uma representação da listagem de patrimonios.
    """
    logger.debug(f"Coletando patrimonios ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    patrimonios = session.query(Patrimonio).all()

    if not patrimonios:
        # se não há patrimonios cadastrados
        return {"patrimonios": []}, 200
    else:
        logger.debug(f"%d patrimonios econtrados" % len(patrimonios))
        # retorna a representação de patrimonio
        print(patrimonios)
        return apresenta_patrimonios(patrimonios), 200


@app.get('/patrimonio', tags=[patrimonio_tag],
         responses={"200": PatrimonioViewSchema, "404": ErrorSchema})
def get_patrimonio(query: PatrimonioBuscaSchema):
    """Faz a busca por um patrimonio a partir do id do patrimonio
    Retorna uma representação dos patrimonios e comentários associados.
    """
    patrimonio_id = query.id
    logger.debug(f"Coletando dados sobre patrimonio #{patrimonio_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    patrimonio = session.query(patrimonio).filter(
        patrimonio.pk_patrimonio == patrimonio_id).first()

    if not patrimonio:
        # se o patrimonio não foi encontrado
        error_msg = "patrimonio não encontrado na base :/"
        logger.warning(
            f"Erro ao buscar patrimonio '{patrimonio_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"patrimonio econtrado: '{patrimonio.nome}'")
        # retorna a representação de patrimonio
        return apresenta_patrimonio(patrimonio), 200


@app.delete('/patrimonio', tags=[patrimonio_tag],
            responses={"200": PatrimonioDelSchema, "404": ErrorSchema})
def del_patrimonio(query: PatrimonioBuscaSchema):
    """Deleta um patrimonio a partir do nome de patrimonio informado
    Retorna uma mensagem de confirmação da remoção.
    """
    patrimonio_nome = unquote(unquote(query.nome))
    print(patrimonio_nome)
    logger.debug(f"Deletando dados sobre patrimonio #{patrimonio_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(patrimonio).filter(
        patrimonio.nome == patrimonio_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado patrimonio #{patrimonio_nome}")
        return {"mesage": "patrimonio removido", "id": patrimonio_nome}
    else:
        # se o patrimonio não foi encontrado
        error_msg = "patrimonio não encontrado na base :/"
        logger.warning(
            f"Erro ao deletar patrimonio #'{patrimonio_nome}', {error_msg}")
        return {"mesage": error_msg}, 404


@app.post('/setor', tags=[setor_tag],
          responses={"200": SetorSchema, "404": ErrorSchema})
def add_setor(form: SetorSchema):

    # criando conexão com a base
    session = Session()
    # criando o setor
    setor = Setor(
        nome=form.nome,
    )

    session.add(setor)
    session.commit()
    return apresenta_setor(setor), 200
    logger.debug(f"Adicionado setor")


@app.get('/setores', tags=[setor_tag],
         responses={"200": SetorSchema, "404": ErrorSchema})
def get_setores():

    logger.debug(f"Coletando produtos ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    setores = session.query(Setor).all()

    if not setores:
        # se não há produtos cadastrados
        return {"setores": []}, 200
    else:
        logger.debug(f"%d rodutos econtrados" % len(setores))
        # retorna a representação de produto
        print(setores)
        return apresenta_setores(setores), 200
