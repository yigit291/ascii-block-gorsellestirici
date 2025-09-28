# Basit blok verilerini metin tabanlı (ASCII) bir kutu içinde görselleştirir.

def visualize_block(block_data):
    """
    Blok verisini bir ASCII kutusu içinde yazdırır.
    """
    lines = [
        f"Blok Index: {block_data.get('index', 'N/A')}",
        f"Timestamp : {block_data.get('timestamp', 'N/A')}",
        f"Hash      : {block_data.get('hash', 'N/A')[:24]}...", # Hash'i kısaltalım
        f"Prev. Hash: {block_data.get('previous_hash', 'N/A')[:24]}...",
    ]

    # Kutunun genişliğini en uzun satıra göre ayarla
    width = max(len(line) for line in lines)

    print("+" + "-" * (width + 2) + "+")
    for line in lines:
        print("| " + line.ljust(width) + " |")
    print("+" + "-" * (width + 2) + "+")

if __name__ == "__main__":
    ornek_blok = {
        'index': 101,
        'timestamp': 1678886400,
        'hash': '0000abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234',
        'previous_hash': '00001234567890abcdef1234567890abcdef1234567890abcdef12345678',
    }
    visualize_block(ornek_blok)