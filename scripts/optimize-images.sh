#!/bin/bash

# Script to optimize images for web

if [ -z "$1" ]; then
    echo "Usage: ./optimize-images.sh /path/to/images/folder"
    exit 1
fi

IMAGE_DIR="$1"

if [ ! -d "$IMAGE_DIR" ]; then
    echo "Directory not found: $IMAGE_DIR"
    exit 1
fi

echo "Optimizing images in: $IMAGE_DIR"
echo ""

# Check if imagemagick is installed
if ! command -v convert &> /dev/null; then
    echo "ImageMagick not found. Installing..."
    # macOS
    if command -v brew &> /dev/null; then
        brew install imagemagick
    # Ubuntu/Debian
    elif command -v apt-get &> /dev/null; then
        sudo apt-get update && sudo apt-get install imagemagick
    else
        echo "Please install ImageMagick manually"
        exit 1
    fi
fi

# Optimize images
cd "$IMAGE_DIR"
for img in *.{jpg,jpeg,png,PNG,JPG,JPEG}; do
    if [ -f "$img" ]; then
        echo "Optimizing: $img"
        
        # Get file size before
        size_before=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img" 2>/dev/null)
        
        # Optimize based on file type
        if [[ "$img" =~ \.(jpg|jpeg|JPG|JPEG)$ ]]; then
            convert "$img" -quality 85 -strip "$img"
        elif [[ "$img" =~ \.(png|PNG)$ ]]; then
            convert "$img" -quality 85 -strip "$img"
        fi
        
        # Get file size after
        size_after=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img" 2>/dev/null)
        
        # Calculate savings
        savings=$((size_before - size_after))
        percent=$((savings * 100 / size_before))
        
        echo "  Size: $(numfmt --to=iec $size_before) → $(numfmt --to=iec $size_after) (${percent}% reduction)"
        echo ""
    fi
done

echo "✅ Image optimization complete!"
