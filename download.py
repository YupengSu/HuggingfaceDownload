from datasets import load_dataset

dataset = load_dataset('winogrande','winogrande_xl')
dataset.save_to_disk("./datasets/winogrande")