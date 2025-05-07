"""
This script is to be run after modifying any necessary functions within for page changes.
This will create a `page_x_fields.json` map that will be used to find the bounding boxes for each 
field on that page. The boxes and fields are unique to each document and must be created from
specific coordinates due to the flattened nature of signed PDFs. Therefore, this should only be used
as a developer tool and not by the end user.
"""

import json
from pdf2image import convert_from_path

def page_1_fields():
    return {
        1: {
            "Purchase and Sale": {
                "Property Identification": {
                    "Address": (),
                    "City": (),
                    "County": (),
                    "Zip Code": (),
                    "MLS Number": (),
                    "Tax Parcel I.D. Number": ()
                },
                "Legal Description": {
                    "Box(1)": (),
                    "Box(2)": (),
                    "Box(3)": {
                        "Deed Book": (),
                        "Page": (),
                    },
                    "Box(4)": {
                        "Land Lot(s)": (),
                        "District": (),
                        "Section/GMD": (),
                        "Lot": (),
                        "Block": (),
                        "Unit": (),
                        "Phase/Section": (),
                        "Subdivision/Development": (),
                        "Plat Boot": (),
                        "Page": ()
                    }
                }
            }
        },
        2: {
            "Purchase Price": ()
        },
        3: {
            "Closing Costs": ()
        },
        4: {
            "Closing Date and Possession": {
                "Closing Date": (),
                "Upon Closing": (),
                "Days after Closing": (),
                "Time": (),
                "AM/PM": ()
            }
        },
        5: {
            "Closing Attorney": (),
            "Phone Number": ()
        },
        6: {
            "Holder (of Earnest Money)": ()
        },
        7: {
            "Earnest Money": {
                "a": {
                    "Check Box": (),
                    "Blank": ()
                },
                "b": {
                    "Check Box": (),
                    "Blank": (),
                    "Days": ()
                },
                "c": {
                    "Check Box": (),
                    "Blank": ()
                }
            }
        },
        8: {
            "Inspection and Due Diligence": {
                "Due Diligence Period": (),
                "Option Payment": {
                    "Option Money": (),
                    "Check": (),
                    "ACH": (),
                    "Wire Transfer": (),
                    "As of Offer Date": (),
                    "Days from Binding Agreement": (),
                    "Additional applied toward purchase price": {
                        "Shall": (),
                        "Shall Not": ()
                    }
                }
            }
        },
        9: {
            "Lead-based Paint": {
                "Prior to 1978": {
                    "was": (),
                    "was not": ()
                }
            }
        },
        10: {
            "Brokerage Relationships": {
                "a": {
                    "Buyer's Broker": (),
                    "Box(1)": (),
                    "Box(2)": (),
                    "Box(3)": (),
                    "Box(4)": (),
                    "Representative": ()
                },
                "b": {
                    "Seller's Broker": (),
                    "Box(1)": (),
                    "Box(2)": (),
                    "Box(3)": (),
                    "Box(4)": (),
                    "Representative": ()
                },
                "c": {
                    "Material Relationship": ()
                }
            }
        },
        11: {
            "Time Limit": {
                "Time": (),
                "A/P": (),
                "Date": ()
            }
        },
        "Buyer initials": (),
        "Seller initials": (),
        "Realtor": ()
    }