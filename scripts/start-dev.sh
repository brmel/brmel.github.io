#!/bin/bash

# Start Hugo development server
echo "🚀 Starting Hugo development server..."
echo "📱 Site will be available at: http://localhost:1313"
echo "⏹️  Press Ctrl+C to stop the server"
echo ""

# Kill any existing Hugo servers
pkill -f "hugo server" 2>/dev/null || true

# Wait a moment for cleanup
sleep 1

# Start server with live reload
hugo server -D --bind 0.0.0.0 --baseURL http://localhost:1313/
