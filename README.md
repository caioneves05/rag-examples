# RAG Examples - In-Memory API

Este projeto implementa uma API FastAPI para consultas semânticas em documentos armazenados na memória.

## Como executar o projeto

### 1. Instale as dependências
Certifique-se de que você tem o Python 3.11 instalado. Em seguida, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

### 2. Execute o servidor
Inicie o servidor FastAPI com o comando:

```bash
uvicorn main:app --reload
```

O servidor estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 3. Teste a API
Você pode testar a API usando a documentação interativa gerada automaticamente pelo FastAPI:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 4. Exemplo de consulta
Use o comando `curl` para enviar uma consulta para a API:

```bash
curl -X POST "http://127.0.0.1:8000/query" \
-H "Content-Type: application/json" \
-d '{"query": "japonês"}'
```

### Resposta esperada
A API retornará uma resposta JSON com os documentos mais relevantes para a consulta.

---

## Estrutura do projeto
- **`main.py`**: Contém a lógica principal da API.
- **`requirements.txt`**: Lista de dependências do projeto.

---

## Requisitos
- Python 3.11 ou superior
- Dependências listadas no `requirements.txt`

---

## Problemas comuns
### 1. `ModuleNotFoundError`
Certifique-se de que todas as dependências estão instaladas corretamente:
```bash
pip install -r requirements.txt
```

### 2. Erro ao importar `cached_download`
Se ocorrer um erro relacionado ao `huggingface_hub`, instale uma versão compatível:
```bash
pip install huggingface_hub==0.14.1
```

Se precisar de mais ajuda, consulte a documentação oficial do FastAPI ou entre em contato com o mantenedor do projeto.