# Script to analyse a DNA sequence in a FASTA formatted 
# file, and produce a table of  frequencies of codons in the 
# first reading frame
# (C) 2014, Ismail Uddin, ismail.sameeuddin@gmail.com

require 'bio'

# Method to allow the script to read the specified FASTA 
# file, through an argument in terminal placed after the 
# script file name
seqnr = 0
dna = ARGV[0] 
seqnumber = ARGV[1]
seqnr = seqnumber.to_i

# Read the specified file as FASTA formatted file containing 
# a DNA sequence
genome = Hash.new(0)
myfile = Bio::FlatFile.open(dna, "r")
myfile.each_entry do |entry|
	genome[entry.entry_id] = entry.naseq
end


# Extracts the first DNA sequence from the FASTA file
entries = genome.keys.to_a
dnaseq = genome.values.to_a
seq = dnaseq[seqnr]

# Create a new hash, containing the codons as keys and their 
# correspdoning values, the frequency of respective codons
hash = Hash.new(0)
seq.window_search(3, 3) do |codon|
	hash["#{codon.to_s}"] += 1
end

# Display raw data from method above in terminal
puts "#{hash.keys}, #{hash.values}"

# Create a .CSV file with columns for amino acid, IUPAC
# code, and frequency of codon within the DNA sequence
output_file = File.new("#{entries[seqnr]}_cdn_table.csv", 'w')
output_file.puts "Amino Acid, IUPAC Code, Codon, Frequency"
hash.each do |k, v|
	cdn = Bio::Sequence::NA.new("#{k.to_s}")
	aa = cdn.translate.codes
	output_file.puts "#{aa[0]}, #{cdn.translate.to_s}, #{k.to_s.upcase}, #{v}"
end