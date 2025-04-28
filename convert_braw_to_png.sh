#!/bin/bash
INPUT="input.braw"
OUTPUT_FOLDER="frames"
FPS=24 


braw-tools decode --input "$INPUT" --output "$OUTPUT_FOLDER" --format png --fps $FPS