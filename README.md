# AI Research Agent

> A fully autonomous AI agent built from scratch in Python for intelligent research and information processing

![Python](https://img.shields.io/badge/python-3.8+-blue)
![LangChain](https://img.shields.io/badge/langchain-latest-green)
![OpenAI](https://img.shields.io/badge/openai-gpt--4-orange)
![License](https://img.shields.io/badge/license-MIT-blue)

## Overview

This project demonstrates a hands-on approach to building a fully functional AI agent from scratch using Python. The agent processes information autonomously, performs intelligent decision-making, and explores core AI concepts through practical implementation of autonomous workflows.

The AI Research Agent combines multiple tools and services to conduct comprehensive research on any given topic, providing structured outputs with source attribution and methodology transparency.

## Features

### 🤖 **Autonomous Decision Making**
- Intelligent tool selection based on query context
- Dynamic workflow adaptation for different research needs
- Self-directed information gathering and synthesis

### 🔍 **Multi-Source Research Capabilities**
- **Web Search**: Real-time information retrieval using DuckDuckGo
- **Wikipedia Integration**: Structured knowledge base access
- **Content Persistence**: Automatic saving of research outputs

### 📊 **Structured Output Processing**
- Pydantic-based response validation and parsing
- Consistent data formatting across all research sessions
- Source attribution and methodology tracking

### 🛠️ **Extensible Tool Architecture**
- Modular tool design for easy expansion
- Custom tool creation support
- Seamless integration with LangChain ecosystem

### 💾 **Research Persistence**
- Automatic timestamped research output saving
- Structured text file generation
- Research session history tracking

## Technical Architecture

### Core Components

- **LangChain Framework**: Orchestrates agent behavior and tool interactions
- **OpenAI GPT-5**: Primary language model for reasoning and synthesis
- **Pydantic**: Data validation and structured output parsing
- **Custom Tools**: Specialized research and persistence tools

### Agent Workflow

1. **Query Processing**: User input analysis and intent recognition
2. **Tool Selection**: Intelligent selection of appropriate research tools
3. **Information Gathering**: Multi-source data collection and processing
4. **Synthesis**: Intelligent combination and analysis of gathered information
5. **Output Generation**: Structured response formatting with source attribution
6. **Persistence**: Automatic saving of research results

## Installation & Setup

### Prerequisites

- **Python**: Version 3.8 or higher
- **OpenAI API Key**: Valid API key for GPT-4 access
- **Internet Connection**: Required for web search and Wikipedia access

### Quick Start

1. **Clone the Repository**
   ```bash
   git clone <https://github.com/JirkaEifler/ai-agent>
   cd AI Agent
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the Agent**
   ```bash
   python main.py
   ```

## Usage

### Basic Research Query

When you run the application, you'll be prompted to enter a research topic:

```
What can I help you research? 
```

**Example queries:**
- "Artificial intelligence trends in 2025"
- "Climate change impact on agriculture"
- "History and evolution of blockchain technology"

### Output Structure

The agent provides structured responses in the following format:

```python
{
    "topic": "Your research topic",
    "summary": "Comprehensive summary of findings",
    "source": ["list", "of", "sources", "used"],
    "tools_used": ["search", "wiki_tool", "save_tool"]
}
```

### Research Persistence

All research outputs are automatically saved to `research_output.txt` with:
- Timestamp of research session
- Complete structured findings
- Source attribution
- Tools utilized

## Project Structure

```
ai-research-agent/
├── main.py                 # Main application entry point
├── tools.py               # Custom tool implementations
├── requirements.txt       # Python dependencies
├── .env                   # Environment configuration
├── .env.example          # Environment template
├── research_output.txt   # Generated research outputs
└── README.md             # This file
```

## Core Components

### `main.py` - Agent Orchestration
- **ResearchResponse Model**: Pydantic model for structured output validation
- **LLM Configuration**: OpenAI GPT-5 integration setup
- **Prompt Engineering**: System prompt for research assistant behavior
- **Agent Executor**: LangChain agent with tool-calling capabilities

### `tools.py` - Tool Implementations
- **Search Tool**: DuckDuckGo web search integration
- **Wikipedia Tool**: Wikipedia API wrapper for knowledge base access
- **Save Tool**: File persistence with timestamp and formatting

### Key Features of Implementation

#### Structured Output Parsing
```python
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    source: list[str]
    tools_used: list[str]
```

#### Intelligent Tool Selection
The agent automatically selects appropriate tools based on the research context, combining web search and Wikipedia for comprehensive information gathering.

#### Error Handling
Robust error handling ensures graceful degradation when parsing fails, providing both structured and raw outputs for debugging.

## Advanced Configuration

### Model Selection
The default configuration uses GPT-4, but you can modify the model in `main.py`:
```python
llm = ChatOpenAI(model="gpt-5")  # or gpt-3.5-turbo for cost optimization
```

### Tool Customization
Add custom tools by extending the tools list in `main.py`:
```python
tools = [search_tool, wiki_tool, save_tool, your_custom_tool]
```

### Output Customization
Modify the `ResearchResponse` model to include additional fields or change the output structure according to your needs.

## Dependencies

### Core Libraries
- **langchain**: Framework for building LLM applications
- **langchain-openai**: OpenAI integration for LangChain
- **langchain-community**: Community tools and utilities
- **pydantic**: Data validation and parsing
- **python-dotenv**: Environment variable management

### Tool-Specific Dependencies
- **wikipedia**: Wikipedia API access
- **duckduckgo-search**: Web search functionality
- **ddgs**: DuckDuckGo search utilities

## Performance Considerations

### API Usage Optimization
- The agent uses GPT-4 which has associated costs per token
- Consider using GPT-3.5-turbo for development to reduce costs
- Monitor API usage through OpenAI dashboard

### Response Time
- Web searches may introduce latency depending on network conditions
- Wikipedia queries are generally fast due to structured API
- Total research time varies with query complexity (typically 10-30 seconds)

### Resource Management
- Research outputs accumulate in the text file over time
- Consider implementing log rotation for long-term usage
- Monitor disk space usage for extensive research sessions

## Troubleshooting

### Common Issues

**API Key Error**
```bash
Error: OpenAI API key not found
```
- Ensure `.env` file exists with valid `OPENAI_API_KEY`
- Verify API key has sufficient credits and permissions

**Parsing Errors**
```bash
Error parsing response
```
- The agent includes fallback to display raw response
- Check OpenAI API status if errors persist
- Verify model availability (GPT-4 access required)

**Tool Execution Failures**
```bash
Tool execution failed
```
- Check internet connectivity for search tools
- Verify Wikipedia API accessibility
- Review verbose output for specific tool errors

## Contributing

This project serves as an educational foundation for understanding AI agent architecture. Areas for contribution include:

- **Additional Tools**: Implement new research tools (academic papers, news APIs, etc.)
- **Enhanced Parsing**: Improve output structure and validation
- **UI Development**: Create web interface for better user experience
- **Performance Optimization**: Implement caching and request optimization

## Future Enhancements

### Planned Features
- **Multi-format Output**: Support for PDF, HTML, and Markdown outputs
- **Advanced Analytics**: Research quality scoring and source reliability assessment
- **Conversation Memory**: Multi-turn research sessions with context retention
- **Custom Workflows**: User-defined research methodologies and templates

### Integration Opportunities
- **Database Integration**: Persistent storage of research sessions
- **Web Interface**: Browser-based research platform
- **API Wrapper**: REST API for integration with other applications
- **Mobile Support**: Cross-platform research assistant

## License

This project is available for everyone under the MIT License. 

## Acknowledgments

- **LangChain Community**: For providing excellent framework and tools
- **OpenAI**: For GPT-5 language model capabilities
- **Python Community**: For robust ecosystem of research and AI libraries
