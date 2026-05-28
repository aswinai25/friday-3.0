#!/usr/bin/env python
"""Test script to verify all imports and basic setup."""

import os
import sys
from dotenv import load_dotenv

print("=" * 60)
print("Friday 3.0 - Voice Agent Test")
print("=" * 60)

# Load environment
load_dotenv()
print("✓ Environment variables loaded")

# Check API keys
livekit_url = os.getenv("LIVEKIT_URL")
livekit_api_key = os.getenv("LIVEKIT_API_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

print(f"\nConfiguration:")
print(f"  LiveKit URL: {livekit_url[:30]}..." if livekit_url else "  LiveKit URL: NOT SET")
print(f"  LiveKit API Key: {'✓ SET' if livekit_api_key else '✗ NOT SET'}")
print(f"  OpenAI API Key: {'✓ SET' if openai_key else '✗ NOT SET'}")

if not openai_key:
    print("\n⚠ WARNING: OpenAI API key not set in .env file")
    print("  Please add OPENAI_API_KEY=sk-... to your .env file")
    sys.exit(1)

print("\n" + "=" * 60)
print("Testing Imports...")
print("=" * 60)

try:
    from livekit import agents
    print("✓ livekit.agents")
except Exception as e:
    print(f"✗ livekit.agents: {e}")
    sys.exit(1)

try:
    from livekit.plugins import openai, silero, google
    print("✓ livekit.plugins (openai, silero, google)")
except Exception as e:
    print(f"✗ livekit.plugins: {e}")
    sys.exit(1)

try:
    from livekit.agents.voice_assistant import VoiceAssistant
    print("✓ VoiceAssistant")
except Exception as e:
    print(f"✗ VoiceAssistant: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("✅ All tests passed! Application is ready to run.")
print("=" * 60)
print("\nNext step: python main.py")
print("This will start the voice agent server.")
