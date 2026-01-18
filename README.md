This project implements **Fast Neural Style Transfer** using PyTorch. It allows you to "borrow" the artistic style of one image (like a painting) and apply it to the content of another image (like a photo).

Unlike the original optimization-based style transfer, this version trains a **Transformer Network**, which allows the stylization process to happen in near real-time once the model is trained.

## 🚀 Features
*   **Training:** Train a unique model for a specific style in ~20-30 minutes on a T4 GPU.
*   **Fast Inference:** Apply styles to images in milliseconds on a GPU or seconds on a CPU.
*   **Lightweight:** The resulting models are only **~6.4 MB**, making them easy to share and run on low-end hardware.

## 💻 Hardware Requirements

| Task | Minimum Requirement | Recommended |
| :--- | :--- | :--- |
| **Training** | NVIDIA GPU (e.g., Tesla T4) | 8GB+ VRAM |
| **Inference** | Dual Core CPU (e.g., Pentium G4560) | NVIDIA GPU |
| **RAM** | 4 GB | 8 GB+ |


## 📂 Project Structure
*   `neural_style.py`: The main script for training and evaluation.
*   `transformer_net.py`: The architecture of the model.
*   `vgg.py`: The pre-trained VGG16 model used to calculate "style loss."
*   `*.model`: Your trained style weights (approx. 6.4 MB).

---

## 🎨 Tips for Best Results
1.  **Style Image:** Use images with heavy textures and vibrant colors (e.g., Van Gogh, Picasso, Abstract patterns).
2.  **Resolution:** Training at 512px provides a good balance between detail and speed.
3.  **Content Scale:** If the output looks too zoomed in, adjust the `--content-scale` parameter during evaluation.

## 📜 Credits
This implementation is based on the [PyTorch Fast Style Transfer examples](https://github.com/pytorch/examples/tree/main/fast_neural_style) and the inspiration from Green Code (https://www.youtube.com/watch?v=D3mz-fAUBVc&t=198s)
