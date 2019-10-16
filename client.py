import socket


HOST = socket.gethostbyname("192.168.0.104")
PORT = 7525
s = socket.socket()

s.connect((HOST, PORT))
s.send(b"Hello server!")

with open('received_file', 'wb') as f:
    print("dosya açıldı")
    while True:
        print('data iletiliyor...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        f.write(data)

f.close()
print('Dosya basariyla alindi')
s.close()
print('baglanti kapatildi')
