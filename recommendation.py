def recommend_products(search_product):
    products = {
        "mobile": [
            {
                "name": "Fast Charging Adapter",
                "brand": "Samsung",
                "company": "Samsung Electronics",
                "price": "₹1,299"
            },
            {
                "name": "Power Bank 20000mAh",
                "brand": "MI",
                "company": "Xiaomi",
                "price": "₹1,899"
            },
            {
                "name": "Wireless Headphones",
                "brand": "boAt",
                "company": "Imagine Marketing",
                "price": "₹2,499"
            },
            {
                "name": "Mobile Back Cover",
                "brand": "Spigen",
                "company": "Spigen Inc.",
                "price": "₹999"
            },
            {
                "name": "In-Ear Earphones",
                "brand": "Realme",
                "company": "Realme Pvt Ltd",
                "price": "₹799"
            }
        ],

        "laptop": [
            {
                "name": "Laptop Backpack",
                "brand": "American Tourister",
                "company": "Samsonite",
                "price": "₹1,499"
            },
            {
                "name": "Wireless Mouse",
                "brand": "Logitech",
                "company": "Logitech Inc.",
                "price": "₹899"
            },
            {
                "name": "Keyboard",
                "brand": "HP",
                "company": "HP Inc.",
                "price": "₹1,099"
            },
            {
                "name": "Cooling Pad",
                "brand": "Zinq",
                "company": "Zinq Technologies",
                "price": "₹1,299"
            },
            {
                "name": "Pendrive 64GB",
                "brand": "SanDisk",
                "company": "Western Digital",
                "price": "₹699"
            }
        ]
    }

    return products.get(search_product.lower(), [])
