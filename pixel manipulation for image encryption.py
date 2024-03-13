from PIL import Image

def encrypt_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()
    
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (g, b, r)  # swapping pixel values
            
    encrypted_image_path = image_path.split('.')[0] + "_encrypted.png"
    img.save(encrypted_image_path)
    print("Image encrypted successfully!")
    return encrypted_image_path

def decrypt_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()
    
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (b, r, g)  # swapping pixel values back
            
*⬤*
