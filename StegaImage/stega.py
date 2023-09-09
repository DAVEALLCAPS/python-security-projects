from PIL import Image

def message_to_bin(message):
    return ''.join(format(ord(i), '08b') for i in message)

def bin_to_message(binary_message):
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))
    return message

def embed_message(image_path, message, output_path):
    image = Image.open(image_path)
    binary_message = message_to_bin(message) + '1111111111111110'  # 16-bit delimiter
    pixels = image.load()
    bin_index = 0

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = list(pixels[i, j])
            for n in range(3):  # Iterate over RGB
                if bin_index < len(binary_message):
                    pixel[n] = int(format(pixel[n], '08b')[:-1] + binary_message[bin_index], 2)
                    bin_index += 1
            pixels[i, j] = tuple(pixel)

    image.save(output_path)

def extract_message(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    binary_message = ""

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            for n in range(3):  # Iterate over RGB
                binary_message += format(pixels[i, j][n], '08b')[-1]

    # Splitting binary_message using the delimiter and then decoding the message
    binary_message = binary_message.split('1111111111111110')[0]
    return bin_to_message(binary_message)
