# Week 001 controlled labs

Bu klasör kullanıcı implementation alanıdır. Mevcut `environment.py`, test, notes, pyproject ve lock kullanıcı çalışması olarak korunur. Testin runtime_name döndürmesi tüm ortamı veya Python mastery'yi kanıtlamaz.

## REQUIRED yol ve sahiplik
- Day 01: `src/week001/runtime_probe.py`, bir küçük test.
- Day 02: `src/week001/object_identity.py`, üç test.
- Day 03: `src/week001/mutability.py`, iki test + debug journal.
- Day 04: `src/week001/closures.py`, scope/function ve iki test; closure yalnızca introduction olabilir.
- Day 05: `src/week001/duplicate_analyzer.py`, üç test.
- Day 06: mevcut local HTTP server ile process/port/recovery evidence; özel server implementation henüz şart değil.
- Day 07: öğretilen problemden küçük bağımsız varyant, iki test.

Dosyalar planlanan öğrenci teslimatlarıdır, Codex tarafından scaffold edilmez. Testler `tests/` altında kullanıcı tarafından yazılır. Her yeni syntax/API/flag önce öğretilir. UNKNOWN için Teach → Demonstrate → Predict → Practice → Observe → Explain → Review; PRACTICING için kısa recall sonrası prediction.

## Toolchain
Mevcut proje mypy kullanır; pyright zorunluluğu yoktur. `uv run` proje ortamında komut yürütür, sistem `python` ile aynı executable olmak zorunda değildir. Komut/flag kartı ve minimal öğretimden sonra kullanıcı:

- `uv run pytest`: test discovery ve assertions ile davranış testleri.
- `uv run ruff check .`: mevcut dizinde lint kuralları.
- `uv run ruff format --check .`: dosya değiştirmeden format denetimi.
- `uv run mypy src`: çalıştırmadan type analizi.

Bunlar runtime testinin veya açıklamanın yerine geçmez. Kurulum ve öğrenme saatleri gün bütçesine dahildir. Type/lint kapsamı aktif küçük lab'dır, bilinmeyen syntax zorla eklenmez.

## OPTIONAL / STRETCH / REFERENCE
Tam JSONL/CSV CLI, custom exceptions, dependency_scheduler ve advanced benchmark Week 001 required değildir. Phase A'da ön koşullarla açılır. Kaynak paketleri [Week 001 cards](../../../12-resources/WEEK_001.md) içinde; production uygulamaları referans, kopyalanacak çözüm değildir.

## Evidence
Tahmin (öğretimden sonra), komut/kod, gerçek sonuç, hata/debug ve açıklama. AI katkısı ayrı yazılır. Kanıt dosyası adı gerçek tarihle; mevcut tarihsel notlar değiştirilmez. [Week plan](../../../03-weeks/week-001/WEEK_PLAN.md) tek kapsam otoritesidir.
