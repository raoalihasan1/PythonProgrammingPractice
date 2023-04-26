from Utilities import Server
from sys import argv
from time import sleep
from enum import Enum


class Commands(Enum):

    """

    Enum class of the possible commands the clients can send in a message to the server to perform

    """

    NEW = "new"     # Create A Unique Username To Join The Chat Room
    ALL = "world"   # Message All The Connected Clients
    LIST = "ls"     # Get A List Of All The Connected Clients
    EXIT = "exit"   # Disconnect From The Chat Room Server


class MyServer(Server):

    """

    Server class processing incoming commands from clients extending another server class 

    """

    def onStart(self):
        """

        Prints a message and initializes a dictionary and the number of connected clients upon starting the server.

        """
        print(f"Server Has Successfully Started...")
        # Dictionary { user_name : socket }
        self.connectedClients = {}
        self.numOfClients = 0

    def onStop(self):
        """

        Prints a message upon stopping the server.

        """
        print(f"\nServer Has Successfully Stopped...")

    def onMessage(self, socket, message):
        """

        Processes messages sent to the server and responds to requests by 
        sending messages back to the sending client or recipient client(s).

        :param socket: The socket of the client who send the message.
        :type socket: Socket.Socket 
        :param message: The message sent to the server.
        :type message: string
        :return: True if connection not to be terminated of the socket else False.
        :rtype: boolean

        """

        # Catch any errors that may occur when trying to split the message
        try:
            # Split the message by whitespace to get the command and the message separately and join the message
            splitMessage = message.strip().split()
            usrMessage = ' '.join(splitMessage[1:])
            command = splitMessage[0]
        except:
            return True

        # Print in the server terminal that the message is received and print the command and the message
        print(f"\nMessage Successfully Received...")
        print(f"Command :: {command}")
        print(f"Parameters :: {usrMessage}")

        # Send an error message to the client if they are trying to perform commands without having registered
        if (command != Commands.NEW.value and socket not in self.swapKeyValDict(self.connectedClients)):
            socket.send(
                b"Error: Please Register A Username To Join The Chat Room Using Command 1")

        # Case where the client is attempting to register if they haven't already done so
        elif (command == Commands.NEW.value and socket not in self.swapKeyValDict(self.connectedClients)):
            # Send an error message to the client if the username contains whitespace
            if (len(splitMessage) > 2):
                socket.send(
                    b"Error: Username Cannot Contain Whitespace. Please Try Again!")
            # Send an error message to the client if the username is one of the reserved commands of the server
            elif (splitMessage[1] in [Command.value for Command in Commands]):
                socket.send(
                    b"Error: This Is A Reserved Command So Cannot Be Used As A Username. Please Try Again!")
            # Send an error message to the client if the username is already taken
            elif (splitMessage[1] in self.connectedClients):
                socket.send(
                    f"Error: The Username {splitMessage[1]} Already Exists. Please Try Again!".encode())
            # Add the clients screen name and their socket to the dictionary and send a welcome message to the client
            else:
                self.connectedClients[splitMessage[1]] = socket
                socket.send(
                    f"Welcome To The Chat Room [{splitMessage[1]}]".encode())
                # Let all other clients know that the new client has joined the chat room
                self.sendToAllOtherClients(
                    socket, f"The Client [{splitMessage[1]}] Has Joined The Chat Room!")

        # Case where the client is attempting to send a message to all the connected clients
        elif (command == Commands.ALL.value):
            # Call the function to send the message to all the clients except the sender
            self.sendToAllOtherClients(
                socket, f"GLOBAL [{self.swapKeyValDict(self.connectedClients)[socket]}]: {usrMessage}")

        # Case where the client is attempting to send a message to a specific client privately
        elif (command in self.connectedClients):
            # Send an error message to the client if they are trying to send a message to themselves
            if self.swapKeyValDict(self.connectedClients)[socket] == command:
                socket.send(
                    "Error: You Cannot Send A Message To Yourself".encode())
            # Send the message to that specific clients' socket using the dictionary to get their socket by their screen name
            else:
                self.connectedClients[command].send(
                    f"PRIVATE [{self.swapKeyValDict(self.connectedClients)[socket]}]: {usrMessage}".encode())

        # Case where the client wants a list of all the connected clients
        elif (command == Commands.LIST.value and len(splitMessage) == 1):
            # Send to the client a list of all the connected clients' screen names by getting the keys of the dictionary
            socket.send(
                f"Connected Clients: {list(self.connectedClients.keys())}".encode())

        # Case where the client wants to terminate their connection from the server
        elif (command == Commands.EXIT.value and len(splitMessage) == 1):
            # Call the disconnect function and exit the function
            self.onDisconnect(socket)
            return False

        # Case where the command in the passed message is an invalid one
        else:
            socket.send(b"Error: Inputted Command/Name Is Invalid!")

        return True

    def onConnect(self, socket):
        """

        Increments the number of connected clients and sends all the possible commands to the clients' socket.

        :param socket: The socket of the client who connected.
        :type socket: Socket.Socket

        """
        # Increment the total number of connected clients
        self.numOfClients += 1
        print(f"\nA Client Has Connected...")
        print(
            f"There Is {self.numOfClients} Client(s) Connected To The Server")
        socket.send(b"")
        socket.send(b"Welcome To The Multi-Client Chat Room...")
        socket.send(b"")
        sleep(0.2)
        socket.send(b"Here Are All The Commands For The Chat Room:")
        sleep(0.2)
        socket.send(
            b"1: new <user_name> - Create A Unique Username To Join The Chat Room")
        sleep(0.2)
        socket.send(b"2: world <message> - Message All The Connected Clients")
        sleep(0.2)
        socket.send(
            b"3: <user_name> <message> - Private Message A Connected Client Specified By Their Username")
        sleep(0.2)
        socket.send(b"4: ls - Get A List Of All The Connected Clients")
        sleep(0.2)
        socket.send(b"5: exit - Disconnect From The Chat Room Server")
        socket.send(b"")
        sleep(0.2)
        socket.send(b"Enter A Unique Username: ")

    def onDisconnect(self, socket):
        """

        Decrements the number of connected clients and deletes the clients' entry in the dictionary.

        :param socket: The socket of the client to disconnect.
        :type socket: Socket.Socket

        """
        try:
            # Get the clients' name who is disconnecting by their socket by swapping the keys and values of the dictionary
            clientName = self.swapKeyValDict(self.connectedClients)[socket]
            # Delete the clients' entry from the dictionary and decrement the number of connected clients
            del self.connectedClients[clientName]
            self.numOfClients -= 1
            socket.send(
                f"Successfully Disconnected [{clientName}] From The Server...".encode())
            print(f'\nA Client Has Disconnected...')
            print(
                f"There Is {self.numOfClients} Client(s) Connected To The Server")
            # Let all other clients know that the client has left the chat room
            self.sendToAllOtherClients(
                socket, f"The Client [{clientName}] Has Left The Chat Room!")
            socket.close()
        except:
            pass

    def swapKeyValDict(self, dict):
        """

        Swap keys and values of a dictionary i.e. keys become the values and values become the keys.

        :param dict: The dictionary who's keys and values need swapping.
        :type dict: dictionary

        """
        return {val: key for key, val in dict.items()}

    def sendToAllOtherClients(self, socket, message):
        """

        Send a message to all the clients except the sending client.

        :param socket: The socket of the client who sent the message.
        :type socket: Socket.Socket
        :param message: The message to send to all the clients.
        :type message: str

        """
        for clientSockets in self.swapKeyValDict(self.connectedClients):
            if socket != clientSockets:
                clientSockets.send(message.encode())


if __name__ == "__main__":

    try:
        ip = argv[1]
        port = int(argv[2])
    except:
        print("Error: Invalid Format! It Should Be In The Following Format:")
        print("python3 Server.py <ip> <port>")
        exit()

    server = MyServer()

    try:
        server.start(ip, port)
    except:
        print("Error: Failed To Start The Server")
        exit()
