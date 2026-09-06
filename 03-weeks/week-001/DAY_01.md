---
status: active
day: 1
date: 2026-09-05
estimated_hours: 4
---

# Day 01 — Ortam, shell ve ilk Python deneyi

## Oturum sözleşmesi
Öğretmen önce [concept-state](../../01-skill-matrix/concept-state.yaml) kaydını okur; kaydı olmayan ön koşulu UNKNOWN sayar. Today → Teach → Mechanism → Example → Predict → Lab → Observe → Review → Teach Back → Evidence sırası uygulanır. Her yeni komut/API/flag açıklanır; tek seferde yalnızca bir görev verilir. Kaynak okuma, açıklama, test ve kayıt aşağıdaki sürelere dahildir. Süre dolunca kalan required konu sonraki oturuma taşınır; tarihe göre atlanmaz. OPTIONAL/STRETCH ek süreleri ayrı kaydedilir ve geçiş koşulu değildir.

Kaynak bölümü, deney ve artefact: [Week 001 kaynak kartları](../../12-resources/WEEK_001.md). Komutlar için [ilk kullanım kartları](../../12-resources/COMMAND_PRIMER.md); kartı sadece linklemek öğretim yerine geçmez.

## Today
REQUIRED hedef: terminal/shell/program ayrımını ve Python'un nasıl başlatıldığını açıklamak; küçük bir Python dosyası çalıştırmak; Git çalışma alanını korumak. Neden: daha sonra runtime ve network hatalarının hangi katmanda olduğunu ayırt etmek.
Ön koşullar: terminale erişim; dosya açma/kaydetme. Bunlar bile kurulmamışsa önce göster. Python syntax, PATH, Git index ve pipe bilgisi varsayılmaz. Ağ deneyinin ayrıntısı Day 06'dadır.

## 1. Öğretim ve ortam — 60 dakika
Shell/program/PATH ve argüman kavramlarını basit model, teknik mekanizma ve tek örnekle öğret. Bir seferde `command -v python`, `python --version`, sonra gerekirse `uv --version` ve `git --version` açıkla. Versiyon sorgusu araç kurulumunun tümü veya mastery kanıtı değildir. Mevcut çalışan ortamı yeniden kurma.

Observe: seçilen executable yolu ile sürüm çıktısını ayır. Tahmin sadece öğretimden sonra. Mevcut oturum kanıtı varsa tekrar komut maratonu yerine kısa review yap. Windows/WSL ayrımı ihtiyaç kadar anlatılır.

## 2. Shell akışı — 35 dakika
Argüman, exit status ve stdout/stdin modelini öğret. `printf`, `echo`, `$?`, `&&`, `||`, `|` ve `wc -l` kartları ilk kullanımda açıklanır. Tek küçük pipeline deneyi yap; mekanizma: üreticinin stdout'u kernel pipe üzerinden tüketicinin stdin'ine gider. Yeni komutları birbirine eklemeden önce her birini tanıt.
Observe: metin çıktısı ile sayısal exit code farklıdır; `wc -l` newline sayar. Shell kaynak kodu, tüm PATH girdilerinin kökeni ve symlink derinleşmesi REFERENCE; günün odağını tüketmez.

## 3. Git çalışma modeli — 30 dakika
Working tree → index → commit snapshot → branch pointer ilişkisini öğret. `git status`, `git diff`, `git diff --cached`, `git log --oneline` seçeneklerini açıkla, sonra kullanıcı kendi değişikliğini incelesin. Daha önce klonlu repoyu klonlatma. Yerel/remote ayrışma varsa önce koruma planı; reset veya kör rebase yok.

## 4. Python ve lab alanı — 80 dakika
Önce literal, isim bağlama, liste, `print()` ve program dosyasının nasıl yürütüldüğünü öğret. [Lab README](../../05-labs/python/week-001/README.md) içindeki mevcut `src/` ve `tests/` yapısını açıkla. `uv run` proje ortamı ile sistem Python'u arasındaki ayrımı öğret; packaging ayrıntıları sonraki faza kalabilir.
Kullanıcı `src/week001/runtime_probe.py` içinde küçük isim/değer ve liste örneği yazar. Önce farklı bir minimal öğretmen örneği; sonra kullanıcı kendi örneği hakkında tahmin üretir. `type()`/`id()` kullanılacaksa önce tanıt; identity derinliği Day 02'de.
pytest assertion ve test discovery önce açıklanır; tek küçük davranış testi yeterlidir. Ruff/mypy neyi kontrol eder gösterilir; tool kurulumu uzarsa kalan işler kaydedilip ertelenir.

## 5. Review ve evidence — 35 dakika
Tek bir yanlış varsayım, gerçek terminal çıktısı, yazılan lab/test ve açıklama kaydedilir. Gerçek çalışma tarihini kullan; kickoff dosyasına geriye dönük başarı yazma. AI notları reference olarak ayrılır. Git staging/commit henüz bilinmiyorsa önce kartla öğret; sadece seçilen evidence dosyaları stage edilir, diff okunur, kullanıcı commit eder.

## REQUIRED evidence
- Ortam yolu/sürümü ve shell açıklaması.
- Bir shell akışı tahmin/gözlemi ve açıklaması.
- Git working tree/index/commit ayrımına ilişkin kanıt.
- Kullanıcı runtime_probe örneği ve bir küçük test.
- Gerçek tarihli günlük veya kaynaklı etkileşim kaydı.

## OPTIONAL / STRETCH / REFERENCE
OPTIONAL: Docker mevcutsa sürüm diagnostic, en fazla 15 dakika ek süre. STRETCH: CPU/RAM/disk envanteri, en fazla 15 dakika ek süre. REFERENCE: symlink ve shell source navigation; zorunlu gün bütçesine yeni görev eklemez.
