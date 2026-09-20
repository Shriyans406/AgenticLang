# Agentic LangGraph

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your `.env` file** (already configured):
   ```
   GROQ_API_KEY=your_groq_key_here
   TAVILY_API_KEY=your_tavily_key_here
   ```
   - Get a Groq API key from https://console.groq.com
   - Get a Tavily API key from https://tavily.com

## Important Notes

- **Model name**: The notebook uses `openai/gpt-oss-20b` which supports both chat and tool calling
  - If this model is unavailable, check available models at https://console.groq.com/models
  - Update `ChatGroq(model='openai/gpt-oss-20b')` in Cell 3 of the notebook
- **Run cells in order**: Always run cells from top to bottom (Cell 0 → Cell 24)
- After changing `.env`, **restart the kernel** and re-run all cells

## Running the Notebook

1. Open `1-BasicChatbot/1-basicchatbot.ipynb` in Jupyter
2. **Restart the kernel** (Kernel → Restart)
3. Run all cells in order (Cell → Run All, or press Shift+Enter for each cell)

## What Was Fixed (All 15 Bugs)

1. **Missing/wrong imports** - `TypedDict`, `Annotated`, `HumanMessage` properly imported
2. **`StartGraph` → `StateGraph`** - Typo fixed
3. **Node name mismatch** - `"llmchatbot"` → `"llamabot"` consistent naming
4. **`max_results-2` → `max_results=2`** - Operator typo fixed
5. **`messsages` → `messages`** - Typo fixed
6. **`graph_builder.compile()` not assigned to `graph`** - Now properly assigned
7. **Missing function in `add_node`** - Added `tool_calling_llm` function
8. **`builder` vs `graph_builder` inconsistency** - Standardized references
9. **`m.pretty.print` → `print(m.content)`** - `HumanMessage` has no `.pretty` attribute
10. **String instead of message objects** - `graph.invoke("Hi")` → `graph.invoke({"messages": [HumanMessage(content="Hi")]})`
11. **`init_chat_model` wrong import path** - `langchain.chat_model` → `langchain.chat_models`
12. **`tools_condition` edge direction** - Fixed `builder.add_edge("tools", "tool_calling_llm")` → `builder.add_edge("tools", END)`
13. **Cell ordering** - `tools`, `llm_with_tool`, `tool_calling_llm` now defined before use
14. **Wrong model name** - `llama-3.1-8192` → `openai/gpt-oss-20b` (valid Groq model)
15. **`multiply` docstring** - Added proper docstring for `ToolNode` compatibility
