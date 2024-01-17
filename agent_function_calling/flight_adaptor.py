import json

class FlightAdaptor:
    def __init__(self) -> None:
        # Load flight data from the JSON file
        with open('flight_data.json', 'r') as file:
            self.flights = json.load(file)

    def get_flight_info(self, flight_number: str) -> str:
        # Find the flight by number and return its details
        for flight in self.flights:
            if flight["flight_number"] == flight_number:
                print("===")
                print("Response from Flight Data:")
                print(json.dumps(flight, indent=4))
                print("===")
                return "Done"
        print("Flight not found")
        return "Done"
