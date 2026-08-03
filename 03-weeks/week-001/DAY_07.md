---
status: ready
day: 7
date: 2026-08-10
estimated_hours: 4.5
---

# Day 07 — Değerlendirme, İngilizce Baseline ve Retrospektif

## Günün amacı

Week 001 boyunca üretilen kanıtları değerlendirmek, güçlü ve zayıf zihinsel modelleri görünür kılmak ve Week 002 zorluk seviyesini belirlemek.

## 1. Kapalı kaynak Python değerlendirmesi — 75 dakika

İlk 45 dakika AI, internet ve önceki kodları kullanmadan tamamla.

### Görev

Bir JSON satırları dosyasındaki müşteri kayıtlarını işleyen küçük bir CLI tasarla.

Gereksinimler:

- Dosya yolunu command-line argument olarak alır.
- Her satırı ayrı JSON kayıt olarak okur.
- `customer_id` ve `name` alanlarını doğrular.
- Duplicate `customer_id` kayıtlarını raporlar.
- Hatalı satırları satır numarasıyla döndürür.
- Başarılı/başarısız kayıt sayılarını özetler.
- Beklenen hatalar için custom exception kullanır.
- En az 8 test içerir.

Değerlendirilecekler:

- Problem parçalama
- Type tasarımı
- Mutability kontrolü
- Error boundary
- Deterministic output
- Test kalitesi
- Kodun açıklanabilirliği

Son 30 dakikada kendi çözümünü incele ve refactor notu çıkar.

## 2. Kavramsal sözlü sınav — 30 dakika

Kayıt alarak her başlığı en fazla iki dakikada açıkla:

1. Identity ve equality
2. Mutability ve aliasing
3. Shallow/deep copy
4. Function argument binding
5. LEGB
6. Closure ve late binding
7. Dictionary/set kullanımının performans etkisi
8. Process ile container ilişkisi

## 3. Teknik İngilizce baseline — 60 dakika

### Writing

300–500 kelimelik metni tamamla:

> My Current Engineering Background and the Purpose of the Verhex Mastery Marathon

Metin şu dört bölümü içermeli:

- Current background
- Systems already built
- Technical gaps to close
- Expected business outcomes for Verhex

### Speaking

5 dakika kayıt:

> Why understanding mechanisms matters more than memorizing frameworks.

### Reading

Hafta içinde seçilen resmî Python doküman bölümünü 150 kelimeyle İngilizce özetle.

## 4. Kanıt ve puanlama — 45 dakika

Güncelle:

- `01-skill-matrix/baseline-assessment.md`
- `01-skill-matrix/skill-matrix.yaml`
- `03-weeks/week-001/ASSESSMENT.md`

Her puanın yanında commit, dosya, test çıktısı, terminal kaydı veya anlatım bağlantısı bulunmalı.

## 5. Retrospektif — 30 dakika

`RETROSPECTIVE.md` içinde cevapla:

- En çok hangi varsayımım yanlış çıktı?
- En güçlü olduğum alan hangisi?
- Nerede AI'ya aşırı bağımlıyım?
- Hangi hata bana en çok şey öğretti?
- Week 002'de hangi konuya daha fazla süre ayrılmalı?
- Çalışma temposu sürdürülebilir mi?

## 6. Git kapanışı — 30 dakika

```bash
git status
git diff main...HEAD
git log --oneline --decorate main..HEAD
```

Hazırsa branch'i push et ve kısa İngilizce pull request açıklaması hazırla.

PR açıklaması şu bölümleri içermeli:

- What changed
- Evidence produced
- Known gaps
- Week 002 recommendations

## Teslimatlar

- [ ] Kapalı kaynak CLI değerlendirmesi
- [ ] En az 8 test
- [ ] Kavramsal sözlü kayıt
- [ ] İngilizce writing, speaking ve reading çıktıları
- [ ] Baseline assessment
- [ ] Güncellenmiş skill matrix
- [ ] Week assessment
- [ ] Retrospective
- [ ] Pull request açıklaması

## Week 002 geçiş kararı

Aşağıdaki seçeneklerden biri kanıta göre seçilir:

- `proceed`: Planlanan Python çekirdeğine geç.
- `proceed-with-reinforcement`: Python çekirdeğine geç, zayıf alanları paralel tekrar et.
- `repeat-critical-sections`: Kritik zihinsel model hatalarını 2–3 gün tekrar et.

Karar güvene göre değil kanıta göre verilir.
