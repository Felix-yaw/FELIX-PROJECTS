import PySimpleGUI as psg
import qrcode as qr
import os

def generate_qr_code(text):
    qr_code = qr.QRCode(version=1, box_size=10, border=4)
    qr_code.add_data(text)
    qr_code.make(fit=True)
    qr_img = qr_code.make_image(fill_color="yellow", back_color="green")
    return qr_img

def main():
    psg.theme("DarkAmber")
    layout = [
        [psg.Text("Enter text to generate QR Code: ")],
        [psg.InputText(key="text_input")],
        [psg.Button("Create"), psg.Exit()],
        [psg.Image(key="qr_code_output")]
    ]

    window = psg.Window("QR Code Generator", layout)

    while True:
        event, values = window.read()
        if event == "Create":
            text = values["text_input"]
            try:
                qr_img = generate_qr_code(text)
                qr_filename = "qr_code.png"
                qr_img.save(qr_filename)
                window["qr_code_output"].update(filename=qr_filename)
                os.remove(qr_filename)
            except qr.exceptions.DataOverflowError:
                psg.popup_error("Text too long to generate QR code.")
            except Exception as e:
                psg.popup_error(f"Error generating QR code: {e}")
        elif event == psg.WIN_CLOSED or event == "Exit":
            break

    window.close()

if __name__ == "__main__":
    main()
