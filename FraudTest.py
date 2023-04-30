from FraudDetector import FraudDetector

if __name__ == '__main__':
    fd = FraudDetector('bankdata.csv.crdownload', ['customer', 'gender', 'category', 'amount'], 'fraud')
    print("Accuracy:", fd.getAccuracy())
    print(fd.predictFraudStr(['C1093826151', 'M', 'es_hotelservices', '58.19']))
