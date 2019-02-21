""" Example tests. Check that they work and that we get the expected output """

from tests.basequery import base
from utils.validate import validate_query


@validate_query(200, path='/')
def info():
    """ The info (/) call """
    resp = {'datasets': [{
        "id": "GRCh38:beacon_test:2030-01-01",
        "assemblyId": "GRCh38",
        "variantCount": 10,
        "callCount": 9,
        "sampleCount": 2504,
    }]}
    return {}, resp



@validate_query(200)
def test_search_1():
    """ Test a standard query with alternateBases, start and end """
    query = base()
    query['start'] = 16050075
    query['end'] = 16050076
    query['referenceBases'] = 'A'
    query['alternateBases'] = 'G'
    resp = {"datasetAlleleResponses": [
        {"datasetId": "GRCh38:beacon_test:2030-01-01",
         "referenceName": "22",
         "callCount": 5008,
         "variantCount": 1,
         "sampleCount": 2504,
         "exists": True,
         "referenceBases": "A",
         "alternateBases": "G",
         "variantType": "SNP",
         "frequency": 0.000199681
        }]}
    return query, resp



@validate_query(200)
def test_snp():
    """ Test variantType SNP """
    query = base()
    query['start'] = 17302972
    query['end'] = 17302973
    query['variantType'] = 'SNP'
    query['referenceBases'] = 'C'
    del query['alternateBases']
    resp = {"datasetAlleleResponses": [
        {"datasetId": "GRCh38:beacon_test:2030-01-01",
         "referenceName": "22",
         "callCount": 5008,
         "variantCount": 2931,
         "sampleCount": 2504,
         "exists": True,
         "referenceBases": "C",
         "alternateBases": "A",
         "variantType": "SNP",
         "frequency": 0.585264
        }]}
    return query, resp


@validate_query(200)
def test_no_end():
    """ Test querying without an end position """
    query = base()
    query['start'] = 17300408
    query['referenceBases'] = 'A'
    query['alternateBases'] = 'G'
    resp = {"datasetAlleleResponses": []}
    return query, resp


@validate_query(200)
def test_end():
    """ Test the same query as `test_no_end()` but with an end position """
    query = base()
    query['start'] = 17300408
    query['end'] = 17300409
    query['referenceBases'] = 'A'
    query['alternateBases'] = 'G'
    resp = {"datasetAlleleResponses": [
        {"datasetId": "GRCh38:beacon_test:2030-01-01",
         "referenceName": "22",
         "callCount": 5008,
         "variantCount": 4723,
         "sampleCount": 2504,
         "exists": True,
         "referenceBases": "A",
         "alternateBases": "G",
         "variantType": "SNP",
         "frequency": 0.943091
        }]}
    return query, resp


@validate_query(200)
def test_insertion():
    """ Test variantTypes INS """
    query = base()
    query['start'] = 16064513
    query['end'] = 16064514
    query['variantType'] = 'INS'
    query['referenceBases'] = 'A'
    del query['alternateBases']
    resp = {"datasetAlleleResponses": [
        {"datasetId": "GRCh38:beacon_test:2030-01-01",
         "referenceName": "22",
         "callCount": 5008,
         "variantCount": 21,
         "sampleCount": 2504,
         "exists": True,
         "referenceBases": "A",
         "alternateBases": "AAGAATGGCCTAATAC",
         "variantType": "INS",
         "frequency": 0.00419329
        }]}
    return query, resp


@validate_query(200)
def test_insertion_altbase():
    """ Test variantTypes by searching for ref and alt """
    query = base()
    query['start'] = 16539541
    query['end'] = 16539542
    query['referenceBases'] = 'A'
    query['alternateBases'] = 'AC'
    resp = {"datasetAlleleResponses": [
        {"datasetId": "GRCh38:beacon_test:2030-01-01",
         "referenceName": "22",
         "callCount": 5008,
         "variantCount": 7,
         "sampleCount": 2504,
         "exists": True,
         "referenceBases": "A",
         "alternateBases": "AC",
         "variantType": "INS",
         "frequency": 0.00139776
        }]}
    return query, resp


@validate_query(200)
def test_multi_insertion():
    """ Find a variantTypes INS at a position where there are two different variants """
    query = base()
    query['start'] = 16879601
    query['end'] = 16879602
    query['referenceBases'] = 'T'
    del query['alternateBases']
    query['variantType'] = 'INS'
    resp = {"datasetAlleleResponses": [
        {"datasetId": "GRCh38:beacon_test:2030-01-01",
         "referenceName": "22",
         "callCount": 5008,
         "variantCount": 116,
         "sampleCount": 2504,
         "exists": True,
         "referenceBases": "T",
         "alternateBases": "TAA",
         "variantType": "INS",
         "frequency": 0.023162939,
        },
        {"datasetId": "GRCh38:beacon_test:2030-01-01",
         "referenceName": "22",
         "callCount": 5008,
         "variantCount": 314,
         "sampleCount": 2504,
         "exists": True,
         "referenceBases": "T",
         "alternateBases": "TA",
         "variantType": "INS",
         "frequency": 0.062699683,
        }
        ]}
    return query, resp


@validate_query(200)
def test_deletion_altbase():
    """ Test a deletion by searching for ref and alt """
    query = base()
    query['start'] = 16497141
    query['end'] = 16497144
    query['referenceBases'] = 'CTT'
    query['alternateBases'] = 'C'
    resp = {"datasetAlleleResponses": [
        {"datasetId": "GRCh38:beacon_test:2030-01-01",
         "referenceName": "22",
         "callCount": 5008,
         "variantCount": 4,
         "sampleCount": 2504,
         "exists": True,
         "referenceBases": "CTT",
         "alternateBases": "C",
         "variantType": "DEL",
         "frequency": 0.000798722
        }]}
    return query, resp


@validate_query(200)
def test_deletion():
    """ Test variantTypes DEL """
    query = base()
    query['start'] = 16517680
    query['end'] = 16517685
    query['referenceBases'] = 'GACAA'
    del query['alternateBases']
    query['variantType'] = 'DEL'
    resp = {"datasetAlleleResponses": [
        {"datasetId": "GRCh38:beacon_test:2030-01-01",
         "referenceName": "22",
         "callCount": 5008,
         "variantCount": 3,
         "sampleCount": 2504,
         "exists": True,
         "referenceBases": "GACAA",
         "alternateBases": "G",
         "variantType": "DEL",
         "frequency": 0.000599042
        }]}
    return query, resp


@validate_query(200)
def test_deletion_2():
    """ Test variantTypes DEL with startMin/startMax """
    query = base()
    query['startMin'] = 17301520
    query['startMax'] = 17301530
    query['endMin'] = 17301536
    query['endMax'] = 17301536
    query['referenceBases'] = 'ATACATAGTC'
    del query['alternateBases']
    query['variantType'] = 'DEL'
    resp = {"datasetAlleleResponses": [
        {"datasetId": "GRCh38:beacon_test:2030-01-01",
         "referenceName": "22",
         "callCount": 5008,
         "variantCount": 2932,
         "sampleCount": 2504,
         "exists": True,
         "referenceBases": "ATACATAGTC",
         "alternateBases": "A",
         "variantType": "DEL",
         "frequency": 0.585463
        }]}
    return query, resp