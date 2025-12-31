from PIL import Image
import os

# Path to the source image
source_image = r"static\Images\raj_image.png"
output_ico = r"static\favicon.ico"
output_png = r"static\favicon.png"

try:
    # Open the source image
    img = Image.open(source_image)
    
    # Convert to RGB if necessary (for PNG with transparency)
    if img.mode == 'RGBA':
        # Create a white background
        background = Image.new('RGB', img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])  # 3 is the alpha channel
        img = background
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Create a 512x512 version (for PNG favicon)
    img_512 = img.resize((512, 512), Image.Resampling.LANCZOS)
    img_512.save(output_png, 'PNG')
    print(f"Created {output_png}")
    
    # Create ICO file with multiple sizes
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    img.save(output_ico, format='ICO', sizes=sizes)
    print(f"Created {output_ico}")
    
    print("Favicon created successfully!")
    
except Exception as e:
    print(f"Error creating favicon: {e}")
