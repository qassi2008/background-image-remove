from rembg import remove
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt


def remove_background(input_path, output_path):
    try:
        with open(input_path, "rb") as image_file:
            input_image = image_file.read()
    except FileNotFoundError:
        print(f"File {input_path} not found.")
        return

    try:
        output_image = remove(input_image)
    except Exception as e:
        print(f"Error during background removal: {e}")
        return

    try:
        output_image = Image.open(BytesIO(output_image))
        output_image.save(output_path)
    except Exception as e:
        print(f"Error during image saving: {e}")

    # Using matplotlib to show the image
    plt.imshow(output_image)
    plt.axis('off')
    plt.show()


remove_background('img.jpeg', 'result.png')
