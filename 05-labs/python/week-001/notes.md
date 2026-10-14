ilk değişiklik
ikinci değişiklik

## 2026-09-06 — Bash, PATH ve Python'un çalıştırılması

Bu bölüm, kullanıcının paylaştığı terminal çıktılarından hareketle Codex tarafından tekrar okumak için hazırlanmıştır. Kullanıcının kendi yazdığı teach-back veya bağımsız mastery kanıtı değildir.

### Terminal ve shell

Cursor'ın terminal paneli komut girip çıktıları gördüğümüz arayüzdür. Shell ise komutları yorumlayan programdır. WSL terminalinde `ps -p $$ -o comm=` çıktısıyla çalışan shell'in Bash olduğunu gözlemledik. Bash de Linux üzerinde çalışan bir process'tir; `$$` Bash tarafından kendi process kimliğiyle (PID) değiştirilir.

Python shell'den ayrı bir programdır. Shell değiştirmek Python'u yeniden kurmayı gerektirmez. Ancak shell ayarları farklı olduğunda aynı komut adı farklı program yollarına çözümlenebilir.

### PATH ne işe yarar?

PATH, dış programların aranacağı dizinlerin sıralı listesini tutan bir ortam değişkenidir. Linux'ta dizinler `:` ile ayrılır. PATH programın kendisini veya sürüm bilgisini içermez.

Yeni bir PATH aramasında dizinler soldan sağa değerlendirilir; ilk uygun çalıştırılabilir dosya seçilir. Örneğin PATH `/opt/tools/bin:/usr/bin` ise ve ikisinde de çalıştırılabilir `python` varsa `/opt/tools/bin/python` seçilir. Bash alias, fonksiyon ve builtin komutları da çözümleyebilir; önceden bulduğu dış komut yollarını önbellekte tutabilir.

`command -v python`, Python'u çalıştırmadan Bash'in bu adı nasıl çözümlediğini gösterir. Bu oturumda çıktı `/usr/bin/python` oldu.

`python --version` komutunda program adı çözümlenir. `/usr/bin/python --version` komutunda ise yol açıkça verildiği için PATH araması yapılmaz. Yalnızca PATH sırasını değiştirmek ikinci komutun seçtiği yolu değiştirmez.

### Gözlemlediğimiz sembolik bağlantı zinciri

```text
/usr/bin/python → python3
/usr/bin/python3 → python3.12
/usr/bin/python3.12 → normal, çalıştırılabilir dosya
```

`ls -l` çıktısının ilk karakteri `l` ise sembolik bağlantı, `-` ise normal dosyadır. İzin alanındaki `x` çalıştırma iznini gösterir. `->` işaretinden sonraki metin bağlantının hedefidir.

`python3` gibi `/` ile başlamayan bağlantı hedefleri, bağlantının bulunduğu dizine göre yorumlanır; terminalin o anki çalışma dizinine göre değil. Tam yol kullanmak PATH aramasını atlar, sembolik bağlantıların takip edilmesini engellemez.

### Komutu yazınca ne olur?

1. Terminal komut satırını Bash'e iletir.
2. Bash `python` komut adını ve `--version` argümanını ayrıştırır; programın yolunu çözümler.
3. Bash normal durumda bir çocuk process oluşturur; Linux programı çalıştırırken sembolik bağlantıları takip ederek asıl dosyaya ulaşır.
4. Çalışan Python, `--version` argümanını işler ve sürüm bilgisini üretir.
5. Python kapanır; Bash yeni komutu bekler.

Kullanıcının çalıştırdığı hem `python --version` hem `/usr/bin/python --version`, `Python 3.12.3` çıktısını verdi. Dosya adının `python3.12` olması, programın tam sürümünün `3.12.3` olmasına engel değildir.

### Oturumda düzeltilen varsayımlar

- `/usr/bin` sistem dizini olduğu için otomatik öncelikli değildir; yeni bir PATH aramasında dizin sırası belirleyicidir.
- Tam yol verilen komutun seçtiği program yolu, yalnızca PATH değiştirilerek değiştirilmez.
- `/usr/bin/python` doğrudan program dosyası çıkmadı; iki sembolik bağlantı üzerinden `/usr/bin/python3.12` dosyasına ulaştık.
- Sürümü PATH veya Bash üretmez; çalışan Python üretir. `--version`, Python'a verilen argümandır.

- Git add sonrasında dosyada yaptığım değişiklik kendiliğinden stage edilmez.
