# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"14B3.12","system":"readv2"},{"code":"H36..00","system":"readv2"},{"code":"H37..00","system":"readv2"},{"code":"H3z..11","system":"readv2"},{"code":"1001.0","system":"med"},{"code":"103494.0","system":"med"},{"code":"104608.0","system":"med"},{"code":"106650.0","system":"med"},{"code":"10802.0","system":"med"},{"code":"10863.0","system":"med"},{"code":"10980.0","system":"med"},{"code":"11150.0","system":"med"},{"code":"12166.0","system":"med"},{"code":"1446.0","system":"med"},{"code":"14798.0","system":"med"},{"code":"15157.0","system":"med"},{"code":"15626.0","system":"med"},{"code":"16410.0","system":"med"},{"code":"21061.0","system":"med"},{"code":"23492.0","system":"med"},{"code":"24248.0","system":"med"},{"code":"25603.0","system":"med"},{"code":"26125.0","system":"med"},{"code":"26306.0","system":"med"},{"code":"27819.0","system":"med"},{"code":"3243.0","system":"med"},{"code":"33450.0","system":"med"},{"code":"37247.0","system":"med"},{"code":"37959.0","system":"med"},{"code":"40159.0","system":"med"},{"code":"40788.0","system":"med"},{"code":"44525.0","system":"med"},{"code":"45089.0","system":"med"},{"code":"46578.0","system":"med"},{"code":"56860.0","system":"med"},{"code":"5710.0","system":"med"},{"code":"5798.0","system":"med"},{"code":"5909.0","system":"med"},{"code":"59263.0","system":"med"},{"code":"60188.0","system":"med"},{"code":"61118.0","system":"med"},{"code":"61513.0","system":"med"},{"code":"63216.0","system":"med"},{"code":"63479.0","system":"med"},{"code":"64721.0","system":"med"},{"code":"65733.0","system":"med"},{"code":"66043.0","system":"med"},{"code":"66058.0","system":"med"},{"code":"67040.0","system":"med"},{"code":"68066.0","system":"med"},{"code":"68662.0","system":"med"},{"code":"70787.0","system":"med"},{"code":"7884.0","system":"med"},{"code":"794.0","system":"med"},{"code":"92955.0","system":"med"},{"code":"93568.0","system":"med"},{"code":"9876.0","system":"med"},{"code":"99536.0","system":"med"},{"code":"998.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chronic-obstructive-pulmonary-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chronic-obstructive-pulmonary-disease-copd---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chronic-obstructive-pulmonary-disease-copd---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chronic-obstructive-pulmonary-disease-copd---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
