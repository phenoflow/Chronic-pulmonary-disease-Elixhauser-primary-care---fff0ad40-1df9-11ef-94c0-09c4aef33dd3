# David Metcalfe, James Masters, Antonella Delmestri, Andrew Judge, Daniel Perry, Cheryl Zogg, Belinda Gabbe, Matthew Costa, 2024.

import sys, csv, re

codes = [{"code":"491 BS","system":"readv2"},{"code":"491","system":"readv2"},{"code":"H301.00","system":"readv2"},{"code":"H312100","system":"readv2"},{"code":"H31..00","system":"readv2"},{"code":"490 T","system":"readv2"},{"code":"H310.00","system":"readv2"},{"code":"AB63600","system":"readv2"},{"code":"H060500","system":"readv2"},{"code":"H33zz13","system":"readv2"},{"code":"493 A","system":"readv2"},{"code":"491 AC","system":"readv2"},{"code":"491 E","system":"readv2"},{"code":"466 BC","system":"readv2"},{"code":"H31y.00","system":"readv2"},{"code":"H30..00","system":"readv2"},{"code":"493 AC","system":"readv2"},{"code":"H311100","system":"readv2"},{"code":"H310000","system":"readv2"},{"code":"H31y100","system":"readv2"},{"code":"490","system":"readv2"},{"code":"H30..11","system":"readv2"},{"code":"H06..00","system":"readv2"},{"code":"H460.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chronic-pulmonary-disease-elixhauser-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chronic-pulmonary-disease-elixhauser-primary-care-tracheobronchitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chronic-pulmonary-disease-elixhauser-primary-care-tracheobronchitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chronic-pulmonary-disease-elixhauser-primary-care-tracheobronchitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
