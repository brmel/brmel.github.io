#!/bin/bash

echo "Building Hugo site for production..."

# Clean public directory
if [ -d "public" ]; then
    rm -rf public
    echo "Cleaned public directory"
fi

# Build site
hugo --gc --minify

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
    echo "Site built in ./public directory"
    echo "Files ready for deployment"
else
    echo "❌ Build failed!"
    exit 1
fi
