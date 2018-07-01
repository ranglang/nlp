import json
import shutil
import sys
import logging

from allennlp.commands import main

config_file = "experiments/quora.json"

# Use overrides to train on CPU.
overrides = json.dumps({
    "train_data_path": "(/data/Quora_question_pair_partition.zip)#Quora_question_pair_partition/train.tsv",
    "validation_data_path": "(/data/Quora_question_pair_partition.zip)#Quora_question_pair_partition/dev.tsv",
    "trainer": {"cuda_device": 0},
    "vocabulary": {"directory_path": "./temp/vocabulary"}
})

serialization_dir = "./temp/bimpm"

# Training will fail if the serialization directory already
# has stuff in it. If you are running the same training loop
# over and over again for debugging purposes, it will.
# Hence we wipe it out in advance.
# BE VERY CAREFUL NOT TO DO THIS FOR ACTUAL TRAINING!
shutil.rmtree(serialization_dir, ignore_errors=True)

# Assemble the command into sys.argv
sys.argv = [
    "allennlp",  # command name, not used by main
    "train",
    config_file,
    "-s", serialization_dir,
    "--include-package", "my_library",
    "-o", overrides,
]

logging.basicConfig(level=logging.WARNING)

main()