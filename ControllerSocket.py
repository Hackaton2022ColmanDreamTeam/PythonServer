import socket

HOST = "localhost"
PORT = 65432

# basic function calls the model
def CPUUtil():
    number = 28
    return "your utilization is " + str(number) +" percent" 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024) # recive the String from the Client
            if not data:
                break
            Result = CPUUtil()
            conn.sendall(str.encode(Result)) # the result from the model
