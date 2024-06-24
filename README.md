# Banco de dados couchdb  

## Projeto Acadêmico  

Fatec de Itapira "Ogari de Castro Pacheco"  
Disciplina – Banco de Dados Não Relacional - DSM

SEGUNDA ATIVIDADE AVALIATIVA

Professor Mateus Fuini

**Desenvolvido pelos alunos**  

André Fonseca - [Github](https://github.com/FonsecaAndre)  

Iago Almeida - [Github](https://github.com/Iagooalmeida)  

Site: [www.fatecitapira.edu.br](https://www.fatecitapira.edu.br)

Rua Tereza Lera Paoletti, 590 • Jardim Bela Vista • 13974-080 • Itapira • SP • Tel.: (19) 3843-7537  

## Gerenciamento de Frota de Carros com Flask e CouchDB  

Este é um sistema simples para gerenciar uma frota de carros utilizando Flask como framework web e CouchDB como banco de dados NoSQL.

### Estrutura do Projeto  

- Configuração do Ambiente
- Back-end com Python (Flask)
- Operações CRUD para Carros
- Interface de Usuário Simples com Flask

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- pip (gerenciador de pacotes do Python)
- Flask
- CouchDB
- Virtualenv (opcional, mas recomendado)

## Instalação e Configuração

### 1. Clonar o repositório

Clone este repositório do GitHub:

```bash
git clone https://github.com/FonsecaAndre/couchdb
cd car_fleet
```

### 2. Configurar o Ambiente Virtual (opcional)

É uma boa prática usar um ambiente virtual para isolar as dependências do projeto:  

```bash
python -m venv venv
source venv/bin/activate  # No Windows use venv\Scripts\activate
```  

### 3. Instalar Dependências  

Instale as dependências listadas no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```  

### 4. Configuração do CouchDB  

Certifique-se de ter o CouchDB instalado e executando localmente.
Configure a URL de conexão no arquivo `app.py` na seção onde se conecta ao CouchDB (`couchdb.Server()`).

### 5. Executar o Aplicativo  

Inicie o servidor Flask  

```bash
python app.py
```  

O aplicativo estará disponível em [http://127.0.0.1:5000](http://127.0.0.1:5000/)  

Esse modelo de `README.md` deve fornecer uma documentação clara e completa do seu projeto, facilitando o entendimento e a configuração por parte de outros desenvolvedores e usuários interessados.
