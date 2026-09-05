# Curated Resources

Bu klasör yalnızca doğrulanmış ve doğrudan programa bağlanan kaynakları içerir. Kaynak tüketimi amaç değil; aktif learning outcome için kullanılan araçtır.

## Çekirdek repository seti

| Repository | Programdaki rolü | Kullanım biçimi |
|---|---|---|
| `nilbuild/developer-roadmap` | Yön / kapsam | Bir alanda öğrenilecek başlıkları ve prerequisite sırasını çıkarmak |
| `freeCodeCamp/freeCodeCamp` | Structured learning / practice | Temel ders, egzersiz, quiz ve proje pratiği |
| `sindresorhus/awesome` | Ecosystem discovery | İlgili alandaki kaliteli primary docs, araçlar ve ileri kaynakları bulmak |
| `codecrafters-io/build-your-own-x` | Mechanism by construction | HTTP server, DB, Redis, shell, container, LLM vb. kritik teknolojileri küçük ölçekte sıfırdan yapmak |
| `donnemartin/system-design-primer` | System design | Scalability, availability, consistency, caching, queues, sharding, load balancing ve architecture case çalışmaları |
| `torvalds/linux` | Production internals | Aktif Linux kavramına bağlı kernel documentation ve seçilmiş implementation yollarını incelemek |

## Kaynak kullanım zinciri

Tercih edilen akış:

1. `developer-roadmap` ile kapsamı gör.
2. Resmî/primary documentation ile mekanizmayı öğren.
3. Gerekiyorsa `freeCodeCamp` ile structured practice yap.
4. `build-your-own-x` ile kritik parçayı kendin inşa et.
5. `awesome` üzerinden daha iyi/derin kaynakları keşfet.
6. Gerçek production repository'de aynı mekanizmanın implementasyonunu incele.
7. Kendi lab veya gerçek projende uygula.
8. Evidence ve reflection kaydı bırak.

Her konuda tüm adımlar zorunlu değildir; learning outcome için en kısa ama yeterli zincir seçilir.

## Production code reading kuralı

Büyük repository baştan sona okunmaz. Aktif soruya göre şu zincir izlenir:

concept → official documentation → source location → call/data path → tests → relevant issue/commit → own explanation

Örnek:

`process scheduling` çalışılıyorsa Linux kernel'in tamamı değil, scheduler documentation ve ilgili seçilmiş kod yolları incelenir.

## Kaynak ekleme kriteri

Yeni kaynak eklenmeden önce şu bilgiler belirlenir:

- Başlık / repository
- Primary veya secondary kaynak sınıfı
- İlgili phase/week
- Hangi learning outcome'u desteklediği
- Okunacak/çalışılacak bölüm
- Üretilecek evidence
- Erişim veya sürüm tarihi

## Yasak anti-pattern

- star sayısına bakıp kaynak yığmak
- aktif hedef olmadan tutorial tüketmek
- bir konuyu sadece video izleyerek tamamlanmış saymak
- README okumayı implementation bilgisi sanmak
- AI özetini primary kaynağın yerine koymak

## NotebookLM / AI kullanımı

NotebookLM veya başka bir knowledge tool'a tüm internet veya tüm repository dump edilmez. Aktif hafta için seçilmiş, doğrulanmış kaynak paketi kullanılır.

Codex kaynakları hızlı sorgulamak ve doğru bölümü bulmak için kullanılabilir; ancak kaynak okuma, deney ve teknik çıkarım kullanıcının mastery evidence'ının parçasıdır.
