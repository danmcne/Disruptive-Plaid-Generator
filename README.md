# Disruptive Plaid Pattern Generator

This is a Python program that generates a **multi-scale plaid pattern** designed for "urban camouflage." The pattern consists of recursive plaid grids, with user-controllable colors, recursion depth, and other parameters. The output can be displayed or saved as an image file.

## Features

- Generate plaid camouflage patterns with **multi-scale recursion**.
- Use either **urban-inspired** or **neon-inspired** color palettes.
- Customize pattern parameters such as the number of colors, recursion depth, line thickness, and scaling factor.
- Save the generated pattern as a PNG image.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/danmcne/disruptive-plaid-generator.git
   cd disruptive-plaid-generator
   ```

2. Install the required Python packages:
   ```bash
   pip install matplotlib numpy
   ```

## Usage

You can run the program directly from the command line. Below are the command-line arguments that can be used to customize the generated pattern:

### Command-Line Arguments

| Argument           | Type    | Default            | Description                                                                 |
|--------------------|---------|--------------------|-----------------------------------------------------------------------------|
| `--seed`           | `int`   | `42`               | Random seed for reproducibility.                                            |
| `--num_colors`     | `int`   | `5`                | Number of colors to use from the palette.                                   |
| `--palette`        | `str`   | `"urban"`          | Color palette to use (`urban` or `neon`).                                   |
| `--recursion_depth`| `int`   | `4`                | How deep the recursive pattern goes. Higher depth increases complexity.     |
| `--line_thickness` | `float` | `2`                | Thickness of the lines in the plaid pattern.                                |
| `--scale_factor`   | `float` | `0.5`              | Scaling factor for recursion. Smaller values result in finer patterns.      |
| `--output`         | `str`   |                    | File path to save the generated pattern as an image. If not provided, the pattern will be displayed. |

### Examples

#### Example 1: Display a pattern with default settings
```bash
python plaid_camo_gen.py
```

#### Example 2: Generate an urban pattern and save it to a file
```bash
python plaid_camo_gen.py --seed 42 --num_colors 6 --palette urban --recursion_depth 5 --line_thickness 3 --scale_factor 0.6 --output pattern.png
```

#### Example 3: Create a neon pattern with different parameters
```bash
python plaid_camo_gen.py --seed 56 --num_colors 7 --palette neon --recursion_depth 4 --line_thickness 1.5 --scale_factor 0.7
```

## Available Palettes

- **Urban**: Inspired by urban environments with a mix of greys, blues, greens, and earthy tones.
- **Neon**: Bright, eye-catching colors inspired by neon lights.

## How It Works

The program recursively generates a plaid pattern by subdividing the canvas into grids and assigning colors to both squares and the lines separating them. With each recursion level, the grid becomes finer, creating a **multi-scale pattern**. This can be used to simulate camouflage in urban settings or just to generate cool abstract patterns.

## Requirements

- **Python 3.x**
- **Matplotlib**: Used for drawing the patterns.
- **NumPy**: For array handling and calculations.

Install dependencies using:

```bash
pip install matplotlib numpy
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## Contact

For any questions or feedback, feel free to reach out via GitHub or create an issue in the repository.
