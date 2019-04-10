from bs4 import BeautifulSoup
from decimal import Decimal
import requests


def convert(amount, cur_from, cur_to, date):
    nom = Decimal('1')
    nom = nom.quantize(Decimal('1.0000'))
    val = Decimal('1')
    val = val.quantize(Decimal('1.0000'))
    nom_1 = Decimal('1')
    nom_1 = nom_1.quantize(Decimal('1.0000'))
    val_1 = Decimal('1')
    val_1 = val_1.quantize(Decimal('1.0000'))
    http = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + date
    response = requests.get(http)
    soup = BeautifulSoup(response.text, 'lxml')
    x = soup.find_all('valute')
    for i in x:
        if cur_from in str(i):
            nom = Decimal(i.nominal.string)
            nom = nom.quantize(Decimal('1.0000'))
            val = str(i.value.string).replace(',', '.')
            val = Decimal(val)
            val = val.quantize(Decimal('1.0000'))
        if cur_to in str(i):
            nom_1 = Decimal(i.nominal.string)
            nom_1 = nom_1.quantize(Decimal('1.0000'))
            val_1 = str(i.value.string).replace(',', '.')
            val_1 = Decimal(val_1)
            val_1 = val_1.quantize(Decimal('1.0000'))
    a = val / nom
    b = val_1 / nom_1
    result = Decimal(Decimal(amount) * a / b)
    result = result.quantize(Decimal('1.0000'))
    return result


def main():
    print(convert(Decimal(input()), input(), input(), input()))


if __name__ == '__main__':
    main()
