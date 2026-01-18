
model_filename = "image.model"

!python neural_style/neural_style.py train \
    --dataset /content/dataset \
    --style-image "images/style-images/{style_image_name}" \
    --save-model-dir /content/ \
    --epochs 1 \
    --accel \
    --batch-size 4


import os
if os.path.exists("/content/style_image.model"):
    os.rename("/content/style_image.model", f"/content/{model_filename}")

print(f"Training Complete! Model saved as /content/{model_filename}")
