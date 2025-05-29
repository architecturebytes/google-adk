from google.adk.agents import Agent 
from agents.tools.hotelbooking_tool import book_hotel_tool

book_hotel_agent = Agent(
    name="HotelBookingAgent",
    model="gemini-2.0-flash",
    #model="gemini-2.0-flash-live-001",
    description=(
        "Agent to book hotel for Travel"
    ),
    instruction=(
        "You are a helpful agent that can book hotel for Travel using 'book_hotel_tool'. Ask for additional information if required."
    ),
    tools=[book_hotel_tool]
)
