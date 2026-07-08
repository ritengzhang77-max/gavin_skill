#!/usr/bin/env python3
"""Lightweight public-release scan for the staged Gavin Hermes workflow repo.

This is a guardrail, not a replacement for manual review.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {'.git', '__pycache__'}
TEXT_EXTS = {'.md', '.txt', '.json', '.yaml', '.yml', '.py', '.sh', '.toml'}
PATTERNS = {
    'possible_api_key': re.compile(r'(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*["\']?[^\s"\']{12,}'),
    'private_key': re.compile(r'-----BEGIN [A-Z ]*PRIVATE KEY-----'),
    'email': re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', re.I),
    'absolute_home_path': re.compile(r'/home/[A-Za-z0-9._-]+/'),
    'discord_id_like': re.compile(r'\b\d{17,20}\b'),
}

def iter_files():
    for p in ROOT.rglob('*'):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if p.is_file() and p.suffix.lower() in TEXT_EXTS:
            yield p

def main() -> int:
    findings = []
    for p in iter_files():
        text = p.read_text(errors='ignore')
        for name, rx in PATTERNS.items():
            for m in rx.finditer(text):
                line = text.count('\n', 0, m.start()) + 1
                snippet = text[m.start():m.end()].replace('\n', ' ')[:160]
                findings.append((str(p.relative_to(ROOT)), line, name, snippet))
    if not findings:
        print('No scanner findings. Manual review still required.')
        return 0
    print('Scanner findings:')
    for rel, line, name, snippet in findings[:500]:
        print(f'{rel}:{line}: {name}: {snippet}')
    if len(findings) > 500:
        print(f'... truncated {len(findings)-500} more findings')
    print('\nReview these before public push. Some local paths/emails may be intentional docs examples.')
    return 1

if __name__ == '__main__':
    raise SystemExit(main())
