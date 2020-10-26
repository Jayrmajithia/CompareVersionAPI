from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    s ='''
    Hello welcome to Version Comparison application<br>
    The compare endpoint is used for comparing versions in this application.<br>
    "/compare/versionA/versionB": This endpoint returns the comparison of the two versions.<br>
    To see an example try go through the readme if any confusion
    '''
    return s

# This method is used to get values between two "." or the inital and first "." or "." and the end of the string
# if we are at the end of the string and this function is called it will return the len(version) and 0 as it is a kind of padding we need
def getPatchHelper(version, index):
    if index >= len(version):
        return len(version), 0
    patch = 0
    while index < len(version) and version[index] != ".":
        patch = patch * 10 + int(version[index])
        index += 1
    return index, patch

# This method is used to check the version input is in the format of our assumption or not
def check(version):
    for val in version:
        if val == ".":
            continue
        if not val.isnumeric():
            return False
    return True

@app.route('/compare/<versionA>/<versionB>')
def copareStringWay1(versionA, versionB):
    # check the format of the input provided to us and if not according to the format returns stating that input of specific format
    if not (check(versionA) and check(versionB)) or not versionA or not versionB:
        return "Enter the version numbers in with only numeric values and \".\" in it and nothing else"
    n1, n2 = len(versionA), len(versionB)
    index1, index2 = 0, 0
    while index1 < n1 or index2 < n2:
        index1, patch1 = getPatchHelper(versionA, index1)
        index2, patch2 = getPatchHelper(versionB, index2)
        # If value of patches are not same we know that there might be one version before or after the second version
        if patch1 != patch2:
            # returns the value accordingly
            return versionA + " is \"after\" " + versionB if patch1 > patch2 else versionA + " is \"before\" " + versionB
        index1 += 1
        index2 += 1
    return versionA + " is \"equal\" " + versionB


if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=5000, debug = True)
