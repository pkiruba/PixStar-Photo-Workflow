# cleanup_photos.py

import os
import argparse
from PIL import Image
from tqdm import tqdm
import pandas as pd

# --- Configuration Constants ---
JPEG_QUALITY = 90


def parse_arguments():
    """
    Handles command-line argument parsing for source, output, and report file name.
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
    parser.add_argument(
        '-r', '--report',
        default="photo_cleanup_report.csv",
        help="CSV file name for the processing report (default: photo_cleanup_report.csv)."
    )
    return parser.parse_args()


def clean_and_save_jpeg(file_path, output_path, quality):
    """
    Opens an image, strips all EXIF/metadata, converts to standard RGB, and saves as JPEG.
    Returns processing metadata.
    """
    try:
        size_before_kb = os.path.getsize(file_path) / 1024

        img = Image.open(file_path)
        width, height = img.size

        if img.mode not in ('RGB', 'L', 'P'):
            img = img.convert('RGB')

        img.save(
            output_path,
            format='JPEG',
            quality=quality,
            optimize=True,
            exif=b''
        )

        size_after_kb = os.path.getsize(output_path) / 1024

        return {
            "success": True,
            "width": width,
            "height": height,
            "size_before_kb": round(size_before_kb, 2),
            "size_after_kb": round(size_after_kb, 2),
            "error": None
        }

    except Exception as e:
        return {
            "success": False,
            "width": None,
            "height": None,
            "size_before_kb": None,
            "size_after_kb": None,
            "error": str(e)
        }


def main():
    """
    Main function to run the photo cleaning process.
    """
    args = parse_arguments()

    source_dir = os.path.abspath(args.source)
    output_dir = os.path.abspath(args.output)
    report_file = args.report

    if not os.path.exists(source_dir):
        print(f"Error: Source directory not found at {source_dir}")
        return

    os.makedirs(output_dir, exist_ok=True)

    print(f"\n--- Pix-Star Photo Cleanup Utility ---")
    print(f"Source Directory: {source_dir}")
    print(f"Output Directory: {output_dir}")
    print(f"JPEG Quality: {JPEG_QUALITY}")
    print(f"Report File: {report_file}")
    print("-" * 40)

    total_processed = 0
    total_skipped = 0
    results = []

    for root, _, files in os.walk(source_dir):
        relative_path = os.path.relpath(root, source_dir)
        output_root = os.path.join(output_dir, relative_path)
        os.makedirs(output_root, exist_ok=True)

        for file_name in tqdm(files, desc=f"Processing {relative_path}"):
            if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                source_file = os.path.join(root, file_name)
                target_file = os.path.join(output_root, file_name)

                result = clean_and_save_jpeg(
                    source_file,
                    target_file,
                    JPEG_QUALITY
                )

                results.append({
                    "file": source_file,
                    "status": "SUCCESS" if result["success"] else "FAILED",
                    "width": result["width"],
                    "height": result["height"],
                    "size_before_kb": result["size_before_kb"],
                    "size_after_kb": result["size_after_kb"],
                    "error": result["error"]
                })

                if result["success"]:
                    total_processed += 1
            else:
                total_skipped += 1

    # Write processing report
    df = pd.DataFrame(results)
    df.to_csv(report_file, index=False)

    print("-" * 40)
    print("✅ Cleanup Complete!")
    print(f"Total Images Processed: {total_processed}")
    print(f"Other Files Skipped: {total_skipped}")
    print(f"📄 Processing report saved to: {report_file}")


if __name__ == "__main__":
    main()
