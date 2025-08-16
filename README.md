# Explorando Agno

Este projeto faz parte de um tutorial do YouTube sobre o framework **Agno**, demonstrando como construir uma equipe de agentes de IA colaborativos para análise financeira.

# Tutorial Youtube:

Acompanhe a explicação do projeto assistindo meu video do youtube: https://youtu.be/EURwUhnHDmk

## Sobre o Projeto

O projeto implementa uma equipe de análise financeira composta por dois agentes especializados:

- **Pesquisador Financeiro**: Coleta informações atualizadas do mercado financeiro usando DuckDuckGo
- **Analista Financeiro**: Analisa dados financeiros usando ferramentas do Yahoo Finance (yfinance)

Os agentes trabalham colaborativamente para produzir relatórios financeiros abrangentes e bem estruturados.

## Pré-requisitos

- Python 3.13+
- [UV](https://docs.astral.sh/uv/) (Astral)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/gustavo-sacchi/explorando_agno.git
cd explorando_agno
```

2. Instale as dependências usando UV:
```bash
uv sync
```

3. Configure as variáveis de ambiente:
```bash
cp .env.exemplo .env
```
Edite o arquivo `.env` e adicione sua chave da API OpenAI:
```
OPENAI_API_KEY=sua_chave_aqui
```

## Como Executar

### Executar o workflow diretamente:
```bash
uv run workflow.py
```

### Executar a API:
```bash
uv run api.py
```

A API estará disponível em `http://localhost:8000` com documentação automática em `http://localhost:8000/docs`.

### Exemplo de uso da API:
```bash
curl -X POST "http://localhost:8000/run" \
     -H "Content-Type: application/json" \
     -d '{"message": "Análise completa das ações do Itaú Unibanco (ITUB4.SA)"}'
```