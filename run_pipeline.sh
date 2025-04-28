#!/bin/bash

# Convertir .braw -> PNG
chmod +x convert_braw_to_png.sh
./convert_braw_to_png.sh

# Détecter les images corrompues
python3 detect_corrupted.py

# Générer les images manquantes
python3 selective_rife.py

# Reconstruire le .braw final
chmod +x reconstruct_video.sh
./reconstruct_video.sh