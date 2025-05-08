import asyncio
import random

# Simulate a server by keeping track of active connections
class Server:
    def __init__(self, name):
        self.name = name
        self.active_connections = 0

    async def handle_request(self):
        self.active_connections += 1
        print(f"{self.name} : {self.active_connections}")
        await asyncio.sleep(random.uniform(5.5, 7.5))  # Simulate work asynchronously
        self.active_connections -= 1
        print(f"Task completed {self.name} : {self.active_connections}")
        

# Function to simulate Round Robin load balancing
def round_robin(servers, index):
    return servers[index % len(servers)]

# Function to simulate Least Connections load balancing
def least_connections(servers):
    return min(servers, key=lambda server: server.active_connections)

# Simulate client requests and distribute them using load balancing
async def simulate_requests(servers, algorithm="round_robin"):
    tasks = []
    load = 10
    for client_id in range(1, load):  # Simulate 5 clients
        if algorithm == "round_robin":
            server = round_robin(servers, client_id - 1)
        elif algorithm == "least_connections":
            server = least_connections(servers)

        print(f"Client {client_id} routed to {server.name}")
        task = asyncio.create_task(server.handle_request())
        tasks.append(task)

    await asyncio.gather(*tasks)

# Main function to simulate the load balancing
async def main():
    servers = [Server(f"Server {i+1}") for i in range(3)]

    print("\n--- Round Robin Load Balancing ---")
    await simulate_requests(servers, "round_robin")

    # print("\n--- Least Connections Load Balancing ---")
    # await simulate_requests(servers, "least_connections")

if __name__ == "__main__":
    asyncio.run(main())
