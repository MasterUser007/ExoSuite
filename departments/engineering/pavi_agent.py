import os, sys, subprocess, requests, logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

GITHUB_TOKEN = os.environ.get('PAVI_GITHUB_TOKEN')
WEBHOOK_URL = os.environ.get('PAVI_WEBHOOK_URL')
DEPT = 'engineering'

logging.basicConfig(filename=f'pavi_{DEPT}.log', level=logging.INFO)

def notify(msg, kind='info'):
    print(f"[PAVI/{DEPT}] {msg}")
    logging.info(msg)
    if WEBHOOK_URL:
        try:
            requests.post(WEBHOOK_URL, json={'content': f"[{DEPT}] {msg}"})
        except Exception as e:
            print("Notification failed: ", e)

class ChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if not event.is_directory:
            try:
                subprocess.run(['python', f'departments/{DEPT}/validate.py'], check=True)
                notify('Validation OK')
            except subprocess.CalledProcessError as e:
                notify(f'Validation failed: {e}', 'error')

if __name__ == '__main__':
    notify(f"{DEPT} agent started")
    observer = Observer()
    observer.schedule(ChangeHandler(), f'departments/{DEPT}', recursive=True)
    observer.start()
    try:
        while True: pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()