import os
import sys

def extract_song_list(folder_path, output_file="songlist.txt"):
    entries = []
    for filename in sorted(os.listdir(folder_path)):
        if not filename.endswith(".txt"):
            continue
        filepath = os.path.join(folder_path, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
        if first_line:
            entries.append(first_line)

    with open(output_file, "w", encoding="utf-8") as out:
        for line in entries:
            out.write(line + "\n")

    print(f"Wrote {len(entries)} entries to {output_file}")

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    extract_song_list(folder)