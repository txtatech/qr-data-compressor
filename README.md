# qr-data-compressor
A simple encoder/decoder multi-tool for qr code data compression that utilizes gzip, base64 and hex.

# QR Data Compressor

## Description
The `qr-data-compressor.py` is a Python-based GUI application designed to handle QR code generation, compression, decompression, and encoding/decoding tasks. It leverages the `wxPython` library for GUI, `qrcode` for QR code generation, and `gzip` and `base64` for compression and encoding tasks, respectively.

The script's GUI offers multiple functionalities organized via buttons, such as:
- Generating a QR code from user input.
- Compressing user input data as Base64 or Hex, and generating QR codes from it.
- Decompressing Base64 or Hex QR code data.
- Converting an image to a Base64 string.
- Converting a Base64 string back to an image.

The application is designed to be intuitive and user-friendly, allowing users to easily handle data compression and QR code generation tasks.

## How to Use

python3 qr-data-compressor.py

1. Run the script using a Python interpreter. The GUI should appear on your screen.
2. Use the text input field to enter the data you want to work with.
3. Select the desired operation by clicking the corresponding button:
   - Generate QR Code: Generates a QR code from the data you input.
   - Compress as Base64 and Generate QR Code: Compresses the data you input as Base64 and generates a QR code from it.
   - Compress as Hex and Generate QR Code: Compresses the data you input as Hex and generates a QR code from it.
   - Decompress QR Code (Base64): Decompresses the Base64 QR code data you input.
   - Decompress QR Code (Hex): Decompresses the Hex QR code data you input.
   - Convert Image to Base64: Converts an image you select to a Base64 string.
   - Convert Base64 to Image: Converts the Base64 string you input back to an image.
4. If the operation involves file selection, a file dialog will appear for you to choose the necessary file.
5. The output of the operation will be displayed in the output text box.

Visit the GitHub page for the script at https://github.com/txtatech/qr-data-compressor for more information.

## Dependencies
- Python 3.7 or later.
- wxPython
- qrcode
- gzip, base64, and binascii from Python's standard library.
- pyzbar and PIL for handling QR code and image operations.

![Example Image](https://github.com/txtatech/qr-data-compressor/qr-data-compressor-example-1.png)

# MIT License

Copyright (c) 2023

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
