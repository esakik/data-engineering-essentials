from avro.datafile import DataFileReader
from avro.io import DatumReader

with DataFileReader(open("contents.avro", "rb"), DatumReader()) as reader:
    for resp in reader:
        print(resp)
