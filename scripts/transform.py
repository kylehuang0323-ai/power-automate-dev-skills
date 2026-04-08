import re

SRC = r'C:\Users\v-lexinhuang\OneDrive - Microsoft\The Garage - Beijing, Greater China-GCR Garage Staff - Lab Manager\CLI file\1.Tool borrow\POWER_AUTOMATE_SKILLS.md'
DST = r'C:\Users\v-lexinhuang\power-automate-dev-skills\README.md'

with open(SRC, 'r', encoding='utf-8') as f:
    src = f.read()

# ---- Remove entire Garage-specific sections ----
# Remove Appendix A (Tool Borrow architecture diagram)
a = src.find('## \u9644\u5f55 A: \u5de5\u5177\u501f\u7528\u7cfb\u7edf Flow')
b = src.find('## \u9644\u5f55 B: \u5feb\u901f\u53c2\u8003\u5361')
if a != -1 and b != -1:
    src = src[:a] + src[b:]

# Remove section 12.6 (tool-borrow DLP compliance)
a = src.find('### 12.6 \u5de5\u5177\u501f\u7528\u7cfb\u7edf DLP')
b = src.find('### 12.7 DLP \u7b56\u7565\u7ba1\u7406')
if a != -1 and b != -1:
    src = src[:a] + src[b:]

# Renumber DLP sub-sections
src = src.replace('### 12.7 DLP', '### 12.6 DLP')
src = src.replace('### 12.8 DLP', '### 12.7 DLP')
src = src.replace('### 12.9 Advanced', '### 12.8 Advanced')

# ---- Process line by line ----
lines = src.split('\n')
out = []

for i, line in enumerate(lines):
    # Skip Chinese-only title line
    if i == 0:
        continue
    if '\u9002\u7528\u4e8e Garage' in line or 'For Garage Beijing' in line:
        continue

    # Bilingual headers: ## N. Chinese / English → ## N. English
    m = re.match(r'^(#{1,4})\s+(.+?)\s*/\s*(.+)$', line)
    if m and re.search(r'[\u4e00-\u9fff]', m.group(2)):
        line = f'{m.group(1)} {m.group(3).strip()}'

    stripped = line.strip()

    # Always keep blank lines, code fences, table separators
    if stripped == '' or stripped.startswith('```') or stripped == '---' or re.match(r'^\|[-\s|:]+\|$', stripped):
        out.append(line)
        continue

    # Handle lines with Chinese
    if re.search(r'[\u4e00-\u9fff]', line):
        # Table rows
        if '|' in line:
            parts = line.split('|')
            new_parts = []
            for p in parts:
                ps = p.strip()
                m2 = re.match(r'(.+?)\s*/\s*(.+)', ps)
                if m2 and re.search(r'[\u4e00-\u9fff]', m2.group(1)):
                    new_parts.append(f' {m2.group(2).strip()} ')
                elif re.search(r'[\u4e00-\u9fff]', ps):
                    en = re.sub(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef\uff0c\u3002\u3001\uff1b\uff1a\u201c\u201d\uff08\uff09\u3010\u3011]+\s*', '', ps).strip()
                    new_parts.append(f' {en} ' if en and len(en) > 1 else p)
                else:
                    new_parts.append(p)
            line = '|'.join(new_parts)
            if line.strip() and line.strip() != '|':
                out.append(line)
            continue

        # Compute Chinese ratio
        cn_chars = len(re.findall(r'[\u4e00-\u9fff]', stripped))
        total = len(stripped)

        # Skip lines that are >60% Chinese
        if total > 0 and cn_chars / total > 0.55:
            continue

        # For mixed lines, remove Chinese portions
        line = re.sub(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef\uff0c\u3002\u3001\uff1b\uff1a\u201c\u201d\uff08\uff09\u3010\u3011]+', '', line)
        line = re.sub(r'\s*/\s*$', '', line)
        line = re.sub(r'\s{3,}', '  ', line)

        if not line.strip():
            continue

    out.append(line)

result = '\n'.join(out)

# ---- Replace Garage-specific terms ----
replacements = [
    ('TheGarageBeijing', 'ContosoTeam'),
    ('Garage Beijing', 'Contoso'),
    ('Garage-Dev', 'Project-Dev'),
    ('Garage-Prod', 'Project-Prod'),
    ('v-lexinhuang@microsoft.com', 'admin@contoso.com'),
    ('v-lexinhuang', 'admin'),
    ('Tool Inventory', 'Asset Inventory'),
    ('Tool Requests', 'Service Requests'),
    ('ToolBorrow_CreateRequest', 'AssetMgmt_CreateRequest'),
    ('ToolBorrow_RejectedRollback', 'AssetMgmt_RejectedRollback'),
    ('ToolBorrow_ReturnedRollback', 'AssetMgmt_ReturnedRollback'),
    ('ToolBorrow_Approval', 'AssetMgmt_Approval'),
    ('ToolBorrow_', 'AssetMgmt_'),
    ('ToolBorrow', 'AssetMgmt'),
    ('Tool borrow', 'Asset management'),
    ('tool borrow', 'asset management'),
    ('Tool Borrow', 'Asset Management'),
    ('ToolId', 'AssetId'),
    ('ToolName', 'AssetName'),
    ('https://microsoft.sharepoint.com/teams/TheGarageBeijing', 'https://contoso.sharepoint.com/teams/ContosoTeam'),
]
for old, new in replacements:
    result = result.replace(old, new)

# ---- Rename appendices ----
result = result.replace('## \u9644\u5f55 B: \u5feb\u901f\u53c2\u8003\u5361 / Appendix B: Quick Reference Card', '## Appendix A: Quick Reference Card')
result = result.replace('## \u9644\u5f55 C: \u5b9e\u6218\u98df\u8c31 / Appendix C: Cookbook Recipes', '## Appendix B: Cookbook Recipes')

# ---- Add GitHub header ----
header = """# \u26a1 Power Automate Developer Skills Reference

> A comprehensive, expert-level Power Automate skills reference \u2014 from fundamentals to enterprise architecture patterns.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

"""
result = header + result

# ---- Fix version/footer ----
result = result.replace('v3.0', 'v1.0')
result = re.sub(r'> \U0001f4c5 .*?\n', '', result)
result = re.sub(r'> \u270f\ufe0f .*', '> \u270f\ufe0f Maintainer: kylehuang0323-ai', result)

# ---- Remove excessive blank lines ----
result = re.sub(r'\n{3,}', '\n\n', result)

# ---- Final stray Chinese cleanup ----
final_lines = result.split('\n')
clean = []
for line in final_lines:
    s = line.strip()
    if s and re.search(r'[\u4e00-\u9fff]', s):
        cn = len(re.findall(r'[\u4e00-\u9fff]', s))
        if cn / len(s) > 0.4:
            continue
        line = re.sub(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef\uff0c\u3002\u3001\uff1b\uff1a\u201c\u201d\uff08\uff09\u3010\u3011]+\s*/?', '', line)
        line = re.sub(r'\s{2,}', ' ', line).rstrip()
        if not line.strip():
            continue
    clean.append(line)

result = '\n'.join(clean)
result = re.sub(r'\n{3,}', '\n\n', result)

with open(DST, 'w', encoding='utf-8') as f:
    f.write(result)

lines_count = len(result.split('\n'))
cn_remaining = len(re.findall(r'[\u4e00-\u9fff]', result))
print(f'Output: {lines_count} lines, {len(result)} chars')
print(f'Remaining Chinese chars: {cn_remaining}')
print('DONE')
