from google.adk.agents import Agent 
from agents.tools.flightbooking_tool import book_flight_tool

book_flight_agent = Agent(
    name="FlightBookingAgent",
    model="gemini-2.0-flash",
    #model="gemini-2.0-flash-live-001",
    description=(
        "Agent to book flights"
    ),
    instruction=(
        "You are a helpful agent that can book flights for travel using 'book_flight_tool'. Ask for additional information if required."
    ),
    tools=[book_flight_tool]
)
