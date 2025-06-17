
DOCX to Clean HTML Converter
============================

Bu Python projesi, `.docx` formatındaki Microsoft Word dosyalarını temiz, sade ve SEO uyumlu HTML'lere dönüştürmek için geliştirilmiştir.

Özellikler
----------
- `.docx` → HTML dönüşümü
- `<a id="...">` gibi boş etiketleri temizler
- Tüm `class`, `id`, `style`, `data-*`, `width`, `height` gibi HTML attribute’larını kaldırır
- Temiz, sadeleştirilmiş HTML çıktısı üretir
- Dönüştürülen dosyaları `output/` klasörüne kaydeder

Gereksinimler
-------------
Python 3 yüklü olmalıdır. Gerekli kütüphaneleri yüklemek için terminale şunu yazın:

    pip install mammoth beautifulsoup4

Kullanım
--------
1. Bu repo'yu klonlayın veya `main.py` dosyasını indirin.
2. `.docx` dosyalarınızı aynı klasöre yerleştirin.
3. Terminal'den klasöre gidin ve script'i çalıştırın:

    python main.py

4. Çıktılar `output/` klasörüne kaydedilecektir.

Klasör Yapısı Örneği
--------------------
.
├── main.py
├── Ford Servis Ankara.docx
├── Opel Servis Aydın.docx
└── output/
    ├── Ford Servis Ankara.html
    └── Opel Servis Aydın.html

Lisans
------
MIT Lisansı ile açık kaynaklıdır. Dilediğiniz gibi kullanabilir, geliştirebilirsiniz.
