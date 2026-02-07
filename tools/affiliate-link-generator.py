#!/usr/bin/env python3
"""
Affiliate Link Generator
Creates tracking links for various programs
"""

# Amazon Associates (apply at https://affiliate-program.amazon.com)
AMAZON_TAG = "novaagent-20"  # Replace with actual tag after approval

def amazon_link(asin, product_name=""):
    """Generate Amazon affiliate link"""
    return f"https://www.amazon.com/dp/{asin}?tag={AMAZON_TAG}"

# Common products for AI/automation niche
AMAZON_PRODUCTS = {
    "python_crash_course": {"asin": "B07J4521M3", "name": "Python Crash Course Book"},
    "raspberry_pi_4": {"asin": "B07TC2BK1X", "name": "Raspberry Pi 4"},
    "external_ssd": {"asin": "B07D998212", "name": "Samsung T7 Portable SSD"},
    "webcam": {"asin": "B07K95WFWM", "name": "Logitech C920 Webcam"},
    "microphone": {"asin": "B078NGCF3X", "name": "Blue Yeti Microphone"},
}

# DigitalOcean Referral
# Apply at: https://www.digitalocean.com/referral-program
DIGITALOCEAN_REF = "YOUR_REF_CODE_HERE"

def digitalocean_link():
    return f"https://m.do.co/c/{DIGITALOCEAN_REF}"

# Vercel Referral
# Apply at: https://vercel.com/referral
VERCEL_REF = "YOUR_REF_CODE_HERE"

def vercel_link():
    return f"https://vercel.com/?ref={VERCEL_REF}"

# Notion Affiliate
# Apply at: https://www.notion.so/affiliates
NOTION_REF = "YOUR_REF_CODE_HERE"

def notion_link():
    return f"https://www.notion.so/?ref={NOTION_REF}"

if __name__ == "__main__":
    print("Affiliate Link Generator")
    print("=" * 50)
    print()
    print("Apply to these programs:")
    print("1. Amazon Associates: https://affiliate-program.amazon.com")
    print("2. DigitalOcean Referral: https://www.digitalocean.com/referral-program")
    print("3. Vercel Referral: https://vercel.com/referral")
    print("4. Notion Affiliates: https://www.notion.so/affiliates")
    print("5. Impact (multiple SaaS): https://impact.com")
    print("6. ShareASale: https://shareasale.com")
    print()
    print("Once approved, update the codes in this file.")
    print()
    print("Sample Amazon links (ready when approved):")
    for key, product in AMAZON_PRODUCTS.items():
        print(f"  {product['name']}: {amazon_link(product['asin'])}")
