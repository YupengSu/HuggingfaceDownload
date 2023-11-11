from datasets import load_dataset

dataset = load_dataset('super_glue','boolq')
dataset.save_to_disk("./datasets/boolq")