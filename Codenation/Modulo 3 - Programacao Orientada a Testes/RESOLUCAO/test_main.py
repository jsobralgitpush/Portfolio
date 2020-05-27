from main import get_temperature
import pytest

def test_get_temperature_if_is_num():
    #setup
    lat = -14.235004
    lng = -51.92528
    test = False

    # execucao do teste
    try:
        float(get_temperature(lat,lng))
        test = True
    except:
        pass

    # verificacao
    assert test is True

def test_get_temperature_between_max_min_global():
    #setup
    lat = -14.235004
    lng = -51.92528
    test = False
    temp_to_test = get_temperature(lat,lng)

    # execucao do teste
    if temp_to_test < 60 or temp_to_test > -90:
        test = True

    # verificacao
    assert test is True

@pytest.mark.parametrize("lat,lng, temp", [(-14.235004, -51.92528, 21),
                                           (-22.882502, -43.349804, 22),
                                           (-23.4593, -46.660036, 16)])
def test_get_temperature_required(lat, lng, temp):
    #setup
    test = False
    aprox_temp = range(int(temp*0.85), int(temp*1.15))

    #execucao do teste
    if get_temperature(lat,lng) in aprox_temp:
        test = True

    #verificacao
    assert test is True



