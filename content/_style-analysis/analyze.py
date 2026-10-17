import json, csv, re
from collections import Counter, defaultdict

# ---------- Load ----------
posts_meta = {}  # (acct, id) -> row dict
with open('all-posts.csv') as f:
    r = csv.DictReader(f)
    for row in r:
        posts_meta[(row['acct'], row['id'])] = row

slides_by_post = defaultdict(list)  # (acct, post) -> [ (slide, text) ]
with open('slide-text.jsonl') as f:
    for line in f:
        d = json.loads(line)
        slides_by_post[(d['acct'], d['post'])].append((d['slide'], d['text']))

# full text per post
post_text = {}
for k, slides in slides_by_post.items():
    slides.sort(key=lambda x: x[0])
    post_text[k] = "\n".join(t for _, t in slides)

joined = []  # merged records
missing_meta = 0
for k, text in post_text.items():
    meta = posts_meta.get(k)
    if meta is None:
        missing_meta += 1
        continue
    joined.append({
        'acct': k[0], 'post': k[1], 'text': text,
        'views': int(meta['plays'] or 0),
        'likes': int(meta['likes'] or 0),
        'saves': int(meta['saves'] or 0),
        'desc': meta['desc'],
    })

print(f"Joined posts: {len(joined)} (missing meta for {missing_meta})")
print(f"Total slide-text posts: {len(post_text)}, total CSV posts: {len(posts_meta)}")
print()

# ---------- Topic taxonomy ----------
TOPICS = {
    'Height/Growth': ['height', 'hgh', r'\bgh\b', 'growth hormone', 'igf-1', 'igf1', 'growth plate',
                       'taller', 'final adult height', r'\bfah\b', 'bone age', 'stature'],
    'Peptides': ['peptide', 'bpc-157', 'bpc157', 'tb-500', 'tb500', 'ghk-cu', 'ghrp', 'cjc-1295',
                 'cjc1295', 'ipamorelin', 'sermorelin', 'mots-c', 'pt-141', 'melanotan'],
    'Steroids/PEDs': ['steroid', 'anabolic', 'sarm', 'testosterone', r'\btrt\b', 'trenbolone', 'tren ',
                       'anavar', r'\bvar\b', 'dianabol', 'winstrol', 'aromatase', 'aas ', r'\baas\b',
                       'gear', 'cycle', 'pct', 'roids'],
    'Nootropics/Cognition': ['nootropic', 'racetam', 'cognit', 'dopamine', 'focus', 'memory', 'adhd',
                              'modafinil', 'choline', 'acetylcholine', r'\bnad\+', 'brain fog', 'gaba'],
    'Looksmaxxing': ['looksmax', 'jawline', r'\bmog\b', 'facial', 'canthal', 'chin', 'hunter eyes',
                      'mewing', 'symmetry'],
    'Hair': ['hair loss', 'hairloss', 'minoxidil', 'finasteride', 'dht', 'dutasteride', 'derma roller',
              'follicle', 'balding', 'hairline'],
    'Skin/Anti-aging': ['collagen', 'retinol', 'skin', 'wrinkle', 'anti-aging', 'antiaging', 'niacinamide'],
    'Sleep/Recovery': ['sleep', 'melatonin', 'recovery', 'circadian'],
    'Diet/Supplements': ['creatine', 'protein', 'vitamin d', 'zinc', 'magnesium', 'supplement', 'diet',
                          'calorie', 'omega-3', 'omega 3'],
}

def classify(text, desc):
    hay = (text + " " + (desc or "")).lower()
    scores = {}
    for topic, kws in TOPICS.items():
        c = 0
        for kw in kws:
            c += len(re.findall(kw, hay))
        if c:
            scores[topic] = c
    if not scores:
        return 'Other/Uncategorized'
    return max(scores, key=scores.get)

for rec in joined:
    rec['topic'] = classify(rec['text'], rec['desc'])

# ---------- Q1: Topics by views, per account and overall ----------
print("="*70)
print("Q1: TOPICS BY VIEWS")
print("="*70)

overall_topic_views = Counter()
overall_topic_count = Counter()
for rec in joined:
    overall_topic_views[rec['topic']] += rec['views']
    overall_topic_count[rec['topic']] += 1

