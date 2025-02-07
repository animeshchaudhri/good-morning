from pygoogle_image import image as pi

def download_images(keyword, num_images=5):
    # Create a downloader object
    downloader = pi.download

    # Download images
    downloader(keyword, limit=num_images)

# Example usage
download_images("Isagi Yoichi", num_images=1000)
