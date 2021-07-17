import os

# DIRECTORY INFORMATION
# DATASET = "imagenet" # UPDATE
# TEST_NAME ="FirstTest"
# ROOT_DIR = os.path.abspath('../')
# DATA_DIR = os.path.join(ROOT_DIR, 'DATASET/'+DATASET+'/')
OUT_DIR = '/content/drive/My Drive/Colab Notebooks/GAN/ChromaGAN/results'
# MODEL_DIR = os.path.join(ROOT_DIR, 'MODEL/'+DATASET+'/')
MODEL_DIR = '/content/drive/My Drive/Colab Notebooks/GAN/ChromaGAN/'
# LOG_DIR = os.path.join(ROOT_DIR, 'LOGS/'+DATASET+'/')

# TRAIN_DIR = "train"  # UPDATE
# TEST_DIR = "test" # UPDATE
TRAIN_DIR = '/content/dataset/train'
TEST_DIR = '/content/dataset/test'

# DATA INFORMATION
IMAGE_SIZE = 224
BATCH_SIZE = 10


# TRAINING INFORMATION
# PRETRAINED = "modelPretrained.h5" # UPDATE
NUM_EPOCHS = 5