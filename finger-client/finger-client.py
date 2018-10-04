import sys
import socket 
 
FINGER_PROTOCOL_PORT= 79


def finger(ip_address, args=""):
    '''
    Send finger request to an ip address.

    Args:
        ip_address (string): IP Address
        args (string): Finger args
    
    Returns:
        bool: True for node details, False otherwise.
    '''

    BUFFER_SIZE = 1024
     
    try:
        # Create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        
        # Connect to the IP address and port
        sock.connect((ip_address, FINGER_PROTOCOL_PORT))

        # Send finger arguments
        sock.send(args + "\n")

        while 1:
            buffer = sock.recv(1024)

            if not buffer:
                break

            sys.stdout.write(buffer)

        sys.stdout.flush()
            
        return True
    except:
        return False
    finally:
        sock.close()

def get_ip_address(host):
    '''
    Resolve IP address of a host 

    Args:
        host (string): Host name
    Returns
        string bool: IP address on success, False otherwise.
    '''

    try:
        addr_info = socket.getaddrinfo(host, FINGER_PROTOCOL_PORT)

        if len(addr_info) == 0:
            return False
        
        return addr_info[0][4][0]
    except:
        return False

if __name__ == "__main__":
    if len(sys.argv) not in [1, 2]:
        print "Usage: finger-client [user][user@host]"
        sys.exit()

    if len(sys.argv) == 1:
        host = "127.0.0.1"
        args = ""
    elif len(sys.argv) == 2:
        connection = sys.argv[1].split('@')
        
        if len(connection) == 1:
            host = "127.0.0.1"
            args = sys.argv[1]
        elif len(connection) == 2:
            host = connection[1]
            args = connection[0]
        else:
            print "Error: invalid parameter" 
            sys.exit()
    
    ip_address = get_ip_address(host)

    response = finger(ip_address, args)

    if (response == False):
        print "Error! could not fetch details"
    else:
        print response



