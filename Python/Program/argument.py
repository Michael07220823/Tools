import argparse
'''
Usage example:
    args["model"]
    args["pickle"]
    args["image"]
'''
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required = True, help = "Input model path.")
ap.add_argument("-p", "--pickle", required = True, help = "Input pickle path.")
ap.add_argument("-i", "--image", required = True, help = "Input predict image path.")
args = vars(ap.parse_args())