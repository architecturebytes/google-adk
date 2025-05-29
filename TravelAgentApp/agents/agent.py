from google.adk.agents import Agent
from agents.sub_agents.flightbooking_agent import book_flight_agent
from agents.sub_agents.hotelbooking_agent import book_hotel_agent

root_agent = Agent(
    name="TravelAgent",
    model="gemini-2.0-flash",
    #model="gemini-2.0-flash-live-001",
    description=(
        "Agent to help with Travel bookings"
    ),
    instruction=(
        "You are a helpful agent that can answer questions about Travel. Delegate to 'FlightBookingAgent' agent to book flights. Delegate to 'HotelBookingAgent' agent to book hotels."
    ),
    sub_agents=[book_flight_agent, book_hotel_agent]
)
