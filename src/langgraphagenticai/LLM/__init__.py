LANGSMITH_API_KEY="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"
LANGSMITH_PROJECT="Chatbot-agentic-ai-project"

import os
os.environ["LANGSMITH_API_KEY"] = LANGSMITH_API_KEY
os.environ["LANGSMITH_PROJECT"] = LANGSMITH_PROJECT
os.environ['LANGSMITH_TRACING'] = "true"

