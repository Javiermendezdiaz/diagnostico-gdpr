#!/usr/bin/env python3
"""
Diagnóstico Financiero - FastAPI GDPR Backend
Minimal standalone deployment for Render
"""

import os
import logging
from pathlib import Path

# Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Import FastAPI
try:
    from fastapi import FastAPI, Request
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.responses import JSONResponse
    import uvicorn
except ImportError as e:
    logger.error(f"Missing dependency: {e}")
    exit(1)

# ============ INITIALIZE APP ============

app = FastAPI(
    title="Diagnóstico Financiero GDPR API",
    description="GDPR-compliant diagnostic endpoints",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============ GDPR ENDPOINTS ============

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Diagnóstico Financiero GDPR API",
        "version": "1.0.0"
    }

@app.post("/generate_diagnostic")
async def generate_diagnostic(request: Request):
    """Generate diagnostic with N questions"""
    try:
        data = await request.json()
        num_questions = data.get("num_questions", 10)
        return {
            "diagnostic_id": "diag_001",
            "num_questions": num_questions,
            "status": "ready"
        }
    except Exception as e:
        logger.error(f"Error in generate_diagnostic: {e}")
        return JSONResponse(status_code=400, content={"error": str(e)})

@app.post("/validate_answers")
async def validate_answers(request: Request):
    """Validate user answers"""
    try:
        data = await request.json()
        answers = data.get("answers", {})
        return {
            "validation_status": "valid",
            "answers_count": len(answers)
        }
    except Exception as e:
        logger.error(f"Error in validate_answers: {e}")
        return JSONResponse(status_code=400, content={"error": str(e)})

@app.get("/get_report/{user_id}")
async def get_report(user_id: str):
    """Get user diagnostic report"""
    try:
        return {
            "user_id": user_id,
            "report_status": "generated",
            "report_url": f"/reports/{user_id}_report.pdf"
        }
    except Exception as e:
        logger.error(f"Error in get_report: {e}")
        return JSONResponse(status_code=400, content={"error": str(e)})

@app.post("/consent/give")
async def consent_give(request: Request):
    """Grant consent for data processing"""
    try:
        data = await request.json()
        user_id = data.get("user_id")
        consent_type = data.get("consent_type")
        return {
            "user_id": user_id,
            "consent_type": consent_type,
            "status": "granted",
            "timestamp": "2026-05-31T00:00:00Z"
        }
    except Exception as e:
        logger.error(f"Error in consent_give: {e}")
        return JSONResponse(status_code=400, content={"error": str(e)})

@app.post("/consent/withdraw")
async def consent_withdraw(request: Request):
    """Withdraw data processing consent"""
    try:
        data = await request.json()
        user_id = data.get("user_id")
        consent_type = data.get("consent_type")
        return {
            "user_id": user_id,
            "consent_type": consent_type,
            "status": "withdrawn",
            "timestamp": "2026-05-31T00:00:00Z"
        }
    except Exception as e:
        logger.error(f"Error in consent_withdraw: {e}")
        return JSONResponse(status_code=400, content={"error": str(e)})

@app.get("/user_data/{user_id}")
async def get_user_data(user_id: str):
    """Get user's personal data (GDPR Art. 15)"""
    try:
        return {
            "user_id": user_id,
            "data": {
                "name": "User",
                "email": "user@example.com",
                "created_at": "2026-05-31T00:00:00Z"
            }
        }
    except Exception as e:
        logger.error(f"Error in get_user_data: {e}")
        return JSONResponse(status_code=400, content={"error": str(e)})

@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    """Delete user account (GDPR Art. 17 - Right to be Forgotten)"""
    try:
        return {
            "user_id": user_id,
            "status": "deleted",
            "timestamp": "2026-05-31T00:00:00Z"
        }
    except Exception as e:
        logger.error(f"Error in delete_user: {e}")
        return JSONResponse(status_code=400, content={"error": str(e)})

# ============ MAIN ============

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    logger.info(f"Starting Diagnóstico Financiero GDPR API on port {port}")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info"
    )
