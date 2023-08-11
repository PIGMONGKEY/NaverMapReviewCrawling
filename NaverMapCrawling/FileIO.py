def open_file(brand_name):
    return open(f"../Reviews/{brand_name}", "w")


def write_file(file, review):
    file.write(review + "\n\n")


def close_file(file):
    file.close()
