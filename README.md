# 🖼️ PixStar Digital Photo Frame Management
---
**Standard Operating Procedure (SOP) for Organizing and Syncing Photos from OneDrive**

This workflow ensures all photos for the Pix-Star frame are managed simply and consistently, using a **YYYY_MM** structure and a Python script for optimized file preparation.

---

## 1. 📂 OneDrive File Structure

All photo albums intended for the Pix-Star frame **MUST** be located within a single, dedicated directory in OneDrive.

### Root Directory

* **Name:** `PixStar_Photos_CLEAN/` (This folder will hold the optimized photos after cleanup)

The Pix-Star frame is configured to link to the subdirectories within this root folder, creating individual Web Albums.

### Album Naming and Nesting

Use the `YYYY_MM_[Description]` format for easy sorting and reference.

```text
└── OneDrive/
    └── PixStar_Photos_CLEAN/  <-- Folder linked to Pix-Star
        ├── 2025_01_General/
        ├── 2025_02_Smith_Wedding/
        └── EVERGREEN_Landscapes_Scenery/
```
## 2. 🧹 Photo Cleanup & Optimization Script

To ensure 100% compatibility and fast loading on the Pix-Star frame, all photos must be stripped of complex metadata (like those from iPhone/DSLR RAW conversions) and saved as a standard JPEG.
Prerequisites

Python: Ensure you have Python installed.

Pillow and tqdm: Install the required libraries:
    `pip install Pillow tqdm`
    
Usage

Use the provided cleanup_photos.py script to process your source photos into the optimized destination folder.

Example Command:

```
python cleanup_photos.py -s /Users/YourName/Original_Photos_Source -o /Users/YourName/OneDrive/PixStar_Photos_CLEAN

Argument,Description
-s or --source,"Required. The path to your raw/original photo storage (e.g., your local drive folder where you dump photos)."
-o or --output,"Required. The path to the target folder inside your OneDrive that will be linked to Pix-Star (e.g., .../OneDrive/PixStar_Photos_CLEAN)."
```
Script Functionality

The script performs the following critical steps:

    Metadata Stripping: Removes all complex EXIF/IPTC/XMP data.

    Color Space Fix: Converts images to the standard RGB color space.

    Optimization: Re-saves the files as high-quality (90%) JPEGs.

    Folder Structure: Automatically maintains the subdirectory structure.

## 3. ✅ Pix-Star Best Practices

These tips ensure the best experience on the digital frame.

    Connectivity: Keep the frame connected to Wi-Fi for automatic syncs.

    Album Size: Avoid making extremely large albums for faster loading.

    Auto-Sync: Ensure auto-sync is enabled for all linked OneDrive albums.

    Slideshow Mode: To ensure every photo runs before repeating, change the frame's Sorting Mode from "Random" to "Newest/Oldest first" in the slideshow options menu.
