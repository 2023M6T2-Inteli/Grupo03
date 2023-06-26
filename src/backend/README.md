## Intruções para rodar o backend:

- Entre na pasta ```src/backend``` e instale as dependêcias essenciais para o projeto: ```pip install -r requirements.txt```.

- Entre na pasta ```src/backend```  e rode ``` make env_template``` para criar um modelo de arquivo de variáveis de ambiente, o qual deve ser preenchido com o conteúdo apontado.

- Entre na pasta ```src/backend``` e rode ```python app.py``` para rodar o servidor.

## Modele o banco de dados no Supabase:

```
CREATE TABLE reports (
    id SERIAL PRIMARY KEY,
    nome_local VARCHAR,
    endereco VARCHAR,
    data VARCHAR,
    observacoes VARCHAR,
    gas INT
);
```
