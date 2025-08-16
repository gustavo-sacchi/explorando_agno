from dotenv import load_dotenv
load_dotenv()

import asyncio

from agno.models.openai import OpenAIChat
from agno.team.team import Team

from agents.analista_financeiro import analista_financeiro
from agents.pesquisador_financeiro import pesquisador_financeiro

agent_team = Team(
    name="Equipe de Análise Financeira",
    mode="collaborate",
    model=OpenAIChat("gpt-4o"),
    members=[
        analista_financeiro,
        pesquisador_financeiro
    ],
    instructions=[
        "Você é o coordenador de uma equipe de análise financeira.",
        "Você deve parar a discussão quando a equipe chegar a um consenso sobre a análise.",
        "Certifique-se de que tanto a pesquisa quanto a análise técnica sejam abordadas.",
        "O relatório final deve ser abrangente e bem estruturado.",
    ],
    success_criteria="Produzir um relatório financeiro completo com pesquisa fundamentada e análise técnica detalhada.",
    enable_agentic_context=True,
    show_tool_calls=True,
    markdown=True,
    show_members_responses=True,
)



if __name__ == "__main__":
    asyncio.run(
        agent_team.aprint_response(
            message="Iniciem a análise sobre o tema: 'Análise completa das ações do Banco do Brasil SA (BBAS3.SA)'",
            stream=True
        )
    )

