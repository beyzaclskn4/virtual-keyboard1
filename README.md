# ⌨️ AI Virtual Keyboard (Yapay Zeka Destekli Sanal Klavye)

Bu proje, bilgisayar görüsü (Computer Vision) tekniklerini kullanarak fiziksel bir klavyeye ihtiyaç duymadan, havada parmak hareketleriyle yazı yazmanızı sağlayan temassız bir insan-bilgisayar etkileşimi (HCI) uygulamasıdır.

Web kamerası üzerinden alınan görüntüler gerçek zamanlı işlenir, el ve parmak eklemleri tespit edilir ve **başparmak ile işaret parmağının birleşmesi** hareketi "tıklama" olarak algılanır.

## 🌟 Özellikler

* **🖐️ Temassız Teknoloji:** Fiziksel temas olmadan, sadece kamera karşısında el hareketleriyle kontrol.
* **🧠 Akıllı Tıklama Algoritması:** Başparmak ve işaret parmağı arasındaki mesafe hesaplanarak tıklama hassasiyeti optimize edilmiştir.
* **🎨 Görsel Geri Bildirim:**
    * **Gezinme:** Tuşların üzerine gelindiğinde renk değişir.
    * **Tıklama:** Tıklama yapıldığında tuş yeşil yanar ve görsel vurgu yapılır.
* **💻 Gerçek Klavye Entegrasyonu:** `pynput` kütüphanesi sayesinde sanal klavyede basılan tuşlar, bilgisayarınızda açık olan herhangi bir uygulamaya (Notepad, Word, Tarayıcı vb.) anlık olarak aktarılır.
* **⚡ Yüksek Performans:** CvZone ve MediaPipe sayesinde düşük gecikme ile çalışır.

## 🛠️ Kullanılan Teknolojiler

* **Python 3.x:** Ana programlama dili.
* **OpenCV:** Görüntü işleme ve kamera akışı.
* **CvZone:** MediaPipe tabanlı el takibi modülü (Hand Tracking).
* **MediaPipe:** Google'ın makine öğrenmesi tabanlı iskelet çıkarma kütüphanesi.
* **Pynput:** İşletim sistemi seviyesinde klavye kontrolü.

## 📂 Proje Yapısı

```text
├── main.py              # Projenin ana kaynak kodu
├── requirements.txt     # Gerekli kütüphanelerin listesi
├── .gitignore           # Gereksiz dosyaların (venv vb.) yüklenmesini engeller
└── README.md            # Proje dökümantasyonu
🚀 Kurulum Adımları
Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

Projeyi Klonlayın:

Bash

git clone [https://github.com/KULLANICI_ADIN/REPO_ADIN.git](https://github.com/KULLANICI_ADIN/REPO_ADIN.git)
cd REPO_ADIN
Sanal Ortamı Kurun (Önerilen):

Bash

python -m venv venv
# Windows için:
.\venv\Scripts\activate
# Mac/Linux için:
source venv/bin/activate
Gerekli Kütüphaneleri Yükleyin:

Bash

pip install -r requirements.txt
(Eğer requirements dosyası yoksa: pip install opencv-python cvzone mediapipe pynput)

Uygulamayı Başlatın:

Bash

python main.py
🎮 Nasıl Kullanılır?
Uygulamayı başlattığınızda web kameranız açılacaktır.

Elinizi kameraya gösterin (İskelet sistemi çizilecektir).

İşaret parmağınızı kullanmak istediğiniz harfin üzerine getirin.

Tuşa basmak için Başparmağınızı ve İşaret parmağınızı birbirine değdirin (Pinch Hareketi).

Tıklama başarılı olduğunda tuş yeşil renge döner ve harf ekrana yazılır.

Çıkış yapmak için klavyeden q tuşuna basabilirsiniz.

🤝 Katkıda Bulunma
Projeyi geliştirmek isterseniz (örneğin: sayısal tuş takımı eklemek, Türkçe karakter desteği vb.) "Pull Request" göndermekten çekinmeyin.