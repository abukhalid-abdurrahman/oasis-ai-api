import sys
sys.path.insert(0, 'pkg/oasis_ai')

from pkg.oasis_ai.command_analyzer import CommandAnalyzer
from fastapi import FastAPI
from pydantic import BaseModel

class Command(BaseModel):
    cmd_text: str

class Answer(BaseModel):
    answer_text: str

class Ping(BaseModel):
    msg: str

commandAnalyzer = CommandAnalyzer()
app = FastAPI()

@app.get("/api/ping")
async def ping() -> Ping:
    return Ping(msg="pong")

@app.post("/api/cmd/")
async def execute_cmd(cmd: Command) -> Answer:
    execution_result = commandAnalyzer.execute_command(cmd.cmd_text)
    query_result = str(execution_result['source'])
    return Answer(answer_text=query_result)
