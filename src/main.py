from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from .agent import create_ticket

app = FastAPI(title="IntelliTicket API", description="AI-Powered Support Ticket Creation")

class EmailRequest(BaseModel):
    email_content: str

class TicketResponse(BaseModel):
    summary: str
    priority: str
    category: str
    original_email: str

@app.post("/create-ticket", response_model=TicketResponse)
async def create_support_ticket(request: EmailRequest):
    try:
        result = create_ticket(request.email_content)
        return TicketResponse(
            summary=result["summary"],
            priority=result["priority"],
            category=result["category"],
            original_email=result["email_content"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
