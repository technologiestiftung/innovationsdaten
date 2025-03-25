from .importer.data_importer import DataImporter

"""
In case we have new data through the XLSX file, we can convert it to JSON via
python -m app.xlsx2json
"""
excel_file = "data_processing/data/basisdaten_clean_2025_v2.xlsx"
outfile_path = "data_processing/data/outfile.json"


data_importer = DataImporter()
data_importer.import_data(excel_file, outfile_path)
