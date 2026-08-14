#!/usr/bin/env python3
"""
AI-Powered Chatbot using Claude API
A fully working conversational chatbot that handles both interactive and piped input.
"""

import os
import sys

# Check if anthropic package is installed
try:
    from anthropic import Anthropic
except ImportError:
    print("Error: anthropic package not installed.")
    print("Install it with: pip install anthropic")
    sys.exit(1)

def create_chatbot():
    """Initialize the chatbot with Anthropic client."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("\nTo set it:")
        print("  Linux/Mac: export ANTHROPIC_API_KEY='your-key-here'")
        print("  Windows:   set ANTHROPIC_API_KEY=your-key-here")
        print("\nGet your API key at: https://console.anthropic.com/keys")
        sys.exit(1)
    
    try:
        return Anthropic(api_key=api_key)
    except Exception as e:
        print(f"Error initializing Anthropic client: {e}")
        sys.exit(1)

def run_chatbot():
    """Main chatbot loop for multi-turn conversation."""
    client = create_chatbot()
    conversation_history = []
    
    system_prompt = """You are a helpful and friendly AI assistant. 
Engage in natural, engaging conversations. Be concise but informative.
If asked for advice, provide thoughtful perspectives."""
    
    print("=" * 60)
    print("Welcome to Claude Chatbot!")
    print("Type 'quit', 'exit', or 'bye' to end the conversation.")
    print("=" * 60)
    print()
    
    try:
        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
            except EOFError:
                # Handle end of input (Ctrl+D or piped input exhausted)
                print("\nChatbot: Goodbye! 👋")
                break
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Chatbot: Thanks for chatting! Goodbye! 👋")
                break
            
            # Skip empty inputs
            if not user_input:
                continue
            
            # Warn if input is very long
            if len(user_input) > 2000:
                print("⚠️  Warning: Your message is very long. It may impact response quality.\n")
            
            # Add user message to conversation history
            conversation_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Limit conversation history to last 20 messages to avoid token overflow
            if len(conversation_history) > 20:
                conversation_history = conversation_history[-20:]
            
            try:
                # Show processing indicator
                print("Chatbot: ", end="", flush=True)
                
                # Get response from Claude
                response = client.messages.create(
                    model="claude-sonnet-5",
                    max_tokens=1024,
                    system=system_prompt,
                    messages=conversation_history
                )
                
                # Extract assistant response
                assistant_message = response.content[0].text
                
                # Add assistant response to conversation history
                conversation_history.append({
                    "role": "assistant",
                    "content": assistant_message
                })
                
                # Display response (clear the processing indicator)
                print(f"\r{assistant_message}\n")
                
            except KeyboardInterrupt:
                print("\n\nChatbot: Conversation interrupted. Goodbye! 👋")
                break
                
            except Exception as e:
                error_msg = str(e)
                print(f"\r❌ Error occurred")
                
                # Provide specific error guidance
                if "401" in error_msg or "invalid" in error_msg.lower():
                    print("   → API Key issue: Check your ANTHROPIC_API_KEY is valid")
                    print("   → Get key at: https://console.anthropic.com/keys")
                elif "429" in error_msg:
                    print("   → Rate limited: Too many requests. Wait a moment and try again.")
                elif "404" in error_msg:
                    print("   → Model not found: claude-sonnet-5 may not be available")
                elif "Connection" in error_msg or "Network" in error_msg:
                    print("   → Network error: Check your internet connection")
                else:
                    print(f"   → {error_msg}")
                print("   Please try again or type 'quit' to exit.\n")
    
    except KeyboardInterrupt:
        print("\n\nChatbot: Goodbye! 👋")

def main():
    """Entry point for the chatbot."""
    run_chatbot()

if __name__ == "__main__":
    main()
