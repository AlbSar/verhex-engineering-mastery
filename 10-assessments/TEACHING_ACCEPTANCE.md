# Teaching acceptance — 2026-09-07

Bu dosya audit sırasında Codex'in ürettiği öğretim simülasyonudur. Öğrenci sınavı değildir; gerçek concept-state'e puan veya PROVEN kaydı eklemez. Yeni protokolün üç farklı girişte uygulanabilir olduğunu sınar; gelecek tüm model davranışlarının otomatik garantisi değildir.

## Case 1 — UNKNOWN wc

**Fixture:** learner has never seen wc; shell/program introduced; stdin, stdout, pipe and newline need instruction.

**Today / Teach:** "Bugün metin akışını saymayı öğreneceğiz. wc, word count demektir; dosya veya gelen metindeki newline, kelime, byte ve karakter sayılarını çıkarır. Unix'te küçük araçların çıktısını başka araca bağlayabilmek için kullanışlıdır. `wc [OPTION] [FILE]`: dosya adı verilmezse stdin, yani standart girdi okunur. `-l` newline, `-w` kelime, `-c` byte, `-m` karakter sayar. stdout'a sayı yazılır. Byte/karakter ve newline/görünen satır farkını ayrı tutarız."

**Mechanism:** "printf metin üretir; `\n` newline olur. Shell'in `|` operatörü üreticinin stdout'unu tüketicinin stdin'ine bağlar. Linux pipe ile byte akışını taşır, wc user-space programı bu girdiyi okur. Dosyaya ara kayıt gerekmiyor."

**Show:** öğretmen `printf 'x\n' | wc -l` örneğinin neden 1 verdiğini açıklar. printf adı, format, `\n`, tırnak ve pipe ilk kullanımda tanıtılır. Bu demonstration, henüz tahmin sorusu değildir.

**Predict:** ancak şimdi "`printf 'a\nb\n' | wc -l` hangi sayıyı verir?" sorulur. Sonra kullanıcı çalıştırır; öğretmen kullanıcı çıktısını bekler. Reviewer beklentisi 2; kullanıcı bunu henüz çalıştırmış gibi kayıt yapılmaz.

**Observe / Explain / Review:** stdout sayısı, newline sayısı ve kendi akış açıklaması. Sonra final newline olmayan `printf 'a\nb' | wc -l` transferi; beklenen 1. İsteğe bağlı ileride fd 0/1, buffering, süreçler; ilk derse source dump yok.

**Evidence:** kullanıcının gerçek deneyi, tahmini, açıklaması; AI explanation ayrı reference. Öğrenci command anlamını bilmeden çalıştırırsa tahmin geriye yazılmaz.

**Result: PASS (manual protocol simulation).** Teach + semantics + minimal demonstration prediction'dan önce; komut/flag açıklaması mevcut; tek kullanıcı görevi; ilk sonucu bilmediği için quiz yok.

## Case 2 — UNKNOWN decorators

**Fixture:** decorator UNKNOWN; function-as-object/higher-order/wrapper da kurulmamış. Önce bu ön koşullar öğretilir; Week 001'e yeni required ödev eklenmez.

**Teach:** fonksiyon bir nesnedir; bir isme bağlanabilir, argüman verilebilir ve geri döndürülebilir. Başka fonksiyonu alan/döndüren fonksiyon higher-order'dır. Wrapper, asıl fonksiyon çağrısını çevreleyen başka fonksiyondur. Decorator fonksiyonu alıp kullanılacak yeni değeri döndürür. `@decorate` ile tanım, basit durumda `greet = decorate(greet)` dönüşümüdür; decorator her çağrıda tekrar uygulanıyor sanılmamalı.

**Layered demonstration:** önce `def`, `return`, çağrı parantezi, print ve iç fonksiyon scope'u anlatılır; sonra öğretmen aşağıdaki küçük örneği ve çıktısını açıklar:

```python
def decorate(fn):
    def wrapped():
        print('before')
        return fn()
    return wrapped

def greet():
    print('hello')

greet = decorate(greet)
greet()
```

Öğretmen beklenen `before`, `hello` sırasını mekanizmayla gösterir. `wrapped` fn binding'ine erişir. Sonra aynı bağlamanın `@decorate` biçimi gösterilir. Production için metadata, argument forwarding, exception behavior ve functools.wraps ileride ayrıca öğretilir; ilk örneğe açıklamasız eklenmez.

**Predict / single task:** öğretimden sonra kullanıcı farklı bir gövde metniyle kendi minimal örneğinin çıktısını tahmin eder, yazar, çalıştırır; dönüşüm eşdeğerliğini açıklar. Tam uygulama ödevi Codex tarafından yazılmaz.

**Result: PASS (manual protocol simulation).** Yeni syntax tahmininden önce function object → higher-order → wrapper → desugaring sırası var. Kaynak: [Python function definitions](https://docs.python.org/3.12/reference/compound_stmts.html#function-definitions). Bu hipotetik fixture gerçek öğrencinin decorator durumunu değiştirmez.

## Case 3 — PRACTICING aliasing

**Fixture:** list basics, assignment ve append prior knowledge olarak kurulmuş; aliasing PRACTICING. Gerçek öğrencide şu an bu kanıt yoktur; bu yalnızca acceptance fixture'dır.

**Recall:** "İki isim aynı liste nesnesine bağlanabilir; mutation nesneyi değiştirir, rebinding ismin bağını değiştirir." Yeni açıklamasız API yoktur.

**Predict before execution:**

```python
a = [1]
b = a
b.append(2)
print(a)
```

Kullanıcı tahmin eder, kendi denemesini çalıştırır. Reviewer beklentisi `[1, 2]`; yürütme öncesi learner yerine cevaplanmaz. Sonra kullanıcı `b = [9]` rebinding varyantını karşılaştırır ve iki isim/nesne diyagramı çizer. append daha önce öğretilmemişse fixture geçersiz; önce onu öğret.

**Review / production:** alias ile copy ayrımı; request verisini paylaşmanın side-effect riski; kullanıcı küçük regression testi yazar.

**Result: PASS (manual protocol simulation).** Burada kısa recall sonrası prediction uygun; bilinmeyen prerequisite gizlenmiyor, öğretim gereksiz başa sarılmıyor.

## Teknik örnek doğrulaması

Audit-only olarak printf/wc 1→2→1 örnekleri, decorator çağrı sırası ve alias/rebinding örnekleri ayrı Python/Bash process'lerinde kontrol edilir. Bunlar learner evidence değildir. Yapısal checker ayrıca daily hours, relative links, YAML ve kanıt olmadan skor geçişini kontrol eder. Hiçbir string check tek başına öğretim davranışını kanıtlamaz; yukarıdaki senaryolar ayrıca gözden geçirilmiştir.
