# Purchase System

## Como rodar localmente

Para rodar a aplicação localmente só é necessário 3 programas: `Docker`, `Docker-compose` e `make`.
Caso não saiba como obter algum deles busque a documentação oficial de cada projeto.

* Crie uma pasta para o projeto rodando `mkdir purchase-system`
* Depois clone o projeto para essa pasta rodando `git clone git@github.com:tamercuba/purchase-system.git purchase-system`
* Agora rode `make build` para criar a primeira imagem do projeto
* Para finalizar, rode `make run-dev` para rodar a aplicação

Este projeto foi pensado para utilizar docker em todas as instancias do desenvolvimento local,
rodar essa aplicação fora de um container fica por sua conta e risco.



