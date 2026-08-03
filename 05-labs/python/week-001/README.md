# Week 001 Python Laboratory

Bu klasör Week 001 boyunca üretilen deney, test ve küçük CLI çalışmalarını içerir.

## Zorunlu yapı

```text
week-001/
├── README.md
├── pyproject.toml
├── src/
│   └── week001/
│       ├── __init__.py
│       ├── object_identity.py
│       ├── mutability.py
│       ├── closures.py
│       ├── duplicate_analyzer.py
│       ├── dependency_scheduler.py
│       └── record_audit_cli.py
└── tests/
    ├── test_object_identity.py
    ├── test_mutability.py
    ├── test_closures.py
    ├── test_duplicate_analyzer.py
    ├── test_dependency_scheduler.py
    └── test_record_audit_cli.py
```

## Çalışma sözleşmesi

Her laboratuvar:

1. Çalıştırılmadan önce yazılı tahmin içerir.
2. En az bir normal durum ve bir edge case içerir.
3. Testlerle doğrulanır.
4. Konunun mekanizmasını açıklayan kısa not içerir.
5. Production kullanım veya failure mode bağlantısı kurar.
6. AI tarafından üretilen bölüm varsa açıkça belirtilir ve kullanıcı tarafından açıklanır.

## Kalite kapıları

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run pyright
```

## Tamamlanma tanımı

Bir dosyanın çalışması tek başına yeterli değildir. Aşağıdakiler birlikte gerekir:

- Doğru davranış
- Type kontrolü
- Test
- Açıklanabilir tasarım
- Hata senaryosu
- Commit kanıtı

## Week 001 nihai ürünü

`verhex-record-audit`:

- JSON Lines veya CSV kayıt girdisi
- Typed validation
- Duplicate detection
- Hatalı satır raporu
- Structured summary
- Custom exception
- Unit tests
- CLI exit codes
