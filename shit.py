#imported sockets library
import socket
#asking for host info
host = input("[HOST IP]: ")
start = input("[STARTING PORT]: ")
end = input("[END PORT]: ")
resolve = input("[END ON FAILED RESOLVE(y/n)]: ")
#if we can't connect to the host, exit
e_res = False
if resolve.strip().lower() == "y":
    e_res = True
#we need a port range
if start == end:
    print("Invalid port range! Start and end port musn't match")
#here we'll store all the ports to scan
port_range = []
for port in range(int(start), int(end)+1):
    port_range.append(port)
#creating the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#here we'll store open ports
open_ports = []
#scan function
def scan():
    #global vars, if this wasn't here we'd get an error
    global port_range
    global e_res
    #going through our ports
    for port in port_range:
        #a little complicated for no reason, there was a bug i fixed but
        #i am not going to bother cleaning it
        try:
            try:
                sock.connect((socket.gethostbyname(host), int(port)))
                sock.close()
                print(f"[*] Port {port} is open")
                open_ports.append(port)
            except Exception:
                print(f"[*] Port {port} seems to be closed")
                if e_res:
                    exit(0)
        except ConnectionRefusedError:
            print(f"[*] Port {port} is closed")
    print(f"[**] Scan finished, found {int(len(open_ports))} open ports. \n{open_ports}")
#running this tragedy
scan()
        
    
