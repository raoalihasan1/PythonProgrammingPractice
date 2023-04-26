class Socket():

    """

    Mutable wrapper class for sockets.

    """

    def __init__(self, socket):
        self._socket = socket

    def send(self, message):
        """

        Processes and sends the message to a socket.

        :param message: The message being sent to the socket.
        :type message: string

        """
        self._socket.send(message.strip()+b"\n")

    def close(self):
        """

        Closes the socket.

        """
        self._socket.close()