print("\n-- Overall (all 14 accounts) --")
print(f"{'Topic':<24}{'Posts':>7}{'Total Views':>14}{'Avg Views':>12}")
for topic, v in overall_topic_views.most_common():
    n = overall_topic_count[topic]
    print(f"{topic:<24}{n:>7}{v:>14,}{v//n:>12,}")

acct_topic_views = defaultdict(Counter)
acct_topic_count = defaultdict(Counter)
for rec in joined:
    acct_topic_views[rec['acct']][rec['topic']] += rec['views']
    acct_topic_count[rec['acct']][rec['topic']] += 1

print("\n-- Per account: top topic by total views --")
for acct in sorted(acct_topic_views, key=lambda a: -sum(acct_topic_views[a].values())):
    tv = acct_topic_views[acct]
    total = sum(tv.values())
    top = tv.most_common(3)
    top_str = ", ".join(f"{t} ({v:,})" for t, v in top)
    print(f"{acct:<24} total={total:>10,}  top: {top_str}")

# ---------- Q3: Most-cited studies ----------
print()
print("="*70)
print("Q3: MOST-CITED STUDIES")
print("="*70)

# Pattern: Capitalized surname (1-2 words) followed by a year 19xx/20xx, optionally "et al"
cite_re = re.compile(r'\b([A-Z][a-zA-Z\-]{2,20}(?:\s+et\s*al\.?)?)\s*[,\(]?\s*((?:19|20)\d{2})\b')

citations = Counter()
citation_accounts = defaultdict(set)
citation_posts = defaultdict(set)
for rec in joined:
    seen_in_post = set()
    for m in cite_re.finditer(rec['text']):
        name, year = m.group(1).strip(), m.group(2)
        # filter out obvious false positives (common words that got capitalized by OCR)
        if name.lower() in {'the', 'this', 'a', 'and', 'for', 'in', 'if', 'no', 'not', 'day', 'days'}:
            continue
        key = f"{name} {year}"
        seen_in_post.add(key)
    for key in seen_in_post:
        citations[key] += 1
        citation_accounts[key].add(rec['acct'])
        citation_posts[key].add(rec['post'])

print(f"\n{'Study citation':<30}{'# posts':>9}{'# accounts':>12}")
for key, n in citations.most_common(25):
    print(f"{key:<30}{n:>9}{len(citation_accounts[key]):>12}")

# ---------- Q2: Recurring claims + evidence ----------
print()
print("="*70)
print("Q2: RECURRING CLAIMS (entity + claim-verb pairs) & EVIDENCE RATE")
print("="*70)

CLAIM_VERBS = ['increase', 'decrease', 'boost', 'reduce', 'improve', 'cause', 'block',
               'suppress', 'stimulate', 'activate', 'inhibit', 'lower', 'raise', 'accelerate',
               'stunt', 'prevent', 'trigger', 'enhance', 'upregulate', 'downregulate',
               'promote', 'delay', 'close', 'accelerate', 'shut down', 'shrink']

EVIDENCE_MARKERS = re.compile(
    r'\bstudy|studies|trial|research|journal|published|showed|shown|demonstrat|meta-analysis|'
    r'\bn\s*=\s*\d+|volunteers|participants|patients|subjects\b|' + cite_re.pattern,
    re.IGNORECASE)

# curated entity vocabulary (substances / hormones / biological targets referenced in this niche)
ENTITIES = [
    'gh', 'hgh', 'igf-1', 'igf1', 'igf-i', 'growth hormone', 'growth plate', 'growth plates',
    'testosterone', 'estrogen', 'estradiol', 'dht', 'cortisol', 'insulin', 'leptin', 'ghrelin',
    'thyroid', r't3\b', r't4\b', 'pth', 'pthrp', 'fsh', 'lh', 'prolactin', 'melatonin',
    'osteoblast', 'osteoclast', 'osteoblasts', 'osteoclasts', 'cartilage', 'chondrocyte',
    'runx2', 'rankl', 'opg', 'bone density', 'bone age', 'final adult height',
    'minoxidil', 'finasteride', 'dutasteride', 'hair follicle', 'hair growth', 'balding',
    'creatine', 'collagen', 'retinol', 'vitamin d', 'zinc', 'magnesium',
    'dopamine', 'serotonin', 'gaba', 'acetylcholine', 'norepinephrine', 'ampk', 'camp', 'mtor',
    'bpc-157', 'bpc157', 'tb-500', 'tb500', 'ghk-cu', 'sarms?', 'anavar', 'trenbolone',
    'appetite', 'metabolism', 'fat loss', 'muscle mass', 'bone mineral density', 'jawline',
]
entity_pattern = re.compile(r'\b(' + '|'.join(ENTITIES) + r')\b', re.IGNORECASE)

