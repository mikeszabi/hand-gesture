# echo-server.py

import socket

class UDPSender:
    def __init__(self, target_host, target_port):
        """
        Initializes the UDPSender object with target host and port.

        :param target_host: The IP address of the target host as a string.
        :param target_port: The target port as an integer.
        """
        self.target_host = target_host
        self.target_port = target_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP socket

    def send_message(self, message):
        """
        Sends a message to the target host and port.

        :param message: The message to be sent as a bytes-like object or string.
                        If it's a string, it will be encoded to bytes using UTF-8.
        """
        if isinstance(message, str):
            message = message.encode('utf-8') # Convert string to bytes
        
        self.socket.sendto(message, (self.target_host, self.target_port))
        print(f"Message sent to {self.target_host}:{self.target_port}")

    def close(self):
        """
        Closes the socket.
        """
        self.socket.close()
        print("Socket closed.")

# Usage
if __name__ == "__main__":
    # Example: Sending a message to localhost on port 9999
    udp_sender = UDPSender("127.0.0.1", 9999)
    udp_sender.send_message("Ciao, UDP!")
    udp_sender.close()