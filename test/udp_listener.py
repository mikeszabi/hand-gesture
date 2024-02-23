#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 21:11:30 2024

@author: szabi
"""

import socket

class UDPServer:
    def __init__(self, listen_host, listen_port):
        """
        Initializes the UDPServer object with the host and port on which to listen.

        :param listen_host: The IP address of the interface to listen on as a string.
        :param listen_port: The port number to listen on as an integer.
        """
        self.listen_host = listen_host
        self.listen_port = listen_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket
        self.socket.bind((self.listen_host, self.listen_port))
        print(f"Listening on {self.listen_host}:{self.listen_port}")

    def listen(self):
        """
        Listens for messages and prints them to the console.
        """
        print("Server is listening for messages. Press Ctrl+C to stop.")
        try:
            while True:
                data, addr = self.socket.recvfrom(1024)  # buffer size is 1024 bytes
                print(f"Received message: {data.decode('utf-8')} from {addr}")
        except KeyboardInterrupt:
            print("\nServer is stopping.")

    def close(self):
        """
        Closes the socket.
        """
        self.socket.close()
        print("Socket closed.")

# Usage
if __name__ == "__main__":
    udp_server = UDPServer("127.0.0.1", 9999)
    try:
        udp_server.listen()
    finally:
        udp_server.close()