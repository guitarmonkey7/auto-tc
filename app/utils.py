import os
from pathlib import Path

OUTPUT_LOCATION = "auto-tc_pdf_converter_output"


def get_local_save_path(file_name):
    dir = os.path.join(os.path.expanduser("~"), "Documents", OUTPUT_LOCATION)
    if not os.path.isdir(dir):
        os.mkdir(dir)
    return os.path.join(dir, file_name)


repo_root = Path(__file__).parents[1]
pdf_path = repo_root.joinpath("docs/F201 - Purchase and Sale Agreement test.pdf")
