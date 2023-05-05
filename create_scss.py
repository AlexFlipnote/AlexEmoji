import os

images = "\n".join([
    f"  '{file.split('.')[0].lower()}': '{file}',"
    for file in sorted(os.listdir("./images"), key=lambda x: x.lower())
])


with open("./scss/_emoji-map.scss", "w") as f:
    f.write(f"$emoji-map: (\n{images[:-1]}\n);\n")
