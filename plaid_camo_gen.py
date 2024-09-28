import matplotlib.pyplot as plt
import numpy as np
import random
import argparse

# Default settings
DEFAULT_SEED = 42
DEFAULT_NUM_COLORS = 5
DEFAULT_RECURSION_DEPTH = 4
DEFAULT_LINE_THICKNESS = 2
DEFAULT_SCALE_FACTOR = 0.5  # Smaller scale factor for more levels

# Urban-inspired color palette
URBAN_COLOR_PALETTE = ['#708090', '#2f4f4f', '#d3d3d3', '#4682b4', '#778899', '#a9a9a9', '#696969', '#bdb76b', '#8b4513', '#556b2f']

# Neon-inspired color palette
NEON_COLOR_PALETTE = ['#ff00ff', '#00ffff', '#ff4500', '#32cd32', '#ff1493', '#00ff00', '#ff6347', '#8a2be2', '#ffb6c1', '#00fa9a']

PALETTES = {
    "urban": URBAN_COLOR_PALETTE,
    "neon": NEON_COLOR_PALETTE
}

def generate_random_color_palette(num_colors, palette):
    """Generate a random color palette with the specified number of colors."""
    return random.sample(palette, num_colors)

def draw_multiscale_plaid(ax, x, y, width, height, depth, colors, line_thickness, scale_factor):
    """Recursive function to draw multi-scale plaid patterns where both squares and lines are colored."""
    if depth == 0:
        return

    num_squares = 10  # Number of rows and columns per grid level

    # Calculate square size
    square_width = width / num_squares
    square_height = height / num_squares

    # Loop through each grid cell and fill it with colors
    for i in range(num_squares):
        for j in range(num_squares):
            # Randomly pick a color for the square background
            square_color = random.choice(colors)
            rect = plt.Rectangle((x + i * square_width, y + j * square_height), square_width, square_height, color=square_color)
            ax.add_patch(rect)

            # Draw vertical and horizontal lines around each square with random colors
            line_color = random.choice(colors)
            ax.plot([x + i * square_width, x + i * square_width], [y, y + height], color=line_color, lw=line_thickness)
            ax.plot([x, x + width], [y + j * square_height, y + j * square_height], color=line_color, lw=line_thickness)

    # Reduce scale and recurse, while filling the entire canvas again
    new_width = width * scale_factor
    new_height = height * scale_factor
    num_repeats_x = int(width // new_width)
    num_repeats_y = int(height // new_height)

    # Repeat the recursive pattern to cover the entire canvas at a smaller scale
    for i in range(num_repeats_x):
        for j in range(num_repeats_y):
            draw_multiscale_plaid(ax, x + i * new_width, y + j * new_height, new_width, new_height, depth - 1, colors, line_thickness, scale_factor)

def create_plaid_pattern(args):
    """Main function to create and save the multi-scale plaid pattern."""
    random.seed(args.seed)
    
    if args.palette not in PALETTES:
        print(f"Palette '{args.palette}' not found. Available palettes: {', '.join(PALETTES.keys())}")
        return
    
    colors = generate_random_color_palette(args.num_colors, PALETTES[args.palette])
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, 400)
    ax.set_ylim(0, 400)
    ax.axis('off')

    draw_multiscale_plaid(ax, 0, 0, 400, 400, args.recursion_depth, colors, args.line_thickness, args.scale_factor)

    # Save the figure to a file if a file path is provided
    if args.output:
        plt.savefig(args.output, bbox_inches='tight', pad_inches=0)
        print(f"Pattern saved as {args.output}")
    else:
        plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a multi-scale plaid pattern for urban camouflage.")

    parser.add_argument("--seed", type=int, default=DEFAULT_SEED, help="Random seed for color generation")
    parser.add_argument("--num_colors", type=int, default=DEFAULT_NUM_COLORS, help="Number of colors to use in the pattern")
    parser.add_argument("--palette", type=str, choices=list(PALETTES.keys()), default="urban", help="Color palette to use (urban or neon)")
    parser.add_argument("--recursion_depth", type=int, default=DEFAULT_RECURSION_DEPTH, help="Depth of recursion for multi-scale patterns")
    parser.add_argument("--line_thickness", type=float, default=DEFAULT_LINE_THICKNESS, help="Thickness of the plaid lines")
    parser.add_argument("--scale_factor", type=float, default=DEFAULT_SCALE_FACTOR, help="Scaling factor for each recursion level")
    parser.add_argument("--output", type=str, help="File path to save the pattern (e.g., 'pattern.png')")

    args = parser.parse_args()
    
    create_plaid_pattern(args)

