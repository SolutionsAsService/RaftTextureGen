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

def draw_lashing(draw, x, y, length, horizontal=True):
    # Draw lashing with some texture
    if horizontal:
        draw.rectangle([x, y, x + length, y + 6], fill=lash_color, outline="black")
        for i in range(2):
            line_y = random.randint(y, y + 6)
            draw.line([x, line_y, x + length, line_y], fill=lash_shadow_color, width=1)
    else:
        draw.rectangle([x, y, x + 6, y + length], fill=lash_color, outline="black")
        for i in range(2):
            line_x = random.randint(x, x + 6)
            draw.line([line_x, y, line_x, y + length], fill=lash_shadow_color, width=1)

def generate_raft_image():
    # Create an image with a white background
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Define plank and lashing sizes
    plank_width = (width - 20) // 5
    plank_height = height - 40

    # Draw bamboo planks
    for i in range(5):
        x = i * plank_width + 10
        y = 20
        draw_bamboo_plank(draw, x, y, plank_width, plank_height)

    # Draw horizontal lashings across the planks
    for i in range(6):
        x = 10
        y = i * (plank_height // 5) + 20
        draw_lashing(draw, x, y, width - 20, horizontal=True)

    # Draw vertical lashings at the ends
    draw_lashing(draw, 10 - 6, 20, plank_height, horizontal=False)
    draw_lashing(draw, width - 10, 20, plank_height, horizontal=False)

    return image

# Generate and save the image for testing
if __name__ == '__main__':
    raft_image = generate_raft_image()
    raft_image.show()  # Opens the generated image in the default image viewer
    raft_image.save("raft.png")  # Saves the generated image to a file
