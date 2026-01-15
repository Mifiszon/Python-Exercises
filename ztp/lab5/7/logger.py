from datetime import datetime

def log(type, message, filename="log.txt"):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{time}] [{type.upper()}] {message}\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(line)