# Sales Register
> Um simples sistema para cadastro de compras

![Python Version][python-badge]

# Motivações
Esse sistema é um estudo de caso do modelo de arquitetura [Ports and adapters][hex-url],
além de ser meu primeiro contato com [Fast API][fast-api] e com [Autenticação JWT][jwt-auth].

## Um breve guia sobre a arquitetura do projeto

A ideia é implementar uma arquitetura em camadas, separando responsabilidades em cada
camada e isolando as regras de negócio/aplicação da solução técnica empregada no produto final.
Por mais que essa ideia adicione complexidade ao produto, a longo prazo ( pensando numa aplicação
grande com uma regra de negócio complexa, com diversas fontes de dados etc ) a promessa
é que essa complexidade se pague.


Sobre cada camada e suas responsabilidades:
### Domain ( Camada de dominio)
A ideia dessa camada é manter todas as regras de negócio e aplicação, independente
de serviços externos e demais soluções técnicas. Aqui temos duas "subcamadas" que são
as entidades (que são literalmente as entidades do business e seu respectivo comportamento)
e a camada de serviço (que implementa as regras especificas da aplicação).

A ideia principal é isolar essas camadas das implementações de persistência/distribuição dos dados. Exemplo:
numa mesma aplicação uma entidade pode viver num banco relacional e outra viver apenas num cache. Usando
essa solução nós conseguimos escrever toda a regra de negócio da nossa aplicação usando a mesma linguagem. Dessa forma não teremos por exemplo algumas entidades que são, digamos, `models` ( do django), outras
são apenas classes enquanto outras são `dicts` que são salvos no cache.

Falando sobre os serviços, obviamente ele precisam se comunicar com a camada de persistência ( por exemplo,
uma regra básica da aplicação é cadastrar um novo vendedor. É óbvio que isso necessita
de acesso a camada de persistência) porém ao invés de implementar uma dependencia direta
se utiliza o [Principio da inversão de dependências][dip] ( principio esse que é foi
utilizado durante todo o desenvolvimento da aplicação e em todas as camadas). Dessa forma
a camada de serviços depende apenas de `Interfaces` implementadas no submodulo `domain.ports`.

Vale ressaltar também que a camada de domínio não tem dependencia alguma de nenhuma outra camada.
Não sequer um import de dentro dessa camada que instancie algo de outra camada.

### Adapters
Essa camada implementa justamente a comunicação da camada de dominio com o mundo exterior.
Chamadas de APIs externas, bancos de dados etc.

## Instalação


Primeiro clone o projeto
```sh
mkdir sales_register && git clone git@github.com:tamercuba/sales-register.git sales_register
```

Agora crie seu `.env` rodando dentro da pasta do projeto `make make-env`

Para preencher a variavel `SECRET_KEY` você pode rodar `make generate-secret`

Escolha também uma pasta (recomendado ser fora da pasta do projeto) e coloque o endereço dessa pasta
na variável `LOCAL_DB_VOLUME`. Essa variável será utilizada para guardar
o volume local do postgres e não perder os dados assim que o container for derrubado.

Crie uma `virtualenv` e após ativa-la rode `make requirements-pip`

Agora para subir a aplicação basta roda `make build` seguido de `make run-dev`
( você pode optar por rodar `make run-dev-no-output` também). Após isso com o sistema de
pé rode `make run-migrations` para confiruar o banco.


## Exemplos de uso

No arquivo `contrib/api_test.http` existem exemplos de todas as requisições http
que o sistema suporta. Segue o exemplo da request para cadastro usando `curl`:
```sh
curl -X POST http://localhost:8000/register -H "Content-Type: application/json" --data '{"email": "exemplo@gmail.com","password": "aaaa","name": "exemplo","cpf": "123456"}'
```


<!-- Markdown link & img dfn's -->
[python-badge]: https://img.shields.io/badge/python-3.9-blue
[hex-url]: https://alistair.cockburn.us/hexagonal-architecture/
[fast-api]: https://fastapi.tiangolo.com/
[jwt-auth]: https://pypi.org/project/fastapi-jwt-auth/
[dip]: https://en.wikipedia.org/wiki/Dependency_inversion_principle
