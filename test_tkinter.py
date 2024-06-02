import sys
import os

print("Python Path:")
for path in sys.path:
    print(path)

print("\nLD_LIBRARY_PATH:")
print(os.environ.get('LD_LIBRARY_PATH', 'Not Set'))

print("\nTK_LIBRARY:")
print(os.environ.get('TK_LIBRARY', 'Not Set'))

print("\nLoaded shared libraries:")
os.system('otool -L $(which python)')

print("\nAttempting to import Tkinter...")

try:
    import _tkinter
    print("_tkinter module found.")
    print("_tkinter module location:", _tkinter.__file__)
except ImportError as e:
    print(f"ImportError: {e}")
    print("Environment variables:")
    print(f"LD_LIBRARY_PATH: {os.environ.get('LD_LIBRARY_PATH')}")
    print(f"TK_LIBRARY: {os.environ.get('TK_LIBRARY')}")
    print("Python paths:")
    for path in sys.path:
        print(path)
    sys.exit(1)

print("\nTkinter Test")

import tkinter as tk

root = tk.Tk()
root.title("Tkinter Test")
label = tk.Label(root, text="Tkinter is working! \nGo Dream Team!")
label.pack()
root.mainloop()
