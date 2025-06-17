import os
import mammoth
from bs4 import BeautifulSoup

input_folder = "."  # Aynı klasördeki docx'leri tara
output_folder = "./output"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".docx"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace(".docx", ".html"))

        with open(input_path, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html = result.value

        soup = BeautifulSoup(html, "html.parser")

        # 1. <a id="..."></a> gibi boş id'li <a> etiketlerini kaldır
        for a in soup.find_all("a", id=True):
            if not a.text and not a.attrs.get("href"):
                a.decompose()
            else:
                del a["id"]

        # 2. Tüm tag'lardan class, id, style, data-*, width, height gibi tüm attribute'ları sil
        for tag in soup.find_all():
            attrs = dict(tag.attrs)  # orijinal attribute'lar
            for attr in attrs:
                if (
                    attr == "class" or
                    attr == "id" or
                    attr.startswith("data-") or
                    attr in ["style", "width", "height"]
                ):
                    del tag.attrs[attr]

        cleaned_html = str(soup)

        with open(output_path, "w", encoding="utf-8") as html_file:
            html_file.write(cleaned_html)

print("✅ Tüm HTML dosyaları oluşturuldu ve tüm gereksiz attribute’lar temizlendi.")

