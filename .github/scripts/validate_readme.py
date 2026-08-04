import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

amp = '&'
lt = '<'
gt = '>'

# Check 1: No bare & in src/href/srcset attributes
pattern = r'(?:src|href|srcset)="[^"]*' + amp + '(?!amp;)[^"]*"'
bare_amp = re.findall(pattern, content)
print(f'Bare & in HTML attrs: {len(bare_amp)} (should be 0)')

# Check 2: No raw > inside src attributes
raw_gt = re.findall(r'src="[^">]*>[^"]*"', content)
print(f'Raw > in src attrs: {len(raw_gt)} (should be 0)')

# Check 3: Markers still intact
tip_start = 'TECH-TIP-START' in content
tip_end = 'TECH-TIP-END' in content
print(f'TECH-TIP markers: {tip_start and tip_end}')

# Check 4: Header has teal name
teal = 'fontColor=00C9A7' in content
print(f'Teal name (fontColor=00C9A7): {teal}')

# Check 5: Black bg
black_bg = 'color=0:000000' in content
print(f'Black bg header: {black_bg}')

# Check 6: Dark footer
dark_footer = 'section=footer' in content and '0A0A1A' in content
print(f'Dark footer: {dark_footer}')

# Check 7: Typing SVG > encoded
typing_ok = '%3E+Manual+Ops' in content
print(f'Typing SVG > encoded: {typing_ok}')

all_ok = len(bare_amp) == 0 and len(raw_gt) == 0 and tip_start and tip_end and teal and black_bg and dark_footer and typing_ok
print()
print('ALL CHECKS PASSED - README is XML clean!' if all_ok else 'SOME CHECKS FAILED')
if bare_amp:
    print('Remaining issues:', bare_amp[:3])
