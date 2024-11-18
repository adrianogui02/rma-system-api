# RMA System API

Bem-vindo à **RMA System API**. Este projeto é uma API desenvolvida para um sistema de RMA.

## Stack utilizada

**Back-end:** Python e FastAPI

## Funcionalidades

- Gerenciamento de Produtos e Solicitações.
- Autenticação e autorização de usuários com JWT.
- Endpoints seguros e protegidos por autenticação.

## Instalação

Para configurar e rodar a **RMA System API**, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em seu sistema:

- [Python](https://www.python.org/)

### Passo a Passo

1. **Clone o repositório**

   Clone o repositório da API para seu ambiente local:

   ```bash
   git clone -b dev https://github.com/adrianogui02/rma-system-api.git
   ```

1. **Navegue até o diretório do projeto**

   Entre no diretório do projeto clonado:

   ```bash
   cd rma-system-api
   ```

1. **Rodando Localmente (Sem Docker)**

Se você optar por rodar a aplicação localmente sem Docker, siga os passos abaixo:

- Instale as dependências:

  ```bash
  pip install -r requirements.txt
  ```

- Inicie a aplicação:

  ```bash
  uvicorn src.main:app --reload

  ```

## Documentação da API

Documentacao com o Swagger pode ser acessada no link:

```bash
  http://localhost:8000/docs
```

## Autores

[@adrianogui02](https://github.com/adrianogui02)

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
