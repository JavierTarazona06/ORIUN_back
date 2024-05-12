#!/bin/bash
set -e  # Exit on errors

mkdir -p $GITHUB_WORKSPACE/django_project/data/test_files

source_dir="$GITHUB_WORKSPACE/django_project/data/test_files_gpg"
target_dir="$GITHUB_WORKSPACE/django_project/data/test_files"

for file in "$source_dir"/*; do
  if [[ -f "$file" ]]; then
    encrypted_file="${file##*/}"  # Extract filename
    original_file="${encrypted_file%.gpg}"  # Remove .gpg extension
    gpg --quiet --batch --yes --decrypt --passphrase=$FILES_PW \
      --output "$target_dir/$original_file" "$file"
  fi
done