# by Thomas Brunner (rennurb3000)
#!/usr/bin/python3
from PIL import Image 
import sys

try:
  albedo = Image.open(sys.argv[1]).convert('RGBA')
  rough = Image.open(sys.argv[2]).convert('L')
  albedo.putalpha(rough)
  albedo.save(sys.argv[3],"PNG",optimize=True)
except:
  print("usage : ./urt albedo.png rough.png out.png")
