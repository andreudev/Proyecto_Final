import requests
import os


class ApiConnector:
    def __init__(self) -> None:
        self.headers = {"Content-Type": "application/json"}
        self.url = "https://invoice-generator.com"
        self.invoice_directory = (
            f"{os.path.dirname(os.path.abspath(__file__))}/{'facturas'}"
        )

    def connect_api_and_save_invoice_pdf(self, from_who, to_who, number, date, items):
        response = requests.post(
            self.url,
            headers=self.headers,
            json={
                "from": from_who,
                "to": to_who,
                "currency": "COP",
                "number": number,
                "date": date,
                "items": items,
            },
        )
        response.raise_for_status()

        if response.status_code == 200 or response.status_code == 201:
            with open(
                f"{self.invoice_directory}/factura{number}_{date}.pdf", "wb"
            ) as file:
                file.write(response.content)
        else:
            print("Error al guardar la factura")


if __name__ == "__main__":
    api = ApiConnector()

    api.connect_api_and_save_invoice_pdf(
        "1111 XYZ",
        "1111",
        111111,
        "2022-12-12",
        [
            {
                "name": "Producto 1",
                "quantity": 1,
                "unit_cost": 10000,
            },
            {
                "name": "Producto 2",
                "quantity": 2,
                "unit_cost": 20000,
            },
        ],
    )
