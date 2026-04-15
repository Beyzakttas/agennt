# 📌 Agent Projesi (FastAPI + AI + Mock Bank System)

## 📖 Proje Tanımı

Bu proje, bir **banka destek asistanı (AI Agent)** simülasyonudur. Kullanıcıların e-posta ve mesajlarına göre sahte (mock) banka verilerini analiz eder ve ödeme hatası / hesap durumu gibi sorulara yanıt üretir.

Sistem:

* FastAPI backend
* Basit kural tabanlı + AI destekli agent mimarisi
* Mock kullanıcı ve işlem veritabanı
* (Opsiyonel) LLM entegrasyonu (Ollama / OpenAI / Gemini)

---

## 🧠 Sistem Mimarisi

```
Kullanıcı (curl / Swagger UI)
        │
        ▼
FastAPI Endpoint (/ask)
        │
        ▼
Agent Layer (agent.py)
        │
        ├── Tool Layer (tools.py)
        │       ├── email extraction
        │       ├── transaction lookup
        │       ├── fraud reason fetch
        │
        ▼
Mock Database (mock_db.py)
        │
        ▼
Response Generator
        │
        ▼
JSON Response
```

---

## 📁 Proje Dosya Yapısı

```
agent_projesi/
│── app/
│   │── main.py              # FastAPI giriş noktası
│   │── agent.py             # AI agent mantığı
│   │── tools.py             # Tool fonksiyonları
│   │── mock_db.py           # Sahte veri tabanı
│   │── schemas.py           # Pydantic modeller
│
│── run.py                   # Uvicorn başlatıcı
│── requirements.txt         # Bağımlılıklar
│── README.md                # Proje dokümantasyonu
```

---

## ⚙️ Kurulum

### 1. Sanal ortam oluştur

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Paketleri yükle

```bash
pip install fastapi uvicorn langchain langchain-core langchain-community
```

### (Ollama kullanıyorsan)

```bash
pip install ollama
```

---

## 🚀 Çalıştırma

```bash
python run.py
```

veya

```bash
uvicorn app.main:app --reload
```

---

## 🌐 API Endpoint

### 🔹 POST /ask

Kullanıcı mesajını analiz eder.

#### Request:

```json
{
  "text": "ali@sirket.com hesabımla yapılan ödeme neden reddedildi?"
}
```

#### Response:

```json
{
  "answer": "İşlem başarısız... neden: Yetersiz bakiye"
}
```

---

## 🧠 Agent Mantığı

Agent şu adımları uygular:

1. Metinden e-posta çıkarılır
2. Kullanıcı MOCK_USERS içinde aranır
3. Kullanıcının işlemleri MOCK_TRANSACTIONS içinden alınır
4. FAILED transaction bulunur
5. Hata sebebi MOCK_FRAUD_REASONS içinden çekilir
6. Kullanıcıya açıklama döndürülür

---

## 🧾 Mock Veriler

### Kullanıcılar

* [ali@sirket.com](mailto:ali@sirket.com) → active
* [ayse@sirket.com](mailto:ayse@sirket.com) → suspended

### İşlemler

* TRX-001 → success
* TRX-002 → failed
* TRX-003 → failed

---

## 🧪 Test Örnekleri

```bash
curl -X POST http://127.0.0.1:8000/ask \
-H "Content-Type: application/json" \
-d '{"text":"ali@sirket.com ödeme neden başarısız oldu?"}'
```

---

## 🧩 Kullanılan Teknolojiler

* Python 3.11
* FastAPI
* Pydantic
* Uvicorn
* (Opsiyonel) LangChain
* (Opsiyonel) Ollama / LLM

---

## ⚠️ Bilinen Sorunlar

* LangChain agent format hataları (ReAct prompt)
* LLM model uyumsuzluğu (Gemini / OpenAI model isimleri)
* Mock DB import path hataları

---

## 🎯 Geliştirme Fikirleri

* Gerçek PostgreSQL entegrasyonu
* JWT authentication
* Streaming AI response
* React frontend
* Multi-agent system

---

## 🧪 Projenin Nasıl Gerçekleştirildiği (Özet)

Bu proje adım adım geliştirilmiştir:

1. Öncelikle FastAPI tabanlı bir backend kurulmuştur.
2. Kullanıcıdan gelen istekleri almak için `/ask` endpoint’i oluşturulmuştur.
3. E-posta tespiti için regex tabanlı bir extractor yazılmıştır.
4. Mock bir banka veritabanı (kullanıcılar, işlemler, hata sebepleri) hazırlanmıştır.
5. İş mantığı katmanı (agent logic) oluşturularak:

   * Kullanıcı bulunur
   * Kullanıcının işlemleri çekilir
   * Başarısız işlem filtrelenir
   * Hata sebebi eşleştirilir
6. Sonuç kullanıcıya açıklayıcı bir metin olarak döndürülür.
7. Geliştirme sürecinde LangChain denemeleri yapılmış ancak sade mimari tercih edilmiştir.
8. Son aşamada Ollama / LLM entegrasyonu test edilmiştir (opsiyonel).

---

## 🤖 Ollama Kullanma Sebebi

Bu projede Ollama tercih edilmesinin temel nedenleri şunlardır:

* 💰 Ücretsiz ve yerel çalışır: API maliyeti yoktur ve dış servislere bağımlı değildir.
* 🔒 Gizlilik: Veriler dış bir API’ye gönderilmez, tüm işlem yerel makinede gerçekleşir.
* ⚡ Hızlı prototipleme: LLM modelleri (Qwen, Llama vb.) kolayca test edilebilir.
* 🧪 Offline kullanım: İnternet olmadan bile model çalıştırılabilir.
* 🧠 Model esnekliği: Farklı açık kaynak modeller (qwen, llama3 vb.) kolayca değiştirilebilir.

Bu nedenle proje geliştirme sürecinde LangChain + bulut API yerine Ollama tercih edilmiştir.

## 👨‍💻 Geliştirici Notu

Bu proje eğitim amaçlıdır ve gerçek banka sistemi değildir.
Tüm veriler mock (sahte) olarak tasarlanmıştır.
