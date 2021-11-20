import easyocr
def recognise_text(image_file):
  bounds = reader.readtext('/content/tmp.png')
  text = '\n'.join([bounds[i][1] for i in range(len(bounds))])
  return text
