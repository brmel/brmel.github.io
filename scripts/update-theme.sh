#!/bin/bash

echo "Updating PaperMod theme..."

# Update theme submodule
git submodule update --remote --merge

# Check for any conflicts
if [ $? -eq 0 ]; then
    echo "✅ Theme updated successfully!"
    echo "🔄 Please test your site locally before deploying"
else
    echo "❌ Theme update failed!"
    echo "Please resolve conflicts manually"
    exit 1
fi