def sentences(text):
    flat = re.sub(r'\s+', ' ', text)
    parts = re.split(r'(?<=[.!?])\s+', flat)
    return [p.strip() for p in parts if len(p.strip()) > 8]

verb_pattern = re.compile(r'\b(' + '|'.join(CLAIM_VERBS) + r')(s|es|d|ed)?\b', re.IGNORECASE)

claim_counter = Counter()
claim_accounts = defaultdict(set)
claim_examples = defaultdict(list)
claim_has_evidence = Counter()

for rec in joined:
    for sent in sentences(rec['text']):
        vm = verb_pattern.search(sent)
        if not vm:
            continue
        verb = vm.group(1).lower()
        # look for an entity within the sentence (either side of the verb)
        em = entity_pattern.search(sent)
        if not em:
            continue
        entity = re.sub(r'\s+', ' ', em.group(1).lower())
        # normalize a few aliases
        entity = {'igf1': 'igf-1', 'igf-i': 'igf-1', 'hgh': 'gh', 'bpc157': 'bpc-157',
                  'tb500': 'tb-500', 'osteoblasts': 'osteoblast', 'osteoclasts': 'osteoclast'}.get(entity, entity)
        key = (entity, verb)
        claim_counter[key] += 1
        claim_accounts[key].add(rec['acct'])
        if len(claim_examples[key]) < 3:
            claim_examples[key].append(sent[:150])
        if EVIDENCE_MARKERS.search(sent):
            claim_has_evidence[key] += 1

recurring = [(k, c) for k, c in claim_counter.items() if len(claim_accounts[k]) >= 2]
recurring.sort(key=lambda kc: (-len(claim_accounts[kc[0]]), -kc[1]))

print(f"\nDistinct entity+verb claims total: {len(claim_counter)}")
print(f"Claims appearing across >=2 accounts: {len(recurring)}")
print(f"\n{'Entity':<22}{'Verb':<14}{'#accts':>7}{'#mentions':>10}{'w/evidence':>11}")
for key, c in recurring[:30]:
    ent, verb = key
    print(f"{ent:<22}{verb:<14}{len(claim_accounts[key]):>7}{c:>10}{claim_has_evidence[key]:>11}")

print("\nExamples for top 10 recurring claims:")
for key, c in recurring[:10]:
    ent, verb = key
    print(f"\n- [{ent} {verb}s] ({len(claim_accounts[key])} accounts, {c} mentions, {claim_has_evidence[key]} with study/data evidence markers)")
    for ex in claim_examples[key]:
        print(f"    \"{ex}\"")

# overall evidence rate
total_claims = sum(claim_counter.values())
total_evidenced = sum(claim_has_evidence.values())
print(f"\nOverall: {total_evidenced}/{total_claims} claim-mentions ({100*total_evidenced/total_claims:.0f}%) co-occur with a study/data/citation marker in the same sentence.")

# ---------- Q4: Whitespace topics ----------
print()
print("="*70)
print("Q4: WHITESPACE - topic x account coverage matrix")
print("="*70)

all_accounts = sorted(set(rec['acct'] for rec in joined))
topic_by_acct_set = defaultdict(set)
for rec in joined:
    topic_by_acct_set[rec['topic']].add(rec['acct'])

print(f"\n{'Topic':<24}" + "".join(f"{a[:10]:>11}" for a in all_accounts))
for topic in list(TOPICS.keys()) + ['Other/Uncategorized']:
    covering = topic_by_acct_set.get(topic, set())
    row = "".join(f"{'X' if a in covering else '.':>11}" for a in all_accounts)
    print(f"{topic:<24}{row}   ({len(covering)}/{len(all_accounts)} accounts)")

print("\nTopics covered by only 1-2 accounts (potential whitespace/niche):")
for topic in TOPICS:
    covering = topic_by_acct_set.get(topic, set())
    if 0 < len(covering) <= 2:
        print(f"  {topic}: only {sorted(covering)}")
