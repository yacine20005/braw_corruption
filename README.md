# Attempt to Recover Corrupted Blackmagic RAW Images

This repository documents an attempt to recover images from corrupted `.braw` files, which occurred during an academic project in a film studies program.

## Context

As part of a university film project, my friend experienced the loss of some footage when a loose connection on her Blackmagic camera resulted in corrupted `.braw` files. Having participated in the filming process myself, I felt personally invested and decided to help her try to recover these important images for her cinema studies work.

## Objective

The goal was to:
- Extract valid images from `.braw` files
- Detect corrupted or missing images
- Automatically generate replacement images using a generative model (deep learning)

## Approach

- Extracting frames using open source tools and the Blackmagic RAW SDK
- Detecting corrupted images with Python scripts (similarity analysis, black frame detection, etc.)
- Attempting to use a generative model to reconstruct missing images

## Result

The recovery attempt has not succeeded so far. The pipeline remains experimental and incomplete, but this project allowed me to learn:
- How the Blackmagic RAW format and its SDK work
- How to use Python scripts for image analysis
- The basics of image generation with AI
- The challenges of recovering corrupted video data

## Acknowledgements

Thanks to my friend for her trust on this project and for allowing me to experiment with her footage.

---

> **Note**: This repository is not a functional recovery tool, but a record of a learning and experimentation process around digital video and AI.
