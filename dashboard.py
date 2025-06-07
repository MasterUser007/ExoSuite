import os
from flask import Flask, render_template_string, jsonify
from threading import Thread
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- Configuration ---
LOG_FILES = [
    'pavi_self_diagnosis.log',
    'pavi_verify.log',
    'python_tests.log',
    'pester_tests.log',
    'pavi_build.log',
    'pavi_git.log'
]
REFRESH_INTERVAL = 2000  # ms

# --- Flask App ---
app = Flask(__name__)

# --- In-memory cache for fast log serving ---
log_data = {name: '' for name in LOG_FILES}

class LogUpdateHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for log_file in LOG_FILES:
            if event.src_path.endswith(log_file) and os.path.exists(log_file):
                with open(log_file, encoding='utf-8', errors='ignore') as f:
                    log_data[log_file] = f.read()[-2000:]  # last 2k chars

def start_watchdog():
    observer = Observer()
    observer.schedule(LogUpdateHandler(), '.', recursive=False)
    observer.start()

Thread(target=start_watchdog, daemon=True).start()

@app.route('/')
def dashboard():
    # Template with auto-refresh and colored output
    template = '''
    <!doctype html>
    <html>
    <head>
      <title>Pavi Real-Time Status Dashboard</title>
      <meta http-equiv="refresh" content="600">
      <style>
        body { font-family: monospace; background: #1a1a1a; color: #fff; }
        .section { margin-bottom: 1em; padding: 1em; border-radius: 12px; background: #232323; }
        .title { font-size: 1.2em; color: #61dafb; margin-bottom: 0.5em; }
        pre { background: #121212; color: #cfcfcf; padding: 1em; border-radius: 8px; }
        .ok { color: #00fa9a; }
        .fail { color: #ff5555; }
        .pending { color: #ffc107; }
      </style>
      <script>
        function fetchLogs() {
          fetch('/api/logs').then(resp => resp.json()).then(data => {
            for (const name in data) {
              let elem = document.getElementById(name);
              if (elem) elem.innerHTML = data[name]
                .replace(/(fail|error|critical)/gi, '<span class="fail">$1</span>')
                .replace(/(ok|success|passed)/gi, '<span class="ok">$1</span>')
                .replace(/pending|waiting|skipped/gi, '<span class="pending">$&</span>');
            }
          });
        }
        setInterval(fetchLogs, {{ refresh // 1 }});
        window.onload = fetchLogs;
      </script>
    </head>
    <body>
      <h1>Pavi ExoSuite — Real-Time Status Dashboard</h1>
      {% for file in files %}
      <div class="section">
        <div class="title">{{ file }}</div>
        <pre id="{{ file }}"></pre>
      </div>
      {% endfor %}
    </body>
    </html>
    '''
    return render_template_string(template, files=LOG_FILES, refresh=REFRESH_INTERVAL)

@app.route('/api/logs')
def get_logs():
    # Return log data for AJAX polling
    return jsonify({name: log_data.get(name, "") for name in LOG_FILES})

if __name__ == '__main__':
    # Preload logs if present
    for log_file in LOG_FILES:
        if os.path.exists(log_file):
            with open(log_file, encoding='utf-8', errors='ignore') as f:
                log_data[log_file] = f.read()[-2000:]
    app.run(debug=False, port=5000, host='0.0.0.0')
