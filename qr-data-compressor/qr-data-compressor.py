import wx
import qrcode
import gzip
import base64
import os
from PIL import Image
import binascii
from pyzbar.pyzbar import decode

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="QR-DATA-COMPRESSOR", size=(600, 600))
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Buttons
        self.button_select_file = wx.Button(self.panel, label="Select File")
        self.button_select_file.Bind(wx.EVT_BUTTON, self.select_file)

        self.button_generate_qr = wx.Button(self.panel, label="Generate QR Code")
        self.button_generate_qr.Bind(wx.EVT_BUTTON, self.generate_qr)

        self.button_compress_base64 = wx.Button(self.panel, label="Compress as Base64 and Generate QR Code")
        self.button_compress_base64.Bind(wx.EVT_BUTTON, self.compress_and_generate_base64_qr)

        self.button_compress_hex = wx.Button(self.panel, label="Compress as Hex and Generate QR Code")
        self.button_compress_hex.Bind(wx.EVT_BUTTON, self.compress_and_generate_hex_qr)

        self.button_decompress_base64 = wx.Button(self.panel, label="Decompress QR Code (Base64)")
        self.button_decompress_base64.Bind(wx.EVT_BUTTON, self.decompress_base64)

        self.button_decompress_hex = wx.Button(self.panel, label="Decompress QR Code (Hex)")
        self.button_decompress_hex.Bind(wx.EVT_BUTTON, self.decompress_hex)

        self.button_decompress_base64_qr = wx.Button(self.panel, label="Decompress Base64 QR Data")
        self.button_decompress_base64_qr.Bind(wx.EVT_BUTTON, self.decompress_base64_qr)

        self.button_decompress_hex_qr = wx.Button(self.panel, label="Decompress Hex QR Data")
        self.button_decompress_hex_qr.Bind(wx.EVT_BUTTON, self.decompress_hex_qr)

        self.button_image_to_base64 = wx.Button(self.panel, label="Convert Image to Base64")
        self.button_image_to_base64.Bind(wx.EVT_BUTTON, self.convert_image_to_base64)

        # Base64 image button
        self.create_base64_image_button()

        self.text_input = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        self.output_text = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY)

        # Adding buttons to sizer
        self.sizer.Add(self.button_select_file, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.button_generate_qr, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.button_compress_base64, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.button_compress_hex, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.button_decompress_base64, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.button_decompress_hex, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.button_decompress_base64_qr, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.button_decompress_hex_qr, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.button_image_to_base64, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.base64_button, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)  # Add this line

        self.sizer.Add(self.text_input, 1, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.output_text, 1, wx.ALL | wx.EXPAND, 5)

        self.base64_image_bitmap = wx.StaticBitmap(self.panel)
        self.sizer.Add(self.base64_image_bitmap, 0, wx.ALL | wx.EXPAND, 5)

        self.panel.SetSizer(self.sizer)

    def create_base64_image_button(self):
        self.base64_button = wx.Button(self.panel, -1, "Convert base64 to Image", size=(200,50))
        self.base64_button.Bind(wx.EVT_BUTTON, self.on_base64_convert)

    def generate_qr(self, event):
        data = self.text_input.GetValue().strip()
        self.generate_qr_code(data, "qr_code_" + self.get_unique_str() + ".png")

    def generate_qr_code(self, data, file_name):
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_name)

    def compress_data(self, data):
        return gzip.compress(data.encode("utf-8"))

    def decompress_base64_data(self, encoded_data):
        decoded_data = base64.urlsafe_b64decode(encoded_data)
        decompressed_data = gzip.decompress(decoded_data).decode("utf-8")
        return decompressed_data

    def decompress_hex_data(self, hex_data):
        binary_data = bytes.fromhex(hex_data)
        decompressed_data = gzip.decompress(binary_data).decode("utf-8")
        return decompressed_data

    def binary_to_hex(self, data):
        return data.hex()

    def compress_and_generate_base64_qr(self, event):
        data = self.text_input.GetValue().strip()
        compressed_data = self.compress_data(data)
        encoded_data_base64 = base64.urlsafe_b64encode(compressed_data).decode("utf-8")
        self.generate_qr_code(encoded_data_base64, "compressed_qr_code_base64_" + self.get_unique_str() + ".png")

    def compress_and_generate_hex_qr(self, event):
        data = self.text_input.GetValue().strip()
        compressed_data = self.compress_data(data)
        encoded_data_hex = self.binary_to_hex(compressed_data)
        self.generate_qr_code(encoded_data_hex, "compressed_qr_code_hex_" + self.get_unique_str() + ".png")

    def decompress_base64(self, event):
        qr_code_data = self.text_input.GetValue().strip()
        decompressed_data = self.decompress_base64_data(qr_code_data)
        self.output_text.SetValue("Decompressed Data (Base64):\n" + decompressed_data)

    def decompress_hex(self, event):
        qr_code_data = self.text_input.GetValue().strip()
        decompressed_data = self.decompress_hex_data(qr_code_data)
        self.output_text.SetValue("Decompressed Data (Hex):\n" + decompressed_data)

    def decompress_base64_qr(self, event):
        qr_code_data = self.text_input.GetValue().strip()
        decompressed_data = self.decompress_base64_data(qr_code_data)
        self.output_text.SetValue("Decompressed Data (Base64 QR):\n" + decompressed_data)

    def decompress_hex_qr(self, event):
        qr_code_data = self.text_input.GetValue().strip()
        decompressed_data = self.decompress_hex_data(qr_code_data)
        self.output_text.SetValue("Decompressed Data (Hex QR):\n" + decompressed_data)

    def select_file(self, event):
        with wx.FileDialog(self, "Open QR code file", wildcard="PNG files (*.png)|*.png",
                            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = fileDialog.GetPath()
            try:
                self.display_qr_code_contents(pathname)
            except IOError:
                wx.LogError("Cannot open file '%s'." % pathname)

    def display_qr_code_contents(self, file_path):
        decoded_qr_codes = decode(Image.open(file_path))
        if decoded_qr_codes:
            qr_code_data = decoded_qr_codes[0].data.decode("utf-8")
            self.text_input.SetValue(qr_code_data)
        else:
            self.text_input.SetValue("No QR codes found in the image.")

    def convert_image_to_base64(self, event):
        with wx.FileDialog(self, "Open image file", wildcard="Image files (*.png;*.jpg)|*.png;*.jpg",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'rb') as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                    self.text_input.SetValue(encoded_string)
            except IOError:
                wx.LogError("Cannot open file '%s'." % pathname)

    def on_base64_convert(self, event):
        base64_str = self.text_input.GetValue().strip()
        missing_padding = len(base64_str) % 4
        if missing_padding != 0:
            base64_str += '=' * (4 - missing_padding)
        try:
            base64_data = base64.b64decode(base64_str)
        except binascii.Error as e:
            self.output_text.SetValue("Error decoding base64 string:\n" + str(e))
            return
        png_file = os.path.join(os.getcwd(), 'decoded_qr_' + self.get_unique_str() + '.png')
        with open(png_file, 'wb') as f:
            f.write(base64_data)
        image = wx.Image(png_file, wx.BITMAP_TYPE_ANY)
        if not image.IsOk():
            self.output_text.SetValue("Failed to load image.")
            return
        if hasattr(self, "base64_image_bitmap"):
            self.base64_image_bitmap.SetBitmap(wx.Bitmap(image))
        else:
            self.base64_image_bitmap = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image))
            self.sizer.Add(self.base64_image_bitmap, pos=(8,0), span=(1,2), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)
        self.panel.Layout()

    def get_unique_str(self):
        import time
        return str(int(time.time()))

if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
