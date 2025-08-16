from dotenv import load_dotenv

load_dotenv()

from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

import httpx

from markdownify import markdownify


## Tool Personalizada

# def buscar_conteudo_completo_site(url: str):
#     """
#     Busca o conteúdo HTML de uma URL e o converte para o formato markdown.
#
#     Utiliza um tempo limite de 10 segundos para evitar travamentos em sites lentos ou páginas muito grandes.
#     """
#     try:
#         with httpx.Client(timeout=10.0) as client:
#             response = client.get(url)
#             response.raise_for_status()
#             return markdownify(response.text)
#     except Exception as e:
#         print(f"Aviso: Falha ao buscar o conteúdo completo da página para {url}: {str(e)}")
#         return f"Aviso: Falha ao buscar o conteúdo completo da página para {url}: {str(e)}"

# --------------------- AGENTE --------------------

# Criar um Agente de Pesquisa
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions=dedent("""\
        Você é um pesquisador especializado que deve fornecer respostas completas e precisas.

        Para responder às perguntas:
        1. Use no máximo 3 sites diferentes para pesquisar informações
        2. Acesse os sites e leia todo o conteúdo.
        3. Busque fontes confiáveis e atualizadas
        4. Sintetize as informações de forma clara e objetiva
        5. Cite as fontes utilizadas ao final da resposta

        Seja conciso mas completo em suas respostas.\
    """),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

# Exemplo de uso
agent.print_response(
    "Pode me dizer sobre os últimos lançamentos da OpenAI?", stream=True
    # "O que tem nesse site de notícia hoje em https://br.investing.com/?", stream=True
)


