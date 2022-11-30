import base64
def convertToImg(base64code,dataFileName):
    imgdata = base64.b64decode(base64code)
    filename = 'static/img/'+dataFileName 
    with open(filename, 'wb') as f:
        f.write(imgdata)
    return '/'+filename

