import urllib.parse
text = "upi://pay?pa=9876543210@kotakbank&pn=ThenamSoftwareSolutions&am=99&cu=INR"
encoded_text = urllib.parse.quote_plus(text)
qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={encoded_text}"x
print(qr_url)
