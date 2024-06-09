import pyshark
from Crypto.Cipher import AES
import base64

# Constants
ENCRYPTION_KEY = "fr33___p4l3571n3"

def decrypt_aes_ecb(encrypted_data, key):
    # Create AES cipher in ECB mode
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    # Decrypt data
    decrypted_data = cipher.decrypt(encrypted_data)
    # Remove padding
    padding_len = decrypted_data[-1]
    return decrypted_data[:-padding_len]

def read_pcap(file_path):
    # Open the pcap file
    cap = pyshark.FileCapture(file_path)

    packet_number = 0
    for packet in cap:
        packet_number += 1
        print(f'Checking packet number: {packet_number}')
        try:
            # Check if the packet has a TCP layer
            if 'TCP' in packet:
                tcp_layer = packet['TCP']
                
                # Check if source or destination port is 1337
                if tcp_layer.srcport == '1337' or tcp_layer.dstport == '1337':
                    # Extract payload
                    encrypted_payload = bytes.fromhex(tcp_layer.payload.replace(':', ''))
                    # Decrypt the payload
                    decrypted_payload = decrypt_aes_ecb(encrypted_payload, ENCRYPTION_KEY)
                    # Decode to string assuming UTF-8 encoding
                    decrypted_message = decrypted_payload.decode('utf-8', errors='ignore')

                    print(f'Timestamp: {packet.sniff_time}')
                    print(f'Source IP: {packet.ip.src}')
                    print(f'Destination IP: {packet.ip.dst}')
                    print(f'Source Port: {tcp_layer.srcport}')
                    print(f'Destination Port: {tcp_layer.dstport}')
                    print(f'Decrypted Message: {decrypted_message}')
                    print('-' * 50)
        except AttributeError:
            # In case a packet does not have the necessary attributes, we skip it
            continue
        except Exception as e:
            # Handle other exceptions, such as decryption errors
            print(f"Error processing packet: {e}")
            continue

    cap.close()

# Example usage
file_path = 'new.pcapng'  # Replace with your actual file path
read_pcap(file_path)
