import os
import sys
from PIL import Image


def remove_metadata(input_file):
    """Remove metadata from a JPEG file and save the image."""

    # Ensure the input file exists
    if not os.path.exists(input_file):
        print(f"File '{input_file}' not found.")
        return

    # Check if the file is a JPEG (supports both .jpg and .jpeg)
    if not input_file.lower().endswith((".jpg", ".jpeg")):
        print(f"File '{input_file}' is not a JPEG file. Only .jpg or .jpeg files are supported.")
        return

    # Open the image
    try:
        image = Image.open(input_file)
    except Exception as e:
        print(f"Error opening file '{input_file}': {e}")
        return

    # Remove EXIF metadata if it exists
    try:
        image.info.pop('exif', None)  # Remove EXIF metadata from the image object if it exists
    except Exception as e:
        print(f"Error removing EXIF data: {e}")

    # Get the filename and extension
    filename, ext = os.path.splitext(input_file)
    output_file = f"{filename}-nometadata{ext}"

    # Save the image without metadata
    try:
        image.save(output_file, "JPEG", quality=97)  # roughly same quality, default subsampling
        print(f"Metadata removed and image saved as '{output_file}'")
    except Exception as e:
        print(f"Error saving file '{output_file}': {e}")


def print_help():
    """Print usage help for the script."""
    help_text = """
    Usage: python metadata_stripper.py <filename.jpg>

    This script removes metadata from JPEG files (.jpg or .jpeg) and saves a new image without metadata.
    The original quality of the image is preserved.

    Options:
    -h, --help      Show this help message and exit.

    Example:
    python metadata_stripper.py myimage.jpg
    """
    print(help_text)


if __name__ == "__main__":
    # Check for help option
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        print_help()
    else:
        input_file = sys.argv[1]
        remove_metadata(input_file)
