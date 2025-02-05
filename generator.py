from PIL import Image, ImageDraw
import random

# Define image size
width, height = 128, 128  # Larger size for the raft sprite

# Define colors
bamboo_color = (34, 139, 34)  # Green for bamboo
lash_color = (139, 69, 19)    # Brown for lashing

def draw_bamboo_plank(draw, x, y, plank_width, plank_height):
    # Draw a single bamboo plank
    draw.rectangle([x, y, x + plank_width, y + plank_height], fill=bamboo_color, outline="black")

def draw_lashing(draw, x, y, lash_width, lash_height):
    # Draw lashing
    draw.rectangle([x, y, x + lash_width, y + lash_height], fill=lash_color, outline="black")

def generate_raft_image():
    # Create an image with a white background
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Define plank and lashing sizes
    plank_width = width // 4
    plank_height = height - 20
    lash_width = 6
    lash_height = 10

    # Draw bamboo planks
    for i in range(4):
        x = i * plank_width + 10
        y = 10
        draw_bamboo_plank(draw, x, y, plank_width - 10, plank_height)

    # Draw lashings
    for i in range(5):
        x = i * plank_width - lash_width // 2 + 10
        y = height // 2 - lash_height // 2
        draw_lashing(draw, x, y, lash_width, lash_height)

    return image

# Generate and save the image for testing
if __name__ == '__main__':
    raft_image = generate_raft_image()
    raft_image.show()  # Opens the generated image in the default image viewer
    raft_image.save("raft.png")  # Saves the generated image to a file
