import ssl
import OpenSSL

def verify_certificate(cert_path):
    with open(cert_path, 'rt') as cert_file:
        cert_data = cert_file.read()
    
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert_data)
    store = OpenSSL.crypto.X509Store()
    store_ctx = OpenSSL.crypto.X509StoreContext(store, cert)
    
    try:
        store_ctx.verify_certificate()
        print("証明書は有効です。")
    except OpenSSL.crypto.X509StoreContextError as e:
        print(f"証明書は無効です: {e}")

verify_certificate('biccamera.pem')