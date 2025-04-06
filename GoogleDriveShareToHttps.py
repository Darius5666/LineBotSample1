def Modify(Drive_url):
    file_id = Drive_url.split('/')[5]
    https_url = f"https://drive.google.com/uc?export=view&id={file_id}"
    return https_url
url="https://drive.google.com/file/d/1vTxcA1ZMxUrtS3JIk_gJLfyNBkzYbOf4/view?usp=sharing"
print(Modify(url))