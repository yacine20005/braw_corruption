#!/bin/bash
INPUT_FOLDER="frames"
OUTPUT="output.braw"
FPS=24  # Remplacer par la vraie valeur

# Nécessite DaVinci Resolve Studio ou braw-tools
braw-tools encode --input "$INPUT_FOLDER" --output "$OUTPUT" --fps $FPS