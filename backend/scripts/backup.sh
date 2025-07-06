#!/bin/bash

# Database backup script for SellApp Django Backend
echo "💾 Creating database backup..."

# Set backup directory
BACKUP_DIR="backups"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="${BACKUP_DIR}/backup_${DATE}.json"

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Create backup
echo "📦 Creating backup: $BACKUP_FILE"
python manage.py dumpdata --exclude auth.permission --exclude contenttypes > $BACKUP_FILE

# Check if backup was successful
if [ $? -eq 0 ]; then
    echo "✅ Backup created successfully: $BACKUP_FILE"
    
    # Get file size
    FILE_SIZE=$(du -h $BACKUP_FILE | cut -f1)
    echo "📊 Backup size: $FILE_SIZE"
    
    # Keep only last 10 backups
    echo "🧹 Cleaning old backups (keeping last 10)..."
    ls -t $BACKUP_DIR/backup_*.json | tail -n +11 | xargs -r rm
    
    echo "🎉 Backup process completed!"
else
    echo "❌ Backup failed!"
    exit 1
fi 