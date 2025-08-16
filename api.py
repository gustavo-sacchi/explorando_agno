from fastapi import FastAPI
from pydantic import BaseModel

from workflow import agent_team

app = FastAPI(title="Análise Financeira API", description="API para análise financeira colaborativa")


class Body(BaseModel):
    message: str


@app.post("/run")
async def run(body: Body):
    response = await agent_team.arun(body.message)
    return {"content": response.content}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", reload=False)

# uv run api.py
