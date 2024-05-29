# David Metcalfe, James Masters, Antonella Delmestri, Andrew Judge, Daniel Perry, Cheryl Zogg, Belinda Gabbe, Matthew Costa, 2024.

import sys, csv, re

codes = [{"code":"H35z100","system":"readv2"},{"code":"H310z00","system":"readv2"},{"code":"H530z00","system":"readv2"},{"code":"H53z.00","system":"readv2"},{"code":"H30z.00","system":"readv2"},{"code":"H41z.00","system":"readv2"},{"code":"H541z00","system":"readv2"},{"code":"H56z.00","system":"readv2"},{"code":"H501100","system":"readv2"},{"code":"H460z00","system":"readv2"},{"code":"H352z00","system":"readv2"},{"code":"H58z.00","system":"readv2"},{"code":"H35z.00","system":"readv2"},{"code":"H583z00","system":"readv2"},{"code":"H46zz00","system":"readv2"},{"code":"H464z00","system":"readv2"},{"code":"H46z.00","system":"readv2"},{"code":"H300.00","system":"readv2"},{"code":"5192BY","system":"readv2"},{"code":"H4yz.00","system":"readv2"},{"code":"H33z000","system":"readv2"},{"code":"H34z.00","system":"readv2"},{"code":"H31yz00","system":"readv2"},{"code":"H52yz11","system":"readv2"},{"code":"H44z.00","system":"readv2"},{"code":"H58yz00","system":"readv2"},{"code":"H54z.00","system":"readv2"},{"code":"H35yz00","system":"readv2"},{"code":"H4z..00","system":"readv2"},{"code":"H45..00","system":"readv2"},{"code":"H57yz00","system":"readv2"},{"code":"H31z.00","system":"readv2"},{"code":"C370z00","system":"readv2"},{"code":"H500400","system":"readv2"},{"code":"H540z00","system":"readv2"},{"code":"H35zz00","system":"readv2"},{"code":"H440.00","system":"readv2"},{"code":"H320z00","system":"readv2"},{"code":"H311z00","system":"readv2"},{"code":"H42z.00","system":"readv2"},{"code":"H060z00","system":"readv2"},{"code":"H35z000","system":"readv2"},{"code":"H32yz00","system":"readv2"},{"code":"H43z.00","system":"readv2"},{"code":"H4y1z00","system":"readv2"},{"code":"H501300","system":"readv2"},{"code":"H56yz00","system":"readv2"},{"code":"H563z00","system":"readv2"},{"code":"H52z.00","system":"readv2"},{"code":"H32z.00","system":"readv2"},{"code":"H50z.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chronic-pulmonary-disease-elixhauser-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chronic-pulmonary-disease-elixhauser-primary-care-byssinosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chronic-pulmonary-disease-elixhauser-primary-care-byssinosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chronic-pulmonary-disease-elixhauser-primary-care-byssinosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
