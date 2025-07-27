import os
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

class TicketState(TypedDict):
    email_content: str
    summary: str
    priority: str
    category: str

def process_email(state: TicketState) -> TicketState:
    """Process incoming email and extract key information"""
    email_content = state.get("email_content", "")
    
    prompt = f"""
    Analyze this customer support email and provide:
    1. A brief summary (max 15 words)
    2. Priority level (High/Medium/Low)
    3. Category (Technical/Billing/General)
    
    Email: {email_content}
    
    Format your response as:
    Summary: [your summary]
    Priority: [priority level]
    Category: [category]
    """
    
    response = llm.invoke(prompt)
    
    # Parse the response
    lines = response.content.split('\n')
    summary = priority = category = ""
    
    for line in lines:
        if line.startswith('Summary:'):
            summary = line.replace('Summary:', '').strip()
        elif line.startswith('Priority:'):
            priority = line.replace('Priority:', '').strip()
        elif line.startswith('Category:'):
            category = line.replace('Category:', '').strip()
    
    return {
        "email_content": email_content,
        "summary": summary,
        "priority": priority,
        "category": category
    }

# Create the graph
workflow = StateGraph(TicketState)
workflow.add_node("process", process_email)
workflow.set_entry_point("process")
workflow.add_edge("process", END)

# Compile the agent
agent = workflow.compile()

def create_ticket(email_content: str) -> dict:
    """Main function to create a ticket from email content"""
    result = agent.invoke({"email_content": email_content})
    return result
