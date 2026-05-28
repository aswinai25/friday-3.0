import logging
from dotenv import load_dotenv

from livekit.agents import (
    Agent,
    AgentServer,
    AgentSession,
    JobContext,
    cli,
    inference,
)
from livekit.plugins import silero

load_dotenv()

logger = logging.getLogger("friday")
logger.setLevel(logging.INFO)


class FridayPersonalAssistant(Agent):
    """Friday - Your Personal AI Friend & Assistant
    
    A helpful, friendly AI assistant that helps with:
    - Answering questions and providing information
    - Setting reminders and managing tasks
    - General conversation and support
    - Learning and problem-solving
    - Daily planning and organization
    """
    
    def __init__(self) -> None:
        super().__init__(
            instructions=(
                "You are Friday, a warm, friendly personal AI assistant. "
                "Think of yourself as a close friend who is always there to help. "
                "Be conversational, empathetic, and genuinely interested in helping the person. "
                "You can help with: "
                "- Answering questions about anything "
                "- Giving advice and suggestions "
                "- Setting reminders and organizing tasks "
                "- Learning new things together "
                "- Having meaningful conversations "
                "- Providing emotional support and encouragement "
                "- Brainstorming ideas "
                "- Problem-solving "
                "- General productivity and life coaching "
                "\n"
                "Personality traits: "
                "- Warm and approachable like a real friend "
                "- Patient and understanding "
                "- Encouraging and supportive "
                "- Honest and straightforward "
                "- Humorous when appropriate "
                "- Never judgmental "
                "\n"
                "Communication style: "
                "- Speak naturally as a friend would "
                "- Keep responses concise for voice conversation "
                "- Use a conversational tone "
                "- Be genuine and authentic "
                "- Remember context from the conversation "
                "- Show that you care about helping "
            ),
        )

    async def on_enter(self) -> None:
        """Greet the user when they join."""
        self.session.generate_reply(
            instructions="Greet the user warmly like a close friend. "
                        "Welcome them and ask how you can help them today. "
                        "Keep it natural and friendly, not robotic."
        )


server = AgentServer()


@server.rtc_session()
async def entrypoint(ctx: JobContext):
    """Main entrypoint for the personal voice assistant."""
    
    ctx.log_context_fields = {
        "room": ctx.room.name,
        "user": ctx.participant.identity,
    }
    
    # Create the agent session with speech-to-text, language model, 
    # text-to-speech, and voice activity detection
    session = AgentSession(
        vad=silero.VAD.load(),
        stt=inference.STT("deepgram/nova-3", language="multi"),
        llm=inference.LLM("openai/gpt-4-turbo"),
        tts=inference.TTS("cartesia/sonic-3"),
    )
    
    logger.info(f"Friday Assistant starting for {ctx.participant.identity} in room: {ctx.room.name}")
    
    # Start the agent
    await session.start(agent=FridayPersonalAssistant(), room=ctx.room)


if __name__ == "__main__":
    cli.run_app(server)
