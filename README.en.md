[Português](README.md) | [English](README.en.md)

# BTC Mining Hub

BTC Mining Hub is a project that simulates a Bitcoin mining environment, where agents connect to a master server to perform mining transactions. The project includes a Telegram bot to monitor and interact with the server.

## Overview

The project consists of two main components:
- **Agent**: Represents a miner that connects to the master server to perform mining transactions.
- **Master**: The server that manages mining transactions and communicates with the agents.

## Project Structure

- `Agent/main.py`: Main script for the agent that configures the connection to the server and starts mining.
- `Agent/mylib.py`: Library with auxiliary functions for the agent, including the mining logic.
- `Master/main.py`: Main script for the server that configures the connection and manages the agents.
- `Master/mylib.py`: Library with auxiliary functions for the server, including transaction logic and integration with the Telegram bot.

## How to Use

### Server Configuration (Master)

1. Navigate to the `Master` directory.
2. Run the main server script:
    ```sh
    python main.py
    ```
3. The server will be listening on port `31471` and ready to accept agent connections.

### Agent Configuration (Agent)

1. Navigate to the `Agent` directory.
2. Run the main agent script:
    ```sh
    python main.py
    ```
3. Enter a username when prompted.
4. The agent will connect to the server and wait for mining transactions.

### Server Commands

- `/newtrans`: Creates a new mining transaction.
- `/validtrans`: Lists validated transactions.
- `/pendtrans`: Lists pending transactions.
- `/clients`: Lists connected agents.
- `/close`: Closes the server and disconnects all agents.

### Telegram Bot

The server includes a Telegram bot to monitor and interact with the server. The available commands are:
- `/start`: Lists the available commands.
- `/validtrans`: Lists validated transactions.
- `/pendtrans`: Lists pending transactions.
- `/clients`: Lists connected agents.

## Requirements

- Python 3.x
- Libraries: `socket`, `sys`, `threading`, `struct`, `hashlib`, `datetime`, `requests`

## Contribution

Contributions are welcome! Feel free to open issues and pull requests.

## License

This project is licensed under the MIT license. See the [LICENSE](LICENSE) file for more details.
