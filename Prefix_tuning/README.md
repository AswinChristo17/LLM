Fine-Tuning DeepSeek-R1-Distill-Qwen-1.5B with Prefix Tuning

Overview

This project fine-tunes the DeepSeek-R1-Distill-Qwen-1.5B model using Prefix Tuning on a supervised dataset based on the Game of Thrones book. The model is loaded with 4-bit quantization for efficient training and inference.

Features

Model: deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B

Fine-Tuning Method: Prefix Tuning (Parameter-Efficient Fine-Tuning)

Dataset: Supervised dataset from the Game of Thrones book

Quantization: 4-bit (BitsAndBytesConfig)

Training Framework: Hugging Face Transformers + PEFT (Parameter-Efficient Fine-Tuning)

Device: Auto-mapped (CPU/GPU support)