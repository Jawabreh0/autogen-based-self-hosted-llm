import autogen
import argparse

from agent_engineer import get_flight_engineer
from agent_expert import get_flight_expert
from agent_user import get_user
from flight_adaptor import FlightAdaptor

def main(prompt: str):
    # Get the external system adaptor for flights
    flight_adaptor = FlightAdaptor()

    # Build the gpt_configuration object
 # build the gpt_configuration object
    base_llm_config = {
        "config_list": [
            {
                "model": "/home/jawabreh/Desktop/CyprusCodes/CyprusCodes_LLM/mistral-7b-openorca.Q5_K_M.gguf",
                "api_key": "dont-copy-this",
                "api_base": "http://localhost:8000/api/v1/chat/completions",
                "api_type": "open_ai",
            }
        ],
        "use_cache": False,
        "request_timeout": 120,
        "temperature": 0,
    }

    # Create the flight engineer
    engineer = get_flight_engineer(base_llm_config, flight_adaptor)

    # Create the flight expert
    expert = get_flight_expert(base_llm_config)

    # Create the user proxy agent
    user = get_user()

    # Create a group chat and initiate the chat
    groupchat = autogen.GroupChat(
        agents=[user, expert, engineer],
        messages=[],
        max_round=10,
    )
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=base_llm_config)

    final_prompt = f"""Provide the user with the details from their flight data that they want in provided PROMPT.
Figure out the specific flight details the user wants if needed.

PROMPT:
{prompt}"""
    user.initiate_chat(
        manager,
        clear_history=True,
        message=final_prompt,
    )

if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Program to interact with flight data.")

    # Add all server arguments
    parser.add_argument("-p", "--prompt", type=str, help="Action you want to perform.")

    # Parse the arguments
    args = parser.parse_args()
    main(args.prompt)
