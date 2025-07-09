#!/bin/bash

# Script to create new blog posts with proper structure

if [ -z "$1" ]; then
    echo "Usage: ./new-post.sh 'Post Title'"
    echo "Example: ./new-post.sh 'Understanding Image Histograms'"
    exit 1
fi

# Convert title to URL-friendly format
POST_TITLE="$1"
POST_SLUG=$(echo "$POST_TITLE" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-\|-$//g')
POST_DIR="content/posts/$POST_SLUG"

# Create post directory
mkdir -p "$POST_DIR/images"

# Get current date
CURRENT_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Create post file
cat > "$POST_DIR/index.md" << EOF
---
title: "$POST_TITLE"
date: $CURRENT_DATE
draft: true
description: "Brief description of the article"
tags: ["tag1", "tag2", "tag3"]
categories: ["Fundamentals"]
series: [""]
cover:
    image: "images/cover.png"
    alt: "Cover image description"
    caption: "Cover image caption"
weight: 1
---

## Introduction

Write your introduction here...

## Main Content

### Section 1

Content for section 1...

### Section 2

Content for section 2...

## Code Example

\`\`\`cpp
// Your code example here
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
\`\`\`

## Conclusion

Summarize your article...

## Next Steps

- Point 1
- Point 2
- Point 3

## Resources

- [Link 1](https://example.com)
- [Link 2](https://example.com)

---

*Have questions about this topic? [Contact me](/contact/) or leave a comment below.*
EOF

echo "✅ New post created: $POST_DIR/index.md"
echo "📁 Images folder created: $POST_DIR/images/"
echo "📝 Edit your post and add images to the images folder"
echo "🚀 Run 'hugo server -D' to preview your draft"
