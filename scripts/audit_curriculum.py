"""Read-only curriculum contract checks; not learner mastery evidence."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
def check(ok, message):
    if not ok:
        errors.append(message)

expected = [4, 2.5, 2.5, 2.5, 3, 2.5, 2]
expected_dates = ['2026-09-05', '2026-09-07', '2026-09-08', '2026-09-09', '2026-09-10', '2026-09-11', '2026-09-12']
total = 0
for day, hours in enumerate(expected, 1):
    path = ROOT / f'03-weeks/week-001/DAY_{day:02}.md'
    text = path.read_text()
    match = re.search(r'^estimated_hours: ([0-9.]+)$', text, re.M)
    declared = float(match[1]) if match else -1
    blocks = [int(x) for x in re.findall(r'^## \d+\. .* — (\d+) dakika$', text, re.M)]
    check(declared == hours, f'{path.name}: wrong declared hours')
    check(sum(blocks) == declared * 60, f'{path.name}: internal minutes {sum(blocks)} != {declared * 60}')
    check(f'date: {expected_dates[day-1]}' in text, f'{path.name}: planned date drift')
    check('## Today' in text and 'UNKNOWN' in text and 'Öğretmen önce' in text, f'{path.name}: missing teaching entry')
    check('## REQUIRED evidence' in text and '## OPTIONAL / STRETCH / REFERENCE' in text, f'{path.name}: scope classification missing')
    total += declared
    print(f'{path.name}: {sum(blocks)} minutes / {declared:g} hours')
check(total == 19, f'Week total {total} != 19')
week = (ROOT / '03-weeks/week-001/WEEK_PLAN.md').read_text()
check('required_hours: 19' in week, 'Week header hours')
for name, field in [('ASSESSMENT.md', 'assessment_date'), ('RETROSPECTIVE.md', 'retrospective_date')]:
    check(f'{field}: 2026-09-12' in (ROOT / '03-weeks/week-001' / name).read_text(), f'{name}: stale date')

# Check every Markdown relative link, excluding code fences and external schemes.
mdfiles = [p for p in ROOT.rglob('*.md') if not any(part.startswith('.') for part in p.relative_to(ROOT).parts)]
for p in mdfiles:
    text = re.sub(r'```.*?```', '', p.read_text(), flags=re.S)
    for dest in re.findall(r'\]\(([^)]+)\)', text):
        dest = dest.split('#', 1)[0].strip('<>')
        if not dest or re.match(r'[a-zA-Z]+:', dest):
            continue
        check((p.parent / dest).exists(), f'{p.relative_to(ROOT)}: broken local link {dest}')

rules = [
    'Never ask the learner to interpret, predict, debug, or use a concept, command, API, tool, flag, protocol, or abstraction that has not first been taught or explicitly established as prior knowledge.',
    'Socratic questioning is a reinforcement technique, not a substitute for instruction.',
    'For unknown concepts the correct order is Teach → Demonstrate → Predict → Practice → Observe → Explain → Review.'
]
for name in ['AGENTS.md', '00-governance/CODEX_TEACHER_PROTOCOL.md', '00-governance/LEARNING_PROTOCOL.md']:
    text = (ROOT / name).read_text()
    for rule in rules:
        check(rule in text, f'{name}: missing canonical teaching rule')
# No old calendar/effort assertions in active curriculum; historical evidence excluded.
for p in [ROOT / 'README.md', *list((ROOT/'00-governance').glob('*.md')), *list((ROOT/'02-phases').glob('*.md')), *list((ROOT/'03-weeks/week-001').glob('*.md'))]:
    check(not re.search(r'36\s*(?:hafta|weeks)|29 saat|25[–-]30|2026-08-10|2026-09-01', p.read_text(), re.I), f'{p.relative_to(ROOT)}: stale plan')

# Validate YAML if available; do not silently claim parsing if dependency is absent.
try:
    import yaml
except ImportError:
    errors.append('PyYAML unavailable: YAML structural validation not performed')
else:
    skills = yaml.safe_load((ROOT/'01-skill-matrix/skill-matrix.yaml').read_text())
    check(skills['scale']['completion_threshold'] == 4, 'Mastery threshold drift')
    for group, entries in skills['skills'].items():
        for name, item in entries.items():
            score = item['score']
            check(score is None or (0 <= score <= 5 and bool(item['evidence'])), f'{group}.{name}: score without evidence')
    data = yaml.safe_load((ROOT/'01-skill-matrix/concept-state.yaml').read_text())
    for concept, item in data['concepts'].items():
        check(item['knowledge_state'] in data['allowed_states'], f'{concept}: invalid state')
        source = item['source']
        if source:
            check((ROOT/source).exists(), f'{concept}: missing state source')
        if item['knowledge_state'] in ['PROVEN', 'MASTERED']:
            check(bool(source) and bool(item.get('independent_evidence')), f'{concept}: independent proof missing')
        if item['knowledge_state'] == 'MASTERED':
            check(item.get('score', -1) >= 4, f'{concept}: mastery score missing')

if errors:
    print('\nFAIL:\n' + '\n'.join(errors))
    sys.exit(1)
print(f'PASS: 7 day budgets, 19 hours, dates, local links, rules, active stale-text scan, YAML/state/score evidence contracts ({len(mdfiles)} Markdown files).')
print('Teaching behavior needs the separate human-readable simulations in TEACHING_ACCEPTANCE.md; these checks cannot prove future tutor behavior.')
