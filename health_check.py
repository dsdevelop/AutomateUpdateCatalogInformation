#!/usr/bin/env python3
import psutil
import emails


def check_cpu_usage():
    cpu_usage = psutil.cpu_percent()
    if cpu_usage > 80:
        return True
    else:
        return False


def check_disk_space():
    disk_usage = psutil.disk_usage("/")  # Replace "/" with the path to the partition you want to check
    available_space = disk_usage.free / disk_usage.total * 100
    if available_space < 20:
        return True
    else:
        return False


def check_memory():
    mem = psutil.virtual_memory()
    available_memory = mem.available / 1024 ** 2  # Convert bytes to megabytes
    if available_memory < 500:
        print("Error - Available memory is less than 500MB")
    else:
        print(f"Current available memory: {available_memory:.2f}MB")


def check_connection():
    hostname = "localhost"
    ip_address = "127.0.0.1"

    for conn in psutil.net_connections():
        if conn.laddr[0] == hostname and conn.raddr[0] == ip_address:
            return True
    else:
        return False


if __name__ == "__main__":
    # send settings
    sender = "automation@example.com"
    recipient = "username@example.com"
    body = "Please check your system and resolve the issue as soon as possible."

    # Check CPU usage
    if check_cpu_usage():
        subject = "Error - CPU usage is over 80%"
        message = emails.generate_error_report(sender, recipient, subject, body)
        emails.send_email(message)

    if check_disk_space():
        subject = "Error - Available disk space is less than 20%"
        message = emails.generate_error_report(sender, recipient, subject, body)
        emails.send_email(message)

    if check_memory():
        subject = "Error - Available memory is less than 500MB"
        message = emails.generate_error_report(sender, recipient, subject, body)
        emails.send_email(message)

    if check_connection():
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        message = emails.generate_error_report(sender, recipient, subject, body)
        emails.send_email(message)
