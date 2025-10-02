import qrcode
import base64
from io import BytesIO

def generate_upi_qr_base64(amount: float, txn_id: str, upi_id="pratapchoubey3@oksbi", payee_name="Pratap") -> str:
    """
    Generates a base64-encoded UPI QR code image for the given amount and transaction ID.
    """
    amount = round(amount, 2)  # Ensure 2 decimal places

    upi_link = (
        f"upi://pay?pa={upi_id}"
        f"&pn={payee_name}"
        f"&mc=0000"
        f"&tid={txn_id}"
        f"&tr={txn_id}"
        f"&am={amount}"
        f"&cu=INR"
        f"&tn=Payment+for+Rental"
    )

    qr = qrcode.QRCode(
        version=None,  # automatically adjust QR size
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(upi_link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    
    return f"data:image/png;base64,{qr_base64}"
