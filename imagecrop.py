from PIL import Image

# Open the image
image_path = "images/First-Vision.jpeg"  # Update with correct path
img = Image.open(image_path)

# Get the image dimensions
width, height = img.size

# Define the crop box (left, top, right, bottom)
crop_box = (0, int(height * 0.1), width, height)  # Cuts off top 10%

# Crop the image
cropped_img = img.crop(crop_box)

# Save the cropped image
cropped_img.save("images/First-Vision.jpeg")  # Saves as a new file

print("Image cropped successfully!")
