# Northstar Support Deflection MVP

**Group 36 — Team Syntatix | Power Learn Project | The Northstar Sprint**

A 1-week industry simulation to reduce manual ticket handling for Northstar Retail Co.'s support team. This MVP covers **Order Status**, **Returns & Refunds**, and **Stock Availability** via an offline Python chatbot that reads directly from a validated JSON dataset.

---

## 📋 Team

| Name | Role | Phone | Email |
|---|---|---|---|
| Swaleh Rama | Tester / Documentation | +254 791 519 981 | rmswaleh1@students.uonbi.ac.ke |
| Emmanuel Ukah | AI Prompts / Integration | +234 818 848 8338 | nuelukah@gmail.com |
| Tracy Wangari | Team Lead / Tester / Audit | — | tracywangari997@gmail.com |
| Abraham Makur Mayor Nyidier | Lead Developer / Repo Setup | +211 927 772 704 | makuurmayornyidier@gmail.com |
| Milkah Michira | Data Engineer / Packaging | +254 729 254 541 | michiramilkah@gmail.com |

---

## What This MVP Does

| Ticket Type | Status | How It Works |
|---|---|---|
| **Order Status** | ✅ Live | User enters Order ID → bot returns status, tracking number, carrier, and estimated delivery |
| **Returns & Refunds** | ✅ Live | User enters Return ID → bot returns refund status, amount, method, and timeline |
| **Stock Availability** | ✅ Live | User searches by product name → bot returns stock count, price, and restock date |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+

### Run the Chatbot (Offline — No API Keys Needed)
```bash
git clone https://github.com/MakurWai-ajokNyidier/GROUP36.git
cd GROUP36
python src/chatbot.py
