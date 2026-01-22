from PIL import Image
import io
import base64

class Base64:
    def __init__(self,audio,image):
        self.audio = audio
        self.image = image

    def audio_base64(self):
        with open(self.audio, 'rb') as binary_file:
            binary_file_data = binary_file.read()
            base64_encoded_data = base64.b64encode(binary_file_data)
            base64_audio = base64_encoded_data.decode('utf-8')
            return base64_audio

    def image_base64(self):
        try:
            with Image.open(self.image) as img:
                byte_arr = io.BytesIO()
                img.save(byte_arr, format='webp')
                byte_arr = byte_arr.getvalue()
                base64_str = base64.b64encode(byte_arr).decode('utf-8')
                return base64_str
        except IOError:
            print(f"Error: Unable to open or convert the image {self.image}")
            return None