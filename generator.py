from PIL import Image, ImageDraw
import random

# Define image size
width, height = 128, 128  # Larger size for the raft sprite

# Define colors
bamboo_color = (34, 139, 34)  # Green for bamboo
lash_color = (139, 69, 19)    # Brown for lashing
bamboo_shadow_color = (0, 100, 0)  # Darker green for bamboo detail
lash_shadow_color = (101, 51, 0)   # Darker brown for lashing detail

def draw_bamboo_plank(draw, x, y, plank_width, plank_height):
    # Draw a single bamboo plank with some texture
    draw.rectangle([x, y, x + plank_width, y + plank_height], fill=bamboo_color, outline="black")
    # Add texture lines to the bamboo plank
    for i in range(5):
        line_x = random.randint(x, x + plank_width)
        draw.line([line_x, y, line_x, y + plank_height], fill=bamboo_shadow_color, width=1)

def draw_lashing(draw, x, y, lash_width, lash_height):
    # Draw lashing with some texture
    draw.rectangle([x, y, x + lash_width, y + lash_height], fill=lash_color, outline="black")
    # Add texture lines to the lashing
    for i in range(2):
        line_y = random.randint(y, y + lash_height)
        draw.line([x, line_y, x + lash_width, line_y], fill=lash_shadow_color, width=1)

def generate_raft_image():
    # Create an image with a white background
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Define plank and lashing sizes
    plank_width = width // 5
    plank_height = height - 40
    lash_width = 8
    lash_height = 15

    # Draw bamboo planks
    for i in range(5):
        x = i * plank_width + 10
        y = 20
        draw_bamboo_plank(draw, x, y, plank_width - 10, plank_height)

    # Draw lashings around the raft
    for i in range(6):
        # Top lashings
        x = i * plank_width - lash_width // 2 + 10
        y = 10
        draw_lashing(draw, x, y, lash_width, lash_height)

        # Bottom lashings
        x = i * plank_width - lash_width // 2 + 10
        y = height - 25
        draw_lashing(draw, x, y, lash_width, lash_height)

    # Draw vertical lashings (left and right sides)
    for i in range(2):
        x = 5
        y = i * (plank_height // 2) + 20
        draw_lashing(draw, x, y, lash_height, lash_width)

        x = width - 25
        y = i * (plank_height // 2) + 20
        draw_lashing(draw, x, y, lash_height, lash_width)

    return image

# Generate and save the image for testing
if __name__ == '__main__':
    raft_image = generate_raft_image()
    raft_image.show()  # Opens the generated image in the default image viewer
    raft_image.save("raft.png")  # Saves the generated image to a file
