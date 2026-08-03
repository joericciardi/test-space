from .database import get_db

def seed_clothes():
    db = get_db()
    if db.clothes.count_documents({}) > 0:
        return

    clothes_data = [
        {
            "type": "T-Shirts",
            "how_to_measure": {
                "Chest Width": "Flat across chest 1\" below armpit (double for body circumference)",
                "Body Length": "From highest shoulder point to the bottom hem",
                "Shoulder Width": "Seam to seam across upper back"
            },
            "sizes": {
                "Chest Width": {"XS": "18\"", "S": "20\"", "M": "22\"", "L": "24\"", "XL": "26\"", "2XL": "28\""},
                "Body Length": {"XS": "27\"", "S": "28\"", "M": "29\"", "L": "30\"", "XL": "31\"", "2XL": "32\""},
                "Shoulder Width": {"XS": "16.5\"", "S": "17.5\"", "M": "18.5\"", "L": "19.5\"", "XL": "20.5\"", "2XL": "21.5\""},
                "Sleeve Length": {"XS": "7.5\"", "S": "8\"", "M": "8.5\"", "L": "9\"", "XL": "9.5\"", "2XL": "10\""}
            }
        },
        {
            "type": "Dress Shirts",
            "how_to_measure": {
                "Neck / Collar": "Around the base of neck, leaving room for two fingers",
                "Sleeve Length": "Center back of neck, across shoulder point, down to wrist bone",
                "Chest Width": "Flat across chest 1\" below armpit"
            },
            "sizes": {
                "Neck Collar": {"XS": "13-13.5\"", "S": "14-14.5\"", "M": "15-15.5\"", "L": "16-16.5\"", "XL": "17-17.5\"", "2XL": "18-18.5\""},
                "Sleeve Length": {"XS": "31-32\"", "S": "32-33\"", "M": "33-34\"", "L": "34-35\"", "XL": "35-36\"", "2XL": "36-37\""},
                "Chest Circumference": {"XS": "32-34\"", "S": "35-37\"", "M": "38-40\"", "L": "42-44\"", "XL": "46-48\"", "2XL": "50-52\""},
                "Waist Circumference": {"XS": "26-28\"", "S": "29-31\"", "M": "32-34\"", "L": "36-38\"", "XL": "40-42\"", "2XL": "44-46\""}
            }
        },
        {
            "type": "Casual Pants & Chinos",
            "how_to_measure": {
                "Waist": "Natural waistline (where pants sit) or top of waistband flat",
                "Inseam": "From crotch seam down the inner leg to ankle",
                "Thigh / Leg Opening": "Thigh width flat at crotch; leg opening flat across bottom hem"
            },
            "sizes": {
                "Waist Tag Range": {"XS": "27-28\"", "S": "29-31\"", "M": "32-34\"", "L": "35-37\"", "XL": "38-41\"", "2XL": "42-44\""},
                "Actual Flat Waist": {"XS": "14.5\"", "S": "15.5\"", "M": "17\"", "L": "18.5\"", "XL": "20.5\"", "2XL": "22.5\""},
                "Front Rise": {"XS": "9.5\"", "S": "10\"", "M": "10.5\"", "L": "11\"", "XL": "11.5\"", "2XL": "12\""},
                "Thigh Flat": {"XS": "11\"", "S": "11.75\"", "M": "12.5\"", "L": "13.25\"", "XL": "14\"", "2XL": "15\""},
                "Leg Opening Flat": {"XS": "6.5\"", "S": "7\"", "M": "7.25\"", "L": "7.5\"", "XL": "8\"", "2XL": "8.25\""},
                "Standard Inseams": {"XS": "30 / 32\"", "S": "30 / 32\"", "M": "30 / 32 / 34\"", "L": "30 / 32 / 34\"", "XL": "32 / 34\"", "2XL": "32 / 34\""}
            }
        },
        {
            "type": "Denim / Jeans",
            "how_to_measure": {
                "Waist & Inseam": "Same as pants",
                "Front Rise": "From crotch seam straight up to top of front waistband",
                "Hip": "Across the widest part of hips/seat flat"
            },
            "sizes": {
                "Actual Flat Waist": {"XS (28)": "15\"", "S (30)": "16\"", "M (32)": "17\"", "L (34)": "18\"", "XL (36)": "19\"", "2XL (38)": "20\""},
                "Hip Flat": {"XS (28)": "18.5\"", "S (30)": "19.5\"", "M (32)": "20.5\"", "L (34)": "21.5\"", "XL (36)": "22.5\"", "2XL (38)": "23.5\""},
                "Front Rise": {"XS (28)": "9.75\"", "S (30)": "10.25\"", "M (32)": "10.75\"", "L (34)": "11.25\"", "XL (36)": "11.75\"", "2XL (38)": "12.25\""},
                "Thigh Flat": {"XS (28)": "10.5\"", "S (30)": "11.25\"", "M (32)": "12\"", "L (34)": "12.75\"", "XL (36)": "13.5\"", "2XL (38)": "14.25\""},
                "Leg Opening Flat": {"XS (28)": "6.25\"", "S (30)": "6.75\"", "M (32)": "7\"", "L (34)": "7.25\"", "XL (36)": "7.5\"", "2XL (38)": "7.75\""},
                "Standard Inseams": {"XS (28)": "30 / 32\"", "S (30)": "30 / 32\"", "M (32)": "30 / 32 / 34\"", "L (34)": "32 / 34\"", "XL (36)": "32 / 34\"", "2XL (38)": "32 / 34\""}
            }
        }
    ]

    db.clothes.insert_many(clothes_data)
