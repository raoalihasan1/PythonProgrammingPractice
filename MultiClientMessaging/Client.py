from Utilities import Client
from sys import argv
from time import sleep
from Server import Commands


"""

    All User Commands:
        new <user_name> : Create A Unique Username To Join The Chat Room
        world <message> : Message All The Connected Clients
        <user_name> <message> : Private Message A Connected Client Specified By Their Username
        ls: Get A List Of All The Connected Clients
        exit: Disconnect From The Chat Room Server
    
    Running my Program:
    
        Running The Server:
            Terminal Command: python3 Server.py <ip> <port>
        
        Running Telnet:
            Terminal Command: telnet <ip> <port>
        
        Running The Client(s):
            Terminal Command: python3 Client.py <ip> <port>
        
        Order of Commands:
            1. Register A Username: new <user_name>
            2. Send A Message:
                2.1. To All Connected Clients: world <message>
                2.2  To A Specific Client: <user_name> <message>
            3. Get A List Of All Connected Clients: ls
            4. Disconnect Client From The Server: exit
            5. Repeat Steps 2-4 As Many Times As You Like With Step 2 and 3 In Any Order 

"""


class MyClient(Client):

    """

    Client class sending requests to the sever class to process and extends another client class 

    """

    def onMessage(self, socket, message):
        """

        Processes incoming messages from other clients.

        :param socket: The socket of the recipient client.
        :type socket: Socket.Socket
        :param message: The message sent to the recipient client.
        :type message: string
        :return: True if connection not to be terminated else False.
        :rtype: boolean

        """
        if (message == ""):
            print()
        elif (message.startswith("Successfully Disconnected")):
            print(f"> {message.strip()}\n")
            return False
        elif (not (message.startswith("GLOBAL") or message.startswith("PRIVATE"))):
            print(f"> {message.strip()}")
        else:
            print(f" {message.strip()}\n> ", end="")
        return True

    def sendMessage(self, message):
        """

        Processes outgoing messages to the server.

        :param message: The message being sent to the server.
        :type message: string

        """
        self.send(message.encode())
        if (message.split()[0] == Commands.EXIT.value and len(message.split()) == 1):
            exit()
        else:
            print(">", end="")


if __name__ == "__main__":

    try:
        ip = argv[1]
        port = int(argv[2])
    except:
        print("Error: Invalid Format! It Should Be In The Following Format:")
        print("python3 Client.py <ip> <port>")
        exit()

    client = MyClient()

    try:
        client.start(ip, port)
    except:
        print("Error: Failed To Connect To The Server")
        exit()

    lineOne = True
    sleep(2.625)
    while True:
        if lineOne:
            usrMessage = input("> ").strip()
            lineOne = False
        else:
            usrMessage = input(" ").strip()
        if (len(usrMessage) == 0):
            print(">", end="")
            continue
        client.sendMessage(usrMessage)
