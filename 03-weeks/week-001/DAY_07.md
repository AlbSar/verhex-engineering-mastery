---
status: ready
day: 7
date: 2026-09-12
estimated_hours: 2
---

# Day 07 — Değerlendirme, Baseline ve Retrospektif

## Günün amacı
Week 001 boyunca üretilen kanıtları değerlendirip Week 002 için kalibre edilmiş karar vermek.

## 1. Kapalı kaynak mini değerlendirme — 45 dakika
İlk 30 dakika AI, internet ve önceki çözümleri kullanmadan küçük bir kayıt doğrulama fonksiyonu/CLI çekirdeği yaz.

Minimum gereksinimler:
- `customer_id` ve `name` doğrulama
- duplicate tespiti
- bozuk kayıtları ayırma
- deterministic summary
- en az 4 test

Son 15 dakikada kendi çözümünü incele ve refactor notu çıkar. Codex yalnızca bu noktadan sonra reviewer olarak devreye girer.

## 2. Kavramsal teach-back — 25 dakika
Kayıt alarak kısa biçimde açıkla:
1. identity vs equality
2. mutability vs rebinding
3. shallow vs deep copy
4. LEGB / closure
5. process → socket → TCP → HTTP zinciri
6. dependency graph cycle detection

## 3. Kanıt ve puanlama — 30 dakika
Güncelle:
- `01-skill-matrix/baseline-assessment.md`
- `01-skill-matrix/skill-matrix.yaml`
- `03-weeks/week-001/ASSESSMENT.md`

Her puan somut kanıta bağlanır.

## 4. Retrospektif — 15 dakika
`RETROSPECTIVE.md` içinde en kritik yanlış mental model, en güçlü alan, AI bağımlılığı, en değerli hata ve Week 002 önceliğini kaydet.

## 5. Git kapanışı — 5 dakika
```bash
git status
git log --oneline --decorate -10
```

Yerel branch'in remote ile ayrışmışsa körlemesine reset/rebase yapma; önce commit grafiğini incele ve güvenli entegrasyon planı çıkar.

## Teslimatlar
- [ ] Mini değerlendirme + en az 4 test
- [ ] Kavramsal teach-back
- [ ] Baseline assessment
- [ ] Güncellenmiş skill matrix
- [ ] Week assessment
- [ ] Retrospective

## Week 002 geçiş kararı
- `proceed`
- `proceed-with-reinforcement`
- `repeat-critical-sections`

Karar güven hissine değil kanıta göre verilir.
