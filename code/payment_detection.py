```python
PAYMENT_HINTS = [
    "upi:", "upi://", "paytm", "gpay", "phonepe",
    "paypal", "stripe", "payu", "razorpay",
    "bitcoin:", "ethereum:", "btc:", "eth:", "iban:", "payto:"
]

def is_payment_payload(text):
    lower = text.lower()
    return any(h in lower for h in PAYMENT_HINTS)
```
