#!/bin/bash

file_count=0

for file in /etc/*; do
	if [ -f "$file" ] && [ ! -L "$file" ]; then
    ((file_count++))
  fi
done

echo "Кількість файлів у каталозі /etc : $file_count"
