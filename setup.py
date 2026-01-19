import os

if "config.py" not in os.listdir("."):
    KEY_PISTE = input("Insert PISTE API KEY here :\n")
    with open("config.py", "w") as f:
        f.write(f'KEY_PISTE = "{KEY_PISTE}"')