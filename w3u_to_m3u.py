import json
import sys
import os

def convert(w3u_path, m3u_path):
    try:
        with open(w3u_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON from {w3u_path}: {e}")
        sys.exit(1)

    lines = ["#EXTM3U"]
    items = data.get("items", [])
    for item in items:
        name = item.get("name", "Unknown")
        url = item.get("url", "")
        image = item.get("image", "")
        info = item.get("info", "")

        extinf = f'#EXTINF:-1 tvg-logo="{image}" group-title="{info}",{name}'
        lines.append(extinf)
        lines.append(url)

    with open(m3u_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")
    print(f"Successfully converted '{w3u_path}' to '{m3u_path}' ({len(items)} items processed).")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python w3u_to_m3u.py <input.w3u> [output.m3u]")
        sys.exit(1)

    w3u_file = sys.argv[1]
    if len(sys.argv) >= 3:
        m3u_file = sys.argv[2]
    else:
        m3u_file = os.path.splitext(w3u_file)[0] + ".m3u"

    convert(w3u_file, m3u_file)
