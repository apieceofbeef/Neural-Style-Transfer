import os


!mkdir -p /content/dataset
%cd /content/dataset

# Download COCO images
if not os.path.exists('val2014.zip'):
    !wget http://images.cocodataset.org/zips/val2014.zip
    !unzip -q val2014.zip
    print("Dataset Unzipped successfully!")

%cd /content/examples/fast_neural_style
