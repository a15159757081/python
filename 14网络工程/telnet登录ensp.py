import telnetlib
import time

host = "192.168.56.100"
password = "123"

tn = telnetlib.Telnet(host)
tn.read_until(b"Password")
tn.write(password.encode('ascii')+b"\n")
tn.write(b"sys\n")
tn.write(b"interface loopback 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
time.sleep(0.5)
print(tn.read_very_eager().decode("ascii"))
tn.close()