from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    START,
    END
)

from langchain_core.messages import (
    HumanMessage,
    SystemMessage
)

from src.llm import get_llm
from src.agent import local_analysis


class AnalystState(TypedDict, total=False):

    df: object

    columns: dict

    question: str

    local_result: str

    route: str

    answer: str

    error: str


def analyze_question(state: AnalystState):

    question = state["question"]

    result = local_analysis(
        state["df"],
        state["columns"],
        question
    )

    if result is not None:

        return {
            "local_result": result,
            "route": "local"
        }

    return {
        "route": "ai"
    }


def route_question(state: AnalystState):

    if state["route"] == "local":

        return "local_answer"

    return "ai_reasoning"


def local_answer(state: AnalystState):

    return {
        "answer": state["local_result"]
    }


def ai_reasoning(state: AnalystState):

    try:

        llm = get_llm()

        columns = state["columns"]

        question = state["question"]

        prompt = f"""
You are an AI Data Analyst.

You are analyzing a dataset.

Available business columns:
{columns}

User question:
{question}

Important rules:

1. Do not invent numerical values.
2. If exact calculations are required, explain that the
   available local analysis should be used.
3. Give concise and useful business insights.
4. Clearly mention when a required column is unavailable.
5. Do not claim something that cannot be supported by the data.
"""

        response = llm.invoke(
            [
                SystemMessage(
                    content=prompt
                ),
                HumanMessage(
                    content=question
                )
            ]
        )

        return {
            "answer": response.content
        }

    except Exception as e:

        error_text = str(e)

        if (
            "RESOURCE_EXHAUSTED" in error_text
            or "429" in error_text
        ):

            return {
                "answer": (
                    "Gemini API quota is currently exhausted. "
                    "The local Pandas analysis is still available. "
                    "Please try again after the Gemini quota resets."
                ),
                "error": error_text
            }

        return {
            "answer": (
                f"AI analysis failed: {error_text}"
            ),
            "error": error_text
        }


def build_graph():

    workflow = StateGraph(
        AnalystState
    )

    workflow.add_node(
        "analyze_question",
        analyze_question
    )

    workflow.add_node(
        "local_answer",
        local_answer
    )

    workflow.add_node(
        "ai_reasoning",
        ai_reasoning
    )

    workflow.add_edge(
        START,
        "analyze_question"
    )

    workflow.add_conditional_edges(
        "analyze_question",
        route_question,
        {
            "local_answer": "local_answer",
            "ai_reasoning": "ai_reasoning"
        }
    )

    workflow.add_edge(
        "local_answer",
        END
    )

    workflow.add_edge(
        "ai_reasoning",
        END
    )

    return workflow.compile()