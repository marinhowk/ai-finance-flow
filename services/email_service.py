import smtplib
import email.message
from dotenv import load_dotenv
import os
import random

load_dotenv()

EMAIL_ADDRESS =  os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def enviar_email(destinatario):
    codigo_gerado = random.randint(1000, 9999)
    assunto = "Verificação de Email"
    corpo_email = f"""
    <html>
    <body style="margin:0; padding:0; background-color:#f4f4f4; font-family: Arial, sans-serif;">
        <table align="center" width="600" cellpadding="0" cellspacing="0" 
            style="background:#ffffff; margin-top:40px; border-radius:8px; overflow:hidden;">

            <tr>
                <td style="background:#2c3e50; color:white; padding:20px; text-align:center; font-size:22px;">
                    Sistema de Verificação
                </td>
            </tr>

            <tr>
                <td style="padding:30px; color:#333;">
                    <p style="font-size:16px;">Prezado usuário,</p>

                    <p style="font-size:16px;">
                        Recebemos uma solicitação de verificação de conta.
                    </p>

                    <p style="font-size:16px;">
                        Seu código de verificação é:
                    </p>

                    <div style="text-align:center; margin:30px 0;">
                        <span style="
                            font-size:28px;
                            letter-spacing:5px;
                            font-weight:bold;
                            background:#f1f1f1;
                            padding:15px 25px;
                            border-radius:6px;
                            display:inline-block;
                        ">
                            {codigo_gerado}
                        </span>
                    </div>

                    <p style="font-size:14px; color:#777;">
                        Este código expira em 10 minutos.
                    </p>

                    <p style="font-size:14px; color:#777;">
                        Caso você não tenha solicitado, ignore este e-mail.
                    </p>
                </td>
            </tr>

            <tr>
                <td style="background:#f4f4f4; padding:15px; text-align:center; font-size:12px; color:#888;">
                    © 2026 AI Finance Flow • Todos os direitos reservados
                </td>
            </tr>

        </table>
    </body>
    </html>
    """

    msg = email.message.Message()
    msg["Subject"] = assunto
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = destinatario
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo_email)

    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        s.starttls()
        s.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        s.sendmail(EMAIL_ADDRESS, [destinatario], msg.as_string().encode("utf-8"))

    return codigo_gerado

