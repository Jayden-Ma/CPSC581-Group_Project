import socket

PI_IP = "10.0.0.27"   # <-- change to your Pi's IP
PORT = 5000

print(f"Connecting to {PI_IP}:{PORT}...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((PI_IP, PORT))
    print("Connected! Type commands (forward, backward, left, right).")
    print("Press Ctrl+C to quit.\n")

    try:
        while True:
            cmd = input("> ").strip()
            if cmd == "":
                continue

            s.sendall(cmd.encode())

    except KeyboardInterrupt:
        print("\nDisconnected.")