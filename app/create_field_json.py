"""
This script is to be run after modifying any necessary functions within for page changes.
This will create a `page_x_fields.json` map that will be used to find the bounding boxes for each 
field on that page. The boxes and fields are unique to each document and must be created from
specific coordinates due to the flattened nature of signed PDFs. Therefore, this should only be used
as a developer tool and not by the end user.
"""

import json
from pdf2image import convert_from_path
