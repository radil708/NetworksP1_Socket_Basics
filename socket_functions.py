import socket
import ssl
from txpr_tree import txpr_tree

# Set constants
HOST, PORT, TIMEOUT_VAL_SEC = socket.gethostbyname("project1.5700.network"), 27995, 20
#HOST, PORT = '44.197.61.29', 27995

def create_ssl_socket(host_in : str, port_in : int, timeout_sec : int):
    '''
    Creates a socket and connects to network and port.
    Displays the server and port if successfully connects.
    Will display connection failed if unsuccesfully connects.
    It will create a socket regardless
    :param host_in: server network in the fomrat of xx.xxx.xx.xx etc..
    :param port_in: server port in format of an int
    :param timeout_sec: length in seconds before socket disconnects
        there is no response
    :return: a wrapped socket object
    '''
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.settimeout(timeout_sec)

    wrapped_socket = ssl.wrap_socket(my_socket, ssl_version=ssl.PROTOCOL_TLSv1)
    #TODO comment out all print statements
    #print("SSL socket object succesfully created\n")

    try:
        wrapped_socket.connect((host_in, port_in))
        # TODO comment out all print statements
        print(f"Socket Successfully Connected to:\nHost: {host_in}\nPort: {port_in}")
    except:
        print(f"Socket Failed to connect to Host: {host_in} at Port: {port_in}")

    return wrapped_socket

def send_msg(socket_used, msg_send :str):
    '''
    Sends an ascii encoded message to the server
    :param socket_used: a wrapped socket object
    :param msg_send: a message to be sent as a string
    :return: None
    '''
    send_out_bytes = msg_send.encode("ascii")
    socket_used.send(send_out_bytes)

def receive_msg(socket_used):
    '''
    Receives and decodes the ascii encoded message
        from the server
    :param socket_used: the wrapped sockect object connected
        to the server
    :return: The message decoded into a String
    '''
    full_response = ""
    received = socket_used.recv(1)

    while received != b'\n':
        full_response += received.decode('ascii')
        received = socket_used.recv(1)

    return full_response