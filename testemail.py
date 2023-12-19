import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def forgotPasswordMail(subject, html_body, image_path, to_email):
    MAIL_ID = "academia.campus.repository@gmail.com"
    PASSWORD = "obdq aojy inuq sbmu"
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  

    msg = MIMEMultipart()
    msg['From'] = MAIL_ID
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(html_body, 'html'))

    # Attach the image
    with open(image_path, 'rb') as image_file:
        img = MIMEImage(image_file.read(), name='image.png')
        img.add_header('Content-ID', '<image1>')
        msg.attach(img)

    # Connect to the Gmail SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Enable TLS
        server.starttls()

        # Log in to the Gmail SMTP server
        server.login(MAIL_ID, PASSWORD)

        # Send the email
        server.sendmail(MAIL_ID, to_email, msg.as_string())

# Replace the following variables with your own values
subject = 'Gmail HTML Email with Image Test'
html_body = '<p>This is a test email sent from Python with an <b>image</b>.</p><img src="cid:image1" alt="Image">'
image_path = 'image1.png'
to_email = 'vishalatmadurai@gmail.com'

# Call the function to send the Gmail HTML email with an image
forgotPasswordMail(subject, html_body, image_path, to_email)
