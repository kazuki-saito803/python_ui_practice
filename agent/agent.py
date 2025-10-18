import os

from dotenv import load_dotenv
from langgraph.graph import StateGraph, MessageState
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import Field, BaseModel


class AgentState(BaseModel):
    current_step: int = Field(default=0, description="This is step.")
    state: str = Field(default="", description="This is state.")

load_dotenv()

GEMINI_MODEL = os.getenv("GEMINI_MODEL")

def decide_next(state: MessageState) -> str:
    last_message = state["messages"][-1]
    # last_messageの属性にtool_callsが含まれており、その値が空出ない場合、
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools_edge"
    return "end"

def call_llm(state: MessageState) -> str:
    system_prompt = ""
    messages = state["messages"]
    # 最初の一回だけシステムメッセージを入れる
    if not any(isinstance(msg, SystemMessage) for msg in messages):
        messages = [SystemMessage(content=system_prompt)] + messages
    llm = ChatGoogleGenerativeAI(model=GEMINI_MODEL)
    response = llm.bind_tools([]).invoke()
    
    return {"messages": messages + [response]}

if __name__ == '__main__':
    print(GEMINI_MODEL)