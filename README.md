# 🖼️ PixStar Digital Photo Frame Management
---
**Standard Operating Procedure (SOP) for Organizing and Syncing Photos from OneDrive**

This workflow ensures all photos for the Pix-Star frame are managed simply and consistently, using a **YYYY_MM** structure and a Python script (`cleanup_photos.py`) for optimized file preparation.

---

## 1. ⬇️ Installation and Setup

### Prerequisites

You must have **Python** installed on your system.

1.  **Clone the Repository**
    ```bash
    git clone [Your_Repo_URL]
    cd [your-repo-name]
    ```

2.  **Install Dependencies**
    The script requires the Pillow library for image processing and `tqdm` for the progress bar.
    ```bash
    pip install Pillow tqdm
    ```

## 2. 📂 OneDrive File Structure and File Handling

All photo albums intended for the Pix-Star frame **MUST** be located within a single, dedicated directory in OneDrive.

### File Handling Policy (Important!)

The `cleanup_photos.py` script is an **optimization and cleaning tool** designed only for JPEGs. You must pre-convert proprietary formats to JPEG before running the script.

| File Type | Requires Pre-Conversion? | Script Action |
| :--- | :--- | :--- |
| **Proprietary RAW (.NEF, .CR2, .DNG)** | **YES.** | **The script will SKIP these files.** Must be converted to JPEG externally. |
| **High Efficiency (.HEIC, .HEIF)** | **YES.** | **The script will SKIP these files.** Convert to JPEG externally. |
| **Standard JPEG (.jpg, .jpeg)** | NO. | The script will **CLEAN** and **OPTIMIZE** these files (strip metadata, convert to RGB). |

### Directory Structure

| Folder | Purpose |
| :--- | :--- |
| **Source** (e.g., `Original_Photos_Source`) | Where your raw/uncleaned JPEGs (and other files) are temporarily saved. **DO NOT LINK THIS TO PIX-STAR.** |
| **Target** (e.g., `OneDrive/PixStar_Photos_CLEAN`) | **This is the folder structure you link to Pix-Star.** It contains only cleaned, optimized JPEGs. |

### Album Naming Convention

All subdirectories within your **Target** folder should follow the `YYYY_MM_[Description]` format.

```text
└── OneDrive/
    └── PixStar_Photos_CLEAN/  <-- Folder linked to Pix-Star
        ├── 2025_01_General/
        ├── 2025_02_Smith_Wedding/
        └── EVERGREEN_Landscapes_Scenery/
```
## 3. 🚀 Usage (Running the Cleanup Script)

Execute the provided Python script, `cleanup_photos.py`, using the command line.

### Command Syntax
```text
python cleanup_photos.py -s <SOURCE_DIR> -o <OUTPUT_DIR>
```

| Argument | Description |
| :--- | :--- |
| `-s` or `--source` | **Required.** Full path to your folder containing the original/raw JPEGs. |
| `-o` or `--output` | **Required.** Full path to the OneDrive folder (`PixStar_Photos_CLEAN`) where the optimized JPEGs will be saved. |

### Example Execution
```text
python cleanup_photos.py --source "/Users/YourName/Desktop/Photo_Uploads" --output "/Users/YourName/OneDrive/PixStar_Photos_CLEAN"
```
### Script Functionality Summary

* Metadata Stripping: Removes all complex EXIF/IPTC/XMP data to prevent skipped photos.
* Color Space Fix: Converts images to the standard RGB color space.
* Optimization: Re-saves the files as high-quality (90%) JPEGs.
* Folder Structure: Automatically maintains the subdirectory structure.

## 4. ✅ Pix-Star Frame Best Practices

These tips ensure the best experience on the digital frame.

### Linking Photos

* In your Pix-Star web account, disconnect any old, direct links to your OneDrive source folders.

* Connect the subdirectories within your `PixStar_Photos_CLEAN` folder.

### Ensuring Full Cycle Playback

If you use "Random" sorting, photos will repeat randomly. To ensure every photo is displayed once before the cycle repeats:
1. On the Pix-Star frame, navigate to the Slideshow Options menu.
2. Change the Sorting Mode from "Random" to "Newest first" or "Oldest first".

## 5.💡 Future Maintenance Options

Beyond Pillow, here are other best options for photo maintenance and conversion:

1. ImageMagick (CLI Tool): A powerful, cross-platform command-line tool. You can use it in your script or directly in a bash/command line workflow for bulk processing, resizing, and metadata stripping.
2. ExifTool (CLI Tool): The industry standard for reading, writing, and editing metadata (EXIF, IPTC, XMP). If you ever need to selectively keep specific metadata (like date taken), this is the tool to use.
3. HEIC/RAW Pre-Conversion: If you frequently use HEIC or RAW files, consider a dedicated utility (like a simple shell script using sips on macOS) to batch convert them to JPEGs before running your Pillow script. This can simplify the workflow, as Pillow is mainly for processing existing raster images (like JPEGs).
