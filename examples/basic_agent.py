from trove.agent import TroveAgent
from trove.models import OpenAIModel

# Load AI model
model = OpenAIModel(api_key="your_openai_api_key")

# Create an agent
agent = TroveAgent(name="FinanceBot", system_prompt="Analyze financial situations.", model=model)

# Run a query
response = agent.run("How can I start investing in stocks?")
print("AI Response:", response)
