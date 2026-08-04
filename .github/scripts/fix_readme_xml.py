import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix: replace bare & with &amp; ONLY inside HTML tag src/href/srcset attributes
# Strategy: find all src="..." href="..." srcset="..." and replace & -> &amp; inside them

def fix_attr(m):
    attr_name = m.group(1)
    url = m.group(2)
    # Replace bare & (not already &amp;) with &amp;
    url_fixed = re.sub(r'&(?!amp;)', '&amp;', url)
    return f'{attr_name}="{url_fixed}"'

pattern = re.compile(r'(src|href|srcset)="([^"]+)"')
new_content = pattern.sub(fix_attr, content)

changes = sum(1 for a, b in zip(content, new_content) if a != b)
print(f"Characters changed: {changes}")

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done! README.md fixed.")

# Verify: count remaining bare & in HTML tags
remaining = re.findall(r'(src|href)="[^"]*&(?!amp;)[^"]*"', new_content)
print(f"Remaining bare & in attributes: {len(remaining)}")
