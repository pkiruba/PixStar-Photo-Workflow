# cleanup_photos.py

import os
import argparse
from PIL import Image
from tqdm import tqdm

# --- Configuration Constants ---
# Recommended JPEG Quality: 90 offers a great balance of visual quality and file size
JPEG_QUALITY = 90

def parse_arguments():
    """
    Handles command-line argument parsing for source and output directories.
    """
    parser = argparse.ArgumentParser(
        description="Clean and optimize JPEG photos for digital picture frames by stripping metadata."
    )
    parser.add_argument(
        '-s', '--source', 
        required=True, 
        help="Path to the root source directory (e.g., OneDrive/PixStar_Photos_RAW)."
    )
    parser.add_argument(
        '-o', '--output', 
        required=True, 
        help="Path to the output directory (e.g., OneDrive/PixStar_Photos_CLEAN)."
    )
    return parser.parse_args()

def clean_and_save_jpeg(file_path, output_path, quality):
    """
    Opens an image, strips all EXIF/metadata, converts to standard RGB, and saves as JPEG.
    """
    try:
        # 1. Open the image
        img = Image.open(file_path)
        
        # 2. Convert to standard RGB color space (crucial for frame compatibility)
        if img.mode not in ('RGB', 'L', 'P'):
            img = img.convert('RGB')
        
        # 3. Save the image, explicitly stripping EXIF data
        img.save(
            output_path, 
            format='JPEG', 
            quality=quality, 
            optimize=True,
            exif=b'' 
        )
        return True
    except Exception as e:
        print(f"\n[ERROR] Could not process {file_path}. Reason: {e}")
        return False

def main():
    """
    Main function to run the photo cleaning process.
    """
    args = parse_arguments()

    source_dir = os.path.abspath(args.source)
    output_dir = os.path.abspath(args.output)
    
    if not os.path.exists(source_dir):
        print(f"Error: Source directory not found at {source_dir}")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print(f"\n--- Pix-Star Photo Cleanup Utility ---")
    print(f"Source Directory: {source_dir}")
    print(f"Output Directory: {output_dir}")
    print(f"JPEG Quality: {JPEG_QUALITY}")
    print("-" * 40)

    total_processed = 0
    total_skipped = 0

    # os.walk iterates through all subdirectories
    for root, _, files in os.walk(source_dir):
        # Determine the relative path to maintain the subfolder structure
        relative_path = os.path.relpath(root, source_dir)
        output_root = os.path.join(output_dir, relative_path)
        
        if not os.path.exists(output_root):
            os.makedirs(output_root)

        # Use tqdm for a professional progress bar
        for file_name in tqdm(files, desc=f"Processing {relative_path}"):
            if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                source_file = os.path.join(root, file_name)
                target_file = os.path.join(output_root, file_name)
                
                if clean_and_save_jpeg(source_file, target_file, JPEG_QUALITY):
                    total_processed += 1
            else:
                total_skipped += 1

    print("-" * 40)
    print(f"✅ Cleanup Complete!")
    print(f"Total JPEGs Processed: {total_processed}")
    print(f"Other Files Skipped: {total_skipped}")

if __name__ == "__main__":
    main()
