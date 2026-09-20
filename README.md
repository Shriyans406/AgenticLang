# Agentic LangGraph

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your `.env` file:**
   - Get a Groq API key from https://console.groq.com
   - Get a Tavily API key from https://tavily.com
   - Replace the keys in `.env` with your own

3. **Important:** The `.env` file contains API keys. If you see `model_not_found` errors, update the model name in the notebook cells. Valid Groq model names include:
   - `llama-3.1-8b-versatile`
   - `llama-3.3-70b-versatile`
   - `mixtral-8x7b-32768`

## Running the Notebook

Open `1-BasicChatbot/1-basicchatbot.ipynb` in Jupyter and run cells in order (Ctrl+Enter for each cell).

## What Was Fixed

The notebook had numerous bugs that were all resolved:

1. **Missing/wrong imports** - `TypedDict`, `Annotated`, `add_messages`, `HumanMessage` now properly imported
2. **`StartGraph` → `StateGraph`** - Typo in graph builder class name
3. **Node name mismatch** - `"llmchatbot"` → `"llamabot"` for consistent edge connections
4. **`max_results-2` → `max_results=2`** - Minus sign was wrong, should be equals
5. **`messsages` → `messages`** - Typo in return dict key
6. **`graph_builder.compile()` not assigned** - Result now assigned to `graph`
7. **Missing function in `add_node`** - `add_node("tool_colling_llm",)` had no function argument
8. **`builder` vs `graph_builder` inconsistency** - Standardized on `builder` and `graph`
9. **`m.pretty.print` → `m.pretty.print()`** - Missing parentheses
10. **String instead of message objects** - `graph.invoke("Hi")` → `graph.invoke({"messages": [HumanMessage(content="Hi")]})`
11. **`init_chat_model` wrong import path** - Changed from `langchain.chat_model` to `langchain.chat_models`
12. **`tools_condition` edge direction** - Fixed `builder.add_edge("tools", "tool_calling_llm")` → `builder.add_edge("tools", END)`
