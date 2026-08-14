# Claude Chatbot - Python Edition 🤖

A fully functional AI-powered conversational chatbot using Claude API.

## Features ✨

- Multi-turn conversations with memory
- Real-time responses from Claude
- Works in interactive and piped modes
- Proper error handling and recovery
- Automatic context management
- Support for Ctrl+D and Ctrl+C exit

## Prerequisites 📋

- Python 3.7+
- pip package manager
- Active internet connection
- Claude API key from [console.anthropic.com](https://console.anthropic.com/keys)

## Installation 🔧

### 1. Install Required Package

```bash
pip install anthropic
```

### 2. Set Your API Key

**Linux/Mac:**
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

**Windows (Command Prompt):**
```cmd
set ANTHROPIC_API_KEY=your-api-key-here
```

**Windows (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY='your-api-key-here'
```

**Permanent Setup (Linux/Mac):**
Add to `~/.bashrc` or `~/.zshrc`:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Then reload:
```bash
source ~/.bashrc  # or ~/.zshrc
```

## Usage 🚀

### Interactive Mode

```bash
python chatbot_fixed.py
```

Then type your messages:
```
You: Hello! How are you?
Chatbot: Hi there! I'm doing well, thanks for asking! How can I help you today?

You: Tell me a joke
Chatbot: Why don't scientists trust atoms? Because they make up everything!

You: quit
Chatbot: Thanks for chatting! Goodbye! 👋
```

**Exit Commands:**
- Type `quit`, `exit`, or `bye`
- Press `Ctrl+D` (Linux/Mac) or `Ctrl+Z + Enter` (Windows)
- Press `Ctrl+C` to force exit

### Piped Input Mode

```bash
echo "What's the capital of France?" | python chatbot_fixed.py
```

### Multiple Messages

```bash
(echo "Hi"; echo "Tell me a fun fact"; echo "quit") | python chatbot_fixed.py
```

### Save Output

```bash
python chatbot_fixed.py > chat_log.txt 2>&1
```

## Configuration 🎛️

### Change Model (Optional)

Edit line 64 in `chatbot_fixed.py`:
```python
model="claude-sonnet-5",  # Change to other models if available
```

Available models:
- `claude-sonnet-5` (recommended - fast & capable)
- `claude-opus-4-8` (more powerful)
- `claude-haiku-4-5-20251001` (fastest, lighter)

### Adjust Response Length

Edit line 65:
```python
max_tokens=1024,  # Change to any value 1-4096
```

### Customize Personality

Edit the system prompt (lines 25-28):
```python
system_prompt = """You are a helpful and friendly AI assistant. 
Engage in natural, engaging conversations. Be concise but informative.
If asked for advice, provide thoughtful perspectives."""
```
## Example Conversations 💬

### Example 1: Learning

```
You: Explain quantum computing in simple terms
Chatbot: Quantum computers use quantum bits (qubits) that can exist in 
multiple states simultaneously. Unlike regular bits (0 or 1), qubits can 
be 0, 1, or both at once (superposition). This allows quantum computers 
to solve certain problems much faster than classical computers.
```

### Example 2: Creative

```
You: Write a haiku about programming
Chatbot: Code lines flow like streams,
Logic gates dance in the night,
Bugs flee from the light.
```

### Example 3: Problem-Solving

```
You: How do I remove an item from a Python list?
Chatbot: You can remove an item from a Python list using:

1. list.remove(item) - removes the first occurrence
2. list.pop(index) - removes by index
3. del list[index] - deletes by index
4. list.clear() - removes all items
```

## Advanced Usage 🎓

### Create a Chat History File

```bash
cat > setup.txt << EOF
How does photosynthesis work?
Tell me about climate change
What are renewable energy sources?
quit
EOF

python chatbot_fixed.py < setup.txt
```

### Use with Other Programs

```bash
# Get response from chatbot and pipe to file
echo "Write a product description for a coffee shop" | python chatbot_fixed.py | tee output.txt

# Chain multiple commands
python chatbot_fixed.py | grep -i "error" || echo "No errors found"
```

### Batch Processing

```bash
for question in "What is AI?" "What is ML?" "What is DL?"; do
  echo "Q: $question"
  echo "$question" | python chatbot_fixed.py
  echo "---"
done
```

## License 📄

This script is provided as-is for educational purposes.

## Support 💬

For issues with the Claude API, visit:
- [Anthropic Documentation](https://docs.anthropic.com)
- [Anthropic Support](https://support.anthropic.com)
- [GitHub Issues](https://github.com/anthropics/anthropic-sdk-python)

---

**Happy chatting! 🎉**
