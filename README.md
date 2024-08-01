# Yesiloğulları Desserts

Yesiloğulları Desserts, en lezzetli Antep tatlılarını sunan bir web sitesidir. Bu projede, kullanıcılar çeşitli Antep tatlılarını inceleyebilir, sepete ekleyebilir ve online ödeme yapabilirler.

## Özellikler

- Tatlıları listeleme
- Tatlıları sepete ekleme ve sepeti yönetme
- Online ödeme işlemi

## Kurulum

### Gereksinimler

- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-WTF

### Adımlar

1. Bu projeyi yerel makinenize klonlayın:

    ```bash
    git clone https://github.com/Bbakac/YesilogullariDesserts.git
    ```

2. Proje dizinine gidin:

    ```bash
    cd YesilogullariDesserts
    ```

3. Gerekli paketleri yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

4. Veritabanını oluşturun:

    ```python
    from app import db, app
    with app.app_context():
        db.create_all()
    ```

5. Uygulamayı başlatın:

    ```bash
    flask run
    ```

6. Web tarayıcınızda `http://127.0.0.1:5000` adresine gidin.

## Proje Yapısı

- `app.py`: Flask uygulamasının ana dosyası.
- `models.py`: Veritabanı modellerini içerir.
- `config.py`: Konfigürasyon ayarlarını içerir.
- `static/`: CSS, görüntüler gibi statik dosyaları içerir.
- `templates/`: HTML şablonlarını içerir.

## Kullanım

### Tatlılar Sayfası

Tatlılar sayfasında, kullanıcılar farklı tatlıları görebilir ve sepetlerine ekleyebilirler.

### Sepet Sayfası

Sepet sayfasında, kullanıcılar sepetlerine ekledikleri ürünleri görebilir ve yönetebilirler.

### Ödeme Sayfası

Ödeme sayfasında, kullanıcılar ödeme bilgilerini girerek siparişlerini tamamlayabilirler.

## Ekran Görüntüleri

Tatlılar Sayfası:
![Tatlılar](static/tatlilar.png)

Sepet Sayfası:
![Sepet](static/sepet.png)

Ödeme Sayfası:
![Ödeme](static/odeme.png)

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request oluşturun. Her türlü katkı ve geri bildirim için teşekkür ederiz.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

---

Bu proje, Flask ve Bootstrap kullanarak geliştirilmiştir. Amacı, en lezzetli Antep tatlılarını dijital ortamda sunmaktır. Projeye katkıda bulunmak ve geri bildirimde bulunmak için lütfen iletişime geçin.
