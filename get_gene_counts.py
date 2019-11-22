
"""File for retrieving gene counts
Parameters
----------
gene_count_file : gzipped .gct file containing the gene reads
gene_name : gene name to be analyzed
output_file : name of resulting file
listing sample IDs and associated counts of given gene
Returns
-------
output_file : file listing sample IDs and associated counts of given gene
"""

import gzip
import argparse


if __name__ == '__main__':

    # Argparse Defns
    parser = argparse.ArgumentParser(
        description='Retrieve counts for specific gene')

    parser.add_argument('--gene_count_file', type=str,
                        help='File containing gene reads', required=True)

    parser.add_argument(
        '--gene_name', type=str,
        help='name of the gene', required=True)

    parser.add_argument(
        '--output_file_name', type=str,
        help='name of output file', required=True)

    args = parser.parse_args()

    # Defines file names
    data_file_name = args.gene_count_file
    output_file = args.output_file_name

    # Defines variable names
    gene_name = args.gene_name

    # Create Python Dictionary
    sample_counts = {}

    version = None
    dim = None
    sample_ids = None
    gene_name_col = 1
    for l in gzip.open(data_file_name, 'rt'):
        if version is None:
            version = l
            continue

        if dim is None:
            dim = [int(x) for x in l.rstrip().split()]
            continue

        if sample_ids is None:
            sample_ids = []
            i = 0
            for field in l.rstrip().split('\t'):
                sample_ids.append([field, i])
                i += 1

        A = l.rstrip().split('\t')
        if A[gene_name_col] == gene_name:
            for i in range(2, len(sample_ids)-2):
                sample_counts[str(sample_ids[i])] = A[i]

    f = open(output_file, 'w')
    for i in range(len(sample_counts)):
        f.write(str(sample_ids[i+2][0]) + "\t" + str(
            sample_counts[str(sample_ids[i+2])]))
        f.write("\n")
    f.close()





