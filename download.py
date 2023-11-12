from datasets import load_dataset

dataset = load_dataset('openbookqa','main')
dataset.save_to_disk("./datasets/openbookqa")