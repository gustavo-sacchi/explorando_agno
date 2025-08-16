from dotenv import load_dotenv

load_dotenv()

from textwrap import dedent

from agno.agent import Agent

from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

from agno.models.openai import OpenAIChat

from agno.storage.sqlite import SqliteStorage


## Banco para armazenar a sessão:
agent_storage = SqliteStorage(table_name="agent_sessions", db_file="data.db")

## Banco para servir de memória para o agente:
memoria_agente = Memory(
    db=SqliteMemoryDb(
        table_name="agent_memory",
        db_file="agent_memory.db",
    ),
)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    user_id="Gustavo", ### user ID
    session_id="1", ### sessão ID
    memory=memoria_agente,
    enable_user_memories=True,
    enable_session_summaries=True,
    storage=agent_storage, ### banco da sessão
    add_history_to_messages=True,
    num_history_responses=3,
    description=dedent("""\
        Você é um assistente de IA útil e amigável com excelente memória.
        - Lembre-se de detalhes importantes sobre os usuários e referencie-os naturalmente
        - Mantenha um tom caloroso e positivo enquanto é preciso e útil
        - Quando apropriado, refira-se a conversas e memórias anteriores
        - Sempre seja honesto sobre o que você lembra ou não lembra"""),
)

while True:
    message = input("Entre com a mensagem:")
    if message in ['q']:
        break

    agent.print_response(message=message, stream=True, markdown=True)
    print("")

