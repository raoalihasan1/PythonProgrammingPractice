import threading
import time
import socket as socketlib
from Socket import Socket


class Receiver():

    """

    A class for receiving newline delimited text commands on a socket.

    """

    def __init__(self):
        self._lock = threading.RLock()
        self._running = True

    def __call__(self, socket):
        """

        Called for a connection.

        :param socket: The socket of the receiver.
        :type socket: Socket.Socket

        """
        # Set timeout on socket operations
        socket.settimeout(1)
        # Wrap socket for events
        wrappedSocket = Socket(socket)
        # Store the unprocessed data
        stored = ''
        chunk = ''
        self._lock.acquire()
        self.onConnect(wrappedSocket)
        self._lock.release()
        # Loop so long as the receiver is still running
        while self.isRunning():
            # Take everything up to the first newline of the stored data
            (message, sep, rest) = stored.partition('\n')
            # If no newline is found, store more data
            if sep == '':
                while self.isRunning():
                    try:
                        chunk = ''
                        chunk = socket.recv(1024).decode()
                        stored += chunk
                        break
                    except socketlib.timeout:
                        pass
                    except:
                        print('Error: An Exception Occurred')
                # Empty chunk means disconnect
                if chunk == '':
                    break
                continue
            # Otherwise store the rest
            else:
                stored = rest
            # Process the command
            self._lock.acquire()
            success = self.onMessage(wrappedSocket, message)
            self._lock.release()
            if not success:
                break
        self._lock.acquire()
        self.onDisconnect(wrappedSocket)
        self._lock.release()
        socket.close()
        del socket
        self.onJoin()

    def stop(self):
        """

        Stop the receiver.

        """
        self._lock.acquire()
        self._running = False
        self._lock.release()

    def isRunning(self):
        """

        Checks if the receiver is still running

        """
        self._lock.acquire()
        running = self._running
        self._lock.release()
        return running

    def onConnect(self, socket):
        pass

    def onMessage(self, socket, message):
        pass

    def onDisconnect(self, socket):
        pass

    def onJoin(self):
        pass


class Server(Receiver):

    def start(self, ip, port):
        """

        Set up the server socket

        :param ip: The IP address of the server.
        :type ip: string
        :param port: The port number of the server.
        :type port: int

        """
        serversocket = socketlib.socket(
            socketlib.AF_INET, socketlib.SOCK_STREAM)
        serversocket.setsockopt(socketlib.SOL_SOCKET,
                                socketlib.SO_REUSEADDR, 1)
        serversocket.bind((ip, int(port)))
        serversocket.listen(10)
        serversocket.settimeout(1)
        self.onStart()
        # Main connection loop
        threads = []
        while self.isRunning():
            try:
                (socket, address) = serversocket.accept()
                thread = threading.Thread(target=self, args=(socket,))
                threads.append(thread)
                thread.start()
            except socketlib.timeout:
                pass
            except:
                self.stop()
        # Wait for all threads
        while len(threads):
            threads.pop().join()
        self.onStop()

    def onStart(self):
        pass

    def onStop(self):
        pass


class Client(Receiver):

    def start(self, ip, port):
        """

        Set up the client socket

        :param ip: The IP address of the server the client is trying to connect to.
        :type ip: string
        :param port: The port number of the server the client is trying to connect to.
        :type port: int

        """
        self._socket = socketlib.socket(
            socketlib.AF_INET, socketlib.SOCK_STREAM)
        self._socket.settimeout(1)
        self._socket.connect((ip, int(port)))
        self.onStart()
        self._thread = threading.Thread(target=self, args=(self._socket,))
        self._thread.start()

    def send(self, message):
        """

        Send a message to the server

        :param message: The message the client is sending to the server.
        :type message: string

        """
        self._lock.acquire()
        self._socket.send(message.strip()+b'\n')
        self._lock.release()
        time.sleep(0.5)

    def stop(self):
        """

        Stop the client from executing

        """
        Receiver.stop(self)
        # Join thread
        if self._thread != threading.currentThread():
            self._thread.join()
        # On stop!
        self.onStop()

    def onStart(self):
        pass

    def onStop(self):
        pass

    def onJoin(self):
        self.stop()
