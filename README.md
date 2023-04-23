# MVPSprint1PucRio
A parte do back-end do MVP do Sprint1 Desenvolvimento Full-stack básico

Este pequeno projeto foi realizado para o Sprint da Disciplina **Desenvolvimento Full Stack Básico**
Eu usei o projeto base da aula 3 que foi fornecido pelo professor, alterei ele para a minha ideia de projeto, criando novas funcionalidades. Porém, algumas partes eu deixei intactas, sem mudanças.

A ideia do projeto é a seguinte. O sistema cadastra os itens de património de uma empresa, porém primeiro o usuário precisa cadastrar pelo menos um setor da empresa, para que ele apareça na lista de setores no formulário de cadastro dos itens. O usuário pode cadastrar tantos setores quanto precisar.
Tem duas tabelas: setor e partimonio.

---

## Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte.

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

