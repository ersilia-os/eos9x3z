# imports
import os
import csv
import sys
import tempfile
import shutil

from chemprop.args import PredictArgs
from chemprop.train.make_predictions import make_predictions

# variables
root = os.path.dirname(os.path.abspath(__file__))
checkpoints_dir = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

tmp_folder = tempfile.mkdtemp(prefix="ersilia-")
tmp_folder = "tmp"
os.makedirs(tmp_folder, exist_ok=True)
tmp_input = os.path.join(tmp_folder, "input.csv")
with open(tmp_input, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["smiles"])
    for s in smiles_list:
        writer.writerow([s])
tmp_output = os.path.join(tmp_folder, "output.csv")

def run():
    argv = [
        "--test_path", f"{tmp_input}",
        "--checkpoint_dir", f"{checkpoints_dir}",
        "--preds_path", f"{tmp_output}",
        "--features_generator", "rdkit_2d_normalized",
        "--no_features_scaling",
        "--num_workers", "0",
    ]

    args = PredictArgs().parse_args(argv)
    make_predictions(args)

run()

outputs = []
with open(tmp_output, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        outputs += [float(r[1])]

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["gn_activity"])
    for o in outputs:
        writer.writerow([o])

shutil.rmtree(tmp_folder)