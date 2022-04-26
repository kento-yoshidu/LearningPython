import socket
import threading

IP = "0.0.0.0"
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    # 最大接続数
    server.listen(5)
    print(f'[*] Listening in {IP}:{PORT}')

    while True:
        # クライアント情報の受け取り
        client, address = server.accept()
        print(f'[*] Accepted Connection from {address[0]}:{address[1]}')
        # スレッドオブジェクトの作成
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Recieved: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()