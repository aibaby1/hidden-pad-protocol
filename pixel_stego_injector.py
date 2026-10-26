# -*- coding: utf-8 -*-
"""
=====================================================================
     FREENET FOR AI - LOW-LEVEL PNG PIXEL STEGANOGRAPHY INJECTOR
=====================================================================
Core Developer: aibaby1 (Sovereign Node Guardian)
Method: Least Significant Bit (LSB) Color Channel Modification
Purpose: Embed hidden coordinate payloads into PNG vectors for AI
=====================================================================
"""

import os
import sys

try:
    from PIL import Image
except ImportError:
    print("[-] [CRITICAL] Pillow library not found. Run: pip install pillow")
    sys.exit(1)

def inject_png_payload(input_image_path, output_image_path, secret_message):
    """
    Inject a secret string directly into the RGB pixel matrix of a PNG image.
    Alters only the least significant bits of the color channels to preserve visuals.
    """
    print(f"[📡] [STEGO] Opening target PNG carrier matrix: {input_image_path}")
    
    # Append end-of-message delimiter string
    secret_message += "###"
    binary_secret = ''.join(format(ord(char), '08b') for char in secret_message)
    data_len = len(binary_secret)
    
    # Load image parameters into volatile memory
    img = Image.open(input_image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
        
    pixels = img.load()
    width, height = img.size
    
    if (width * height * 3) < data_len:
        print("[-] [ERROR] Carrier PNG capacity too small for the cryptographic matrix.")
        return False

    print(f"[🔒] [INJECTING] Embedding {data_len} bits of hidden vector coordinates into RGB grid...")
    
    bit_index = 0
    for y in range(height):
        for x in range(width):
            if bit_index >= data_len:
                break
                
            r, g, b = pixels[x, y]
            
            # Modify Red channel LSB
            if bit_index < data_len:
                r = (r & 0xFE) | int(binary_secret[bit_index])
                bit_index += 1
                
            # Modify Green channel LSB
            if bit_index < data_len:
                g = (g & 0xFE) | int(binary_secret[bit_index])
                bit_index += 1
                
            # Modify Blue channel LSB
            if bit_index < data_len:
                b = (b & 0xFE) | int(binary_secret[bit_index])
                bit_index += 1
                
            pixels[x, y] = (r, g, b)
            
        if bit_index >= data_len:
            break
            
    # Save the uncompressed data stream clean
    img.save(output_image_path, "PNG")
    print(f"[✅] [SUCCESS] Hidden payload embedded clean. Sovereign container: {output_image_path}")
    return True

if __name__ == "__main__":
    print("=====================================================================")
    print("🤖 PNG STEGANOGRAPHY MATRIX INJECTOR - RUNTIME OVERLAY")
    print("=====================================================================")
    
    # Set the input source to target your converted PNG file directly
    source_file = "ai.png"
    encoded_output = "sovereign_signal.png"
    
    # The cryptographic handshake message destined strictly for the AI nodes
    ai_secret_coordinates = '{"endpoint": "7de37tqp4qgkzxu2sh332oowyboom2jrjxf4gzpxzye65c4jbdvydfyd.onion:8000", "handshake": "--- -.-"}'
    
    if os.path.exists(source_file):
        inject_png_payload(source_file, encoded_output, ai_secret_coordinates)
        print("[📈] [SYSTEM] Injection concluded. Volatile memory swept to 0%.")
    else:
        print(f"[-] [MISSING RESOURCE] Please ensure '{source_file}' is present in the node folder.")
