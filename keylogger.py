# import needed modules
import os
from datetime import datetime
import time
import pyxhook
import csv

def main():
    username = input("Enter Your Name: ")
    print("\nHello " + username + "! Please enter some text and when you are done press ESC to create the output csv file. To terminate the program you can press CTRL+C.\n")

    # Specify the name of the files

    date_time = datetime.now().strftime("%d.%m.%Y-%H:%M")
    log_file = f'{os.getcwd()}/{username + "-" + date_time}.log'
    csv_file = f'{os.getcwd()}/keylogger_outputs/{username + "-" + date_time}.csv'

    eventList = []
    global capsLockOn
    capsLockOn = False
    # The function to be called when a key is pressed
    def OnKeyPress(event):
        global capsLockOn
        with open(log_file, "a") as f:  # Open a file as f with Append (a) mode
            if event.Key == 'Escape':
                with open(csv_file,'a',newline='\n') as f:
                    writer = csv.writer(f)
                    headers = ["User", "Key", "Event", "TimeInMillis"]
                    writer.writerow(headers)
                    writer.writerows(eventList)
                f.close()
            elif event.Key == 'Return':
                f.write(f"RETURN down {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "RETURN", "down", int(time.time() * 1000)))
            elif event.Key == "Control_L":
                f.write(f"CONTROL_LEFT down {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "CONTROL_LEFT", "down", int(time.time() * 1000)))
            elif event.Key == "Shift_L":
                f.write(f"SHIFT_LEFT down {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "SHIFT_LEFT", "down", int(time.time() * 1000)))
            elif event.Key == "Shift_R":
                f.write(f"SHIFT_RIGHT down {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "SHIFT_RIGHT", "down", int(time.time() * 1000)))
            elif event.Key == "Caps_Lock":
                capsLockOn = not capsLockOn
                f.write(f"CAPS_LOCK down {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "CAPS_LOCK", "down", int(time.time() * 1000)))
            elif event.Key == "space":
                f.write(f"SPACE down {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "SPACE", "down", int(time.time() * 1000)))
            elif event.Key == "BackSpace":
                f.write(f"BACK_SPACE down {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "BACK_SPACE", "down", int(time.time() * 1000)))
            elif event.Key == "Alt_L":
                f.write(f"ALT_LEFT down {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "ALT_LEFT", "down", int(time.time() * 1000)))
            elif event.Key == "Tab":
                f.write(f"TAB down {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "TAB", "down", int(time.time() * 1000)))
            else:
                if capsLockOn:
                    f.write(f"{chr(event.Ascii).upper()} down {datetime.now().strftime('%H:%M:%S.%f')}\n") # Write to the file and convert ascii to readable characters
                    eventList.append((username, chr(event.Ascii).upper(), "down", int(time.time() * 1000)))
                else:
                    f.write(f"{chr(event.Ascii)} down {datetime.now().strftime('%H:%M:%S.%f')}\n") # Write to the file and convert ascii to readable characters
                    eventList.append((username, chr(event.Ascii), "down", int(time.time() * 1000)))

    # The function to be called when a key is released
    def OnKeyRelease(event):
        with open(log_file, "a") as f:  # Open a file as f with Append (a) mode
            if event.Key == 'Escape':
                pass
            elif event.Key == 'Return':
                if len(eventList) != 0:
                    f.write(f"RETURN up {datetime.now().strftime('%H:%M:%S.%f')}\n")
                    eventList.append((username, "RETURN", "up", int(time.time() * 1000)))
            elif event.Key == "Control_L":
                f.write(f"CONTROL_LEFT up {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "CONTROL_LEFT", "up", int(time.time() * 1000)))
            elif event.Key == "Shift_L":
                f.write(f"SHIFT_LEFT up {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "SHIFT_LEFT", "up", int(time.time() * 1000)))
            elif event.Key == "Shift_R":
                f.write(f"SHIFT_RIGHT up {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "SHIFT_RIGHT", "up", int(time.time() * 1000)))
            elif event.Key == "Caps_Lock":
                f.write(f"CAPS_LOCK up {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "CAPS_LOCK", "up", int(time.time() * 1000)))
            elif event.Key == "space":
                f.write(f"SPACE up {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "SPACE", "up", int(time.time() * 1000)))
            elif event.Key == "BackSpace":
                f.write(f"BACK_SPACE up {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "BACK_SPACE", "up", int(time.time() * 1000)))
            elif event.Key == "Alt_L":
                f.write(f"ALT_LEFT up {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "ALT_LEFT", "up", int(time.time() * 1000)))
            elif event.Key == "Tab":
                f.write(f"TAB up {datetime.now().strftime('%H:%M:%S.%f')}\n")
                eventList.append((username, "TAB", "up", int(time.time() * 1000)))
            else:
                if capsLockOn:
                    f.write(f"{chr(event.Ascii).upper()} up {datetime.now().strftime('%H:%M:%S.%f')}\n")
                    eventList.append((username, chr(event.Ascii).upper(), "up", int(time.time() * 1000)))
                else:
                    f.write(f"{chr(event.Ascii)} up {datetime.now().strftime('%H:%M:%S.%f')}\n")
                    eventList.append((username, chr(event.Ascii), "up", int(time.time() * 1000)))
        
    # Create a hook manager object
    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = OnKeyPress
    new_hook.KeyUp = OnKeyRelease

    new_hook.HookKeyboard()  # set the hook

    try:
        new_hook.start()  # start the hook
    except KeyboardInterrupt:
        # User cancelled from command line so close the listener
        new_hook.cancel()
    except Exception as ex:
        # Write exceptions to the log file, for analysis later.
        msg = f"Error while catching events:\n  {ex}"
        pyxhook.print_err(msg)
        with open(log_file, "a") as f:
            f.write(f"\n{msg}")

if __name__ == "__main__":
    main()
