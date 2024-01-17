import autogen
from agent_utils import is_termination_message
from flight_adaptor import FlightAdaptor
from importlib import reload

reload(autogen)
def get_flight_engineer(base_llm_config: dict, flight_adaptor: FlightAdaptor):
    # Add the function signature to our llm config
    llm_config = base_llm_config.copy()
    llm_config["functions"] = [
        {
            "name": "get_flight_info",
            "description": "Get the details of a flight based on its flight number",
            "parameters": {
                "type": "object",
                "properties": {
                    "flight_number": {
                        "type": "string",
                        "description": "The flight number for which information is requested",
                    },
                },
                "required": ["flight_number"],
            },
        }
    ]

    # A system message to define the role and job of our agent
    system_message = "A Flight Engineer. You fetch flight details based on the flight number provided."

    # Create and return our assistant agent
    return autogen.AssistantAgent(
        name="Flight_Engineer",
        llm_config=llm_config,
        system_message=system_message,
        function_map={
            "get_flight_info": flight_adaptor.get_flight_info,
        },
        is_termination_msg=is_termination_message,
    )
