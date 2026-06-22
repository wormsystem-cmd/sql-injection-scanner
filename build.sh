#!/bin/bash

# SQL Injection Scanner Build Script
# © Copyright © 2024 WORM SYSTEM - All Rights Reserved

set -e

echo "🔨 Building SQL Injection Scanner..."

# التحقق من Go
if ! command -v go &> /dev/null; then
    echo "❌ Go is not installed. Please install Go 1.21 or higher."
    exit 1
fi

# الحصول على إصدار Go
GO_VERSION=$(go version | awk '{print $3}' | sed 's/go//')
echo "✓ Go version: $GO_VERSION"

# تنزيل المتطلبات
echo "📦 Downloading dependencies..."
go mod download
go mod tidy

# البناء
echo "🔨 Building binary..."
go build -o scanner .

echo ""
echo "✅ Build completed successfully!"
echo "🚀 Run with: ./scanner --help"
echo ""
echo "© WORM SYSTEM - Enterprise Security Solutions"
