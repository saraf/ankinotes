import os
import shutil
import yaml
from datetime import datetime
from pathlib import Path
from slugify import slugify
from collections import defaultdict

NOTES_SRC = "notable_notes"  # folder where Notable markdown files live
POSTS_DST = "_posts"
TAGS_DST = "tags"
TAG_GROUP_FILE = "_data/tag_groups.yml"

os.makedirs(POSTS_DST, exist_ok=True)
os.makedirs(TAGS_DST, exist_ok=True)
os.makedirs("_data", exist_ok=True)

seen_tags = set()
created_tag_pages = []

def convert_note_to_post(src_path):
    with open(src_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # parse metadata
    if lines[0].strip() == "---":
        end = lines[1:].index("---
") + 2
        frontmatter = "".join(lines[:end])
        body = "".join(lines[end:])
        meta = yaml.safe_load(frontmatter)
    else:
        return

    title = meta.get("title") or "Untitled"
    slug = slugify(title)
    created = meta.get("created", datetime.now().isoformat())
    date = datetime.fromisoformat(created.replace("Z", "+00:00"))
    tags = meta.get("tags", [])

    filename = f"{date.strftime('%Y-%m-%d')}-{slug}.md"
    dst_path = os.path.join(POSTS_DST, filename)

    # Rebuild frontmatter for Jekyll
    new_meta = {
        "layout": "post",
        "title": title,
        "date": date.strftime("%Y-%m-%d %H:%M:%S"),
        "tags": tags
    }

    with open(dst_path, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(new_meta, f)
        f.write("---\n\n")
        f.write(body)

    for tag in tags:
        seen_tags.add(tag)

def generate_tag_pages():
    for tag in seen_tags:
        slug = slugify(tag)
        tag_path = os.path.join(TAGS_DST, f"{slug}.md")
        if not os.path.exists(tag_path):
            with open(tag_path, "w", encoding="utf-8") as f:
                f.write(f"""---
layout: tag
title: Tag: {tag}
tag: {tag}
permalink: /tags/{slug}/
---\n""")
            created_tag_pages.append(tag)

def scan_notes():
    for file in Path(NOTES_SRC).glob("*.md"):
        convert_note_to_post(file)

scan_notes()
generate_tag_pages()

if created_tag_pages:
    print("\n✅ New tags detected and tag pages generated:")
    for tag in created_tag_pages:
        print(f"  - {tag}")
else:
    print("✅ No new tags found.")

print(f"📂 To manage tag groups, edit: {TAG_GROUP_FILE}")
