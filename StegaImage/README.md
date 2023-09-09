# StegaImage

A test in storing data inside an image using steganography.

## Description

StegaImage allows you to embed a message in an image using steganography. Compare the 2 PNG's I've included, one has a hidden message. The script also allows you to extract the message after it has been embedded.

## Features

- **Embed & Extract**: Seamlessly embed messages into images and extract them when needed.
- **Unnoticeable Alterations**: The integrity of the image remains uncompromised, making the concealed message indistinguishable.
- **User-friendly Interface**: The command-line interface is intuitive and straightforward, ensuring that users can easily navigate through the embedding and extraction processes.

## Setup

1. Install the required libraries:
   
   ```
   pip install pillow
   ```

## Usage

After setting up, navigate to the directory containing the script. The tool can be used in the following ways:

- **Embedding a Message**:

  ```
  py main.py
  ```

  Follow the on-screen prompts to select (e)mbedding. Provide the source image path, the message you wish to hide, and specify the path for the steganographic image.

- **Extracting the Message**:

  ```
  py main.py
  ```

  Follow the on-screen prompts to select e(x)traction. Provide the path to the steganographic image to reveal the hidden message.
