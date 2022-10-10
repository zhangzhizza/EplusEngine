import os
from StaticEplusEngine import run_eplus_model, convert_json_idf

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

def test_run_eplus_model():
	eplus_run_path = THIS_DIR + os.sep + \
					'EnergyPlus9.5' + os.sep + 'energyplus'
	idf_path = THIS_DIR + os.sep + '1ZoneUncontrolled_win_1.idf'
	output_dir = THIS_DIR + os.sep + '1ZoneUncontrolled_win_1_res'
	run_eplus_model(eplus_run_path, idf_path, output_dir)

def test_convert_json_idf():
	eplus_run_path = THIS_DIR + os.sep + \
					'EnergyPlus9.5' + os.sep + 'energyplus'
	idf_path = THIS_DIR + os.sep + '1ZoneUncontrolled_win_1.idf'
	convert_json_idf(eplus_run_path, idf_path)
	epjson_path = THIS_DIR + os.sep + '1ZoneUncontrolled_win_test.epJSON'
	convert_json_idf(eplus_run_path, epjson_path)

test_run_eplus_model()
test_convert_json_idf()