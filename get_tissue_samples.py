"""File for retrieving sample IDs
Parameters
----------
attribute_file : gzipped .gct file containing the gene reads
tissue_name : tissue sample to search corresponding IDs for
output_file_name : name of resulting file
listing sample IDs of associated tissue sample

Returns
-------
output_file : file listing sample IDs and associated counts of given gene
"""

import gzip
import argparse


if __name__ == '__main__':

    # Argparse Defns
    parser = argparse.ArgumentParser(
        description='Pull sampleIDs for specific tissue type')

    parser.add_argument('--attributes_file', type=str,
                        help='File containing attributes', required=True)

    parser.add_argument(
        '--tissue_name', type=str,
        help='name of the gene', required=True)

    parser.add_argument(
        '--output_file_name', type=str,
        help='name of output file', required=True)

    args = parser.parse_args()

    # Defines file names
    sample_info_file_name = args.attributes_file
    output_file = args.output_file_name

    # Defines variable names
    tissue_name = args.tissue_name


    samples = []
    info_header = None
    for l in open(sample_info_file_name):
        if info_header is None:
            info_header = l.rstrip().split('\t')
        else:
            samples.append(l.rstrip().split('\t'))

    f = open(output_file, 'w')
    for i in range(len(samples)):
        tissue_type = samples[i][5]
        if tissue_type == tissue_name:
            f.write(str(samples[i][0]))
            f.write("\n")
    f.close()
