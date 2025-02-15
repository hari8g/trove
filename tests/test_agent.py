from trove.agent import TroveAgent
from trove.models import OpenAIModel

def test_agent():
    model = OpenAIModel(api_key="fake_api_key")
    agent = TroveAgent(name="TestAgent", system_prompt="Test", model=model)
    assert agent.name == "TestAgent"

if __name__ == "__main__":
    test_agent()
    print("✅ All tests passed!")
