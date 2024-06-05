import re
import pytest

# Regex deseni
year_pattern = r'^(19[0-9][0-9]|20[0-1][0-9]|202[0-4])$'

# Test fonksiyonu
def test_year_regex():
    # Eşleşmesi gereken yıllar
    valid_years = [
        '1900', '1919', '1929',
        '1930', '1940', '1950', # 1900'lü yıllar
        '1960', '1965', '1970', # 2000'li yıllar (2024 dahil)
        '1975', '1980', '1985',
        '1990', '1991', '1992',
        '1995', '1996', '1997', # 1900'lü yıllar
        '1998', '1999', '2000', # 2000'li yıllar (2024 dahil)
        '2001', '2002', '2003',
        '2004', '2005', '2006',
        '2007', '2008', '2009',
        '2010', '2011', '2012',
        '2013', '2014', '2015',
        '2016', '2017', '2018',
        '2019', '2020', '2021',
        '2022', '2023', '2024'
    ]

    # Eşleşmemesi gereken yıllar
    invalid_years = [
        '1899', '1800', '2025', # 1900'den önce ve 2024'ten sonra
        '2100', 'abcd', '20204', # Geçersiz formatlar
        '1898', '9999', '0000'
    ]

    for year in valid_years:
        assert re.match(year_pattern, year), f"Year {year} should be valid but did not match."

    for year in invalid_years:
        assert not re.match(year_pattern, year), f"Year {year} should be invalid but matched."


# E-posta regex deseni
email_pattern = r'^[a-zA-Z0-9]{3,}[a-zA-Z0-9._]*[a-zA-Z0-9]@[a-zA-Z0-9][a-zA-Z0-9.]*[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'


# Test fonksiyonu
def test_email_regex():
    # Eşleşmesi gereken e-posta adresleri
    valid_emails = [
        'test@example.com',
        'username@example.com',
        'user.name@example.co.uk',
        'user_name@example.com',
        'username@subdomain.example.com'
    ]

    # Eşleşmemesi gereken e-posta adresleri
    invalid_emails = [
        'plainaddress', # @ eksik
        'test_@example.com',
        'user@.com.my', # Alan adında geçersiz karakter
        'user.name@example.', # TLD eksik
        'user.name@.com', # Alan adında geçersiz karakter
        '@example.com', # Kullanıcı adı eksik
        'user@com', # TLD eksik
        'user@-example.com', # Alan adında geçersiz karakter
        'user@example..com', # Çift nokta
        'user+name@example.com' # '+' işareti içeren geçersiz e-posta adresi
    ]

    for email in valid_emails:
        assert re.match(email_pattern, email), f"E-mail {email} should be valid but did not match."

    for email in invalid_emails:
        assert not re.match(email_pattern, email), f"E-mail {email} should be invalid but matched."


if __name__ == "__main__":
    pytest.main()

