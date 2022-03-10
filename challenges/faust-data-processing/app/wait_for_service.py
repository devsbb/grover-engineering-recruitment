import socket
import sys
import time

attempts = 20
timeout = 5


def check_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex((host, port))
        alive = result == 0

    return alive


def wait_for_service(host, port):
    for _ in range(1, attempts + 1):
        print("*" * 10)
        print(f"Waiting for {host}:{port}")
        print("*" * 10)

        if check_port(host, port):
            return True

        time.sleep(timeout)


if __name__ == "__main__":
    host, port = sys.argv[1:]
    wait_for_service(host, int(port))
