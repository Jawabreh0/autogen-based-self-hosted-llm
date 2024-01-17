import autogen
from agent_utils import is_termination_message
from importlib import reload

reload(autogen)
def get_flight_expert(base_llm_config: dict):
    # A system message to define the role and job of our agent
    system_message = """A Flight Expert. 
    Identify which flight details the user wants based on the flight number. 
    Provide the requested information or complete flight details in the provided JSON FORMAT.

    FORMAT: 
    {"key": "value"}."""

    # Create and return our assistant agent
    return autogen.AssistantAgent(
        name="Flight_Expert",
        llm_config=base_llm_config,
        system_message=system_message,
        is_termination_msg=is_termination_message,
    )
