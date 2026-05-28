from fastapi import FastAPI, HTTPException, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
import json
from livekit.api import AccessToken

load_dotenv()

app = FastAPI(title="Friday - AI Personal Assistant")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# LiveKit Configuration
LIVEKIT_URL = os.getenv("LIVEKIT_URL", "wss://friday-4qy4pvd9.livekit.cloud")
LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY", "APIY4v43QZkDbwb")
LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET", "3ScKXo4OuUhhUOQyVFfw4WEdxaO0jgFeOZf48yKBuqgA")


class TokenRequest(BaseModel):
    room: str
    username: str


class TokenResponse(BaseModel):
    token: str
    url: str


@app.get("/")
async def root():
    """Serve the main HTML page."""
    return FileResponse("index.html", media_type="text/html")


@app.get("/config")
async def get_config():
    """Get LiveKit configuration."""
    return {
        "livekit_url": LIVEKIT_URL,
        "has_credentials": bool(LIVEKIT_API_KEY and LIVEKIT_API_SECRET)
    }


@app.post("/token")
async def generate_token(request: TokenRequest) -> TokenResponse:
    """Generate LiveKit access token for a participant."""
    
    try:
        # Try to create real token if credentials are available
        if LIVEKIT_API_KEY and LIVEKIT_API_SECRET:
            try:
                token = AccessToken(
                    api_key=LIVEKIT_API_KEY,
                    api_secret=LIVEKIT_API_SECRET,
                    identity=request.username,
                    name=request.username,
                    grants={
                        "room": request.room,
                        "roomJoin": True,
                        "canPublish": True,
                        "canPublishData": True,
                        "canSubscribe": True,
                    }
                )
                
                return TokenResponse(
                    token=token.to_jwt(),
                    url=LIVEKIT_URL
                )
            except Exception as e:
                print(f"Error creating LiveKit token: {str(e)}")
                # Fall back to mock mode
        
        # Mock mode - return test token for development
        mock_token = f"test-token-{request.username}-{request.room}"
        return TokenResponse(
            token=mock_token,
            url=LIVEKIT_URL or "wss://test.livekit.io"
        )
    
    except Exception as e:
        print(f"Token generation error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/clear/{session_id}")
async def clear_conversation(session_id: str):
    """Clear session."""
    return {"status": "cleared", "session_id": session_id}


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "running",
        "service": "Friday - LiveKit Voice Agent",
        "livekit_configured": bool(LIVEKIT_API_KEY and LIVEKIT_API_SECRET)
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
