# Discord Server Message Saver Bot

This simple Discord bot is designed to send a direct message to the user when he/she reacts to that message with a green tick emoji (✅) for any message the user wants to save on the server.

## Features

- Listens for reactions with the green checkmark emoji (✅) on any message.
- It sends that message directly to the user who wants to record a message.
## Getting Started

### Prerequisites

- [Python](https://www.python.org/) installed
- [discord.py](https://discordpy.readthedocs.io/) library installed (`pip install discord.py`)

### Installation

1. Clone the repository:

 ```bash
   git clone https://github.com/Oguzhanyldrmm/Messender-Bot.git
 ```
2.Install dependencies:
 ```bash
   pip install -r requirements.txt

```

### USAGE
- Invite the bot to your server using the OAuth2 URL generated from the Discord Developer Portal.
- Ensure the bot has the necessary permissions to read messages and send direct messages.
- Users can react to any message with the green checkmark emoji (✅).
- The bot will automatically send a direct message to the user who reacted.
- In the code section, enter your discord token.

### Add Messender Bot Your Server!
```bash
https://discord.com/api/oauth2/authorize?client_id=1209469930857177168&permissions=330752&response_type=code&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Foauth2%2Fauthorize%3F%26client_id%3D1209469930857177168%26scope%3Dbot&scope=messages.read+bot


