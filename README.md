<div align= "center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)![Firebase](https://img.shields.io/badge/firebase-a08021?style=for-the-badge&logo=firebase&logoColor=ffcd34)![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)

</div>

# Weather Playlists

## 🎺 Sobre o projeto

Projeto para a criação de uma API onde o usuário poderá solicitar recomendações de playlists baseadas na temperatura da cidade informada.
Vi nessa proposta uma boa oportunidade para criar esse projeto utilizando o FastAPI, que é amplamente recomendado pela comunidade de desenvolvedores Python, e aprofundar meus conhecimentos sobre o framework.

Projeto desenvolvido para uma avaliação técnica, ao longo da documentação trarei os detalhes sobre a aplicação.

Confira a [documentação da API](API.md).

---

## 💻 Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
    - O projeto foi concebido utilizando o framework FastAPI, devido sua alta performance, alta produtividade, forte tipagem e facilidade de implementação em ambientes Serverless.
    - O padrão de design e a estrutura de arquivos escolhido para construir esse serviço se inspira em três padrões: o padrão MVC, o padrão sugerido pela [documentação oficial](https://fastapi.tiangolo.com/tutorial/bigger-applications/) e a [sugestão de jankatins](https://github.com/zhanymkanov/fastapi-best-practices?tab=readme-ov-file#project-structure) inspirado no [Dispatch](https://github.com/Netflix/dispatch) da Netflix. Dessa forma, a aplicação pode ser facilmente interpretada, atualizada e receber novas features.
- [Google Cloud Run](https://cloud.google.com/run/)
    - A escolha de hospedagem no Google Cloud Run se dá pela possibilidade e facilidade de executar um ambiente serverless altamente escalável, garantindo a flexibilidade dos containers e a redução de custos.
    - Possui cota gratuíta, se tornando uma boa opção para low-budget.
- [Google Cloud Firestore](https://cloud.google.com/firestore)
    - Utilizando o Google Cloud Firestore para armazenamento de dados, podemos facilmente instanciar uma coleção e começar a trabalhar nela de imediato, sendo uma boa opção para não precisar gastar tempo configurando um banco de dados.
    - Garante a redução de custos, possuindo uma cota gratuíta.
- [Docker](https://www.docker.com/)
    - Apesar do Cloud Run permitir a execução direta da aplicação através do comando informado, decidi por incluir um Dockerfile, dessa forma facilita o desacoplamento do GCP, podendo ser facilmente adaptado para outros servidores.

## 📎 APIs externas

- [x] [Spotify](https://developer.spotify.com/)
    - API utilizada para buscar as playlists baseadas na categoria informada.
- [x] [OpenWeather](https://openweathermap.org/)
    - API utilizada para obter as coordenadas da localização informada e obter as condições de clima.

## ⚙️ Funcionalidades

- [x] Usuários:
  - [x] Criação de usuário
  - [x] Login (formulário com email e senha)
    - Autenticação através de [JWT](https://pyjwt.readthedocs.io/en/stable/)

- [x] Playlists:
  - [x] Buscar playlists baseadas nas condições atuais de temperatura
    - Temperatura abaixo de 10°C: playlist de músicas clássicas
    - Temperatura entre 10°C e 25°C: playlist de músicas de rock
    - Temperatura acima de 25°C: playlist de músicas pop
  - [x] Consultar playlists salvas na lista de favoritos
  - [x] Salvar playlist na lista de favoritos
  - [x] Deletar playlist da lista de favoritos

---

## 🚀 Como executar o projeto

### 💡 Pré-requisitos

- [x] python3.12 (garantir os pacotes python-dev e python-venv)
- [x] pip
- [x] git
- [x] gcloud (com conta configurada no GCP)

#### 💾 Rodando local

```bash

# Clonar repositório
$ git clone git@github.com:leandro-alvesc/weather-playlists.git

# Crie um arquivo .env de acordo com os campos contidos no arquivo .env.example
$ cat .env.example

# Crie e ative um ambiente virtual
$ python3.12 -m venv venv
$ source ./venv/bin/activate

# Instale as dependências
$ pip install -r requirements.txt

# Configure sua conta do Google Cloud, garantindo acesso ao SDK
$ gcloud init

# Garanta a autenticação na aplicação escolhida do gcloud
$ gcloud auth application-default login

# Execute a aplicação em modo de desenvolvimento
$ fastapi dev app/main.py

# O serviço será iniciado na porta 8000
# Abra a documentação Swagger acessando o endpoint:
$ localhost:8000/docs

```
