# Bioinformatics script to predict the probability of
# PCR success based on an equation by Benita et. al (2003)
# Benita, Y. (2003), Nucleic Acids Research., 31 (16)

require 'bio'

# Reads specified FASTA file, and extracts the PCR 
# template, and both primers used for amplifications
dna = ARGV[0]

genome = Hash.new(0)
myfile = Bio::FlatFile.open(dna, "r")
myfile.each_entry do |entry|
	genome[entry.entry_id] = entry.naseq
end

dnaseq = genome.values.to_a

# First sequence in FASTA file is denoted as the PCR 
# template, remaining two denoted as primers
template = dnaseq[0]
primer0 = dnaseq[1]
primer1 = dnaseq[2]

p0 = dnaseq[1].gc_content.to_f
p1 = dnaseq[2].gc_content.to_f

# Primer with lowest GC content is selected for inclusion
# in the equation
if p0 < p1 then
	primer = dnaseq[1]
else
	primer = dnaseq[2]
end

# GC curve calculated using sliding window of with 21 bp,
# and step of 1 bp, across the PCR template
a = {}
c = {}
i = 0
j = 0

template.window_search(21) do |s|
	a[i] = s.gc_content.to_f
	i += 1
end

# Number of windows with GC value above 65% counted
counts = Hash.new{|h, k| h[k] = 0}
a.each do |k, v|
	if v.to_f > 0.65
		counts[0] += 1
	end
end

# Array created of windows with GC values above 65%, 
# with their respective values recorded
a.each do |k, v|
	if v.to_f > 0.65
		c[j] = v.to_f
	end
	j += 1
end

gc65 = c.values

# Parameters for equation are calculated 
gc_primer = primer.gc_content.to_f / primer.length
ratio_gc = counts[0].to_f / template.length
gc_windows = gc65.inject(0){|sum, x| sum + x}
auc_gc = gc_windows - (counts[0].to_f * 0.65)
norm_auc = ratio_gc * auc_gc


# Equation is broken into parts, calculated
exponent = 4.9 - 7.6 * gc_primer - 0.004 * norm_auc
k = Math.exp(exponent)
p = k / (1 + k)

# Raw values of parameters are shown on screen, in
# addition to the probability value (P) of PCR success
puts "\nProbability of PCR success: \n" + p.to_s
puts "\nNumber of GC windows above 65%: \n" + counts[0].to_s
puts "\nPCR template length: \n" + template.length.to_s
puts "\nGC content of primer with lowest GC content: \n" + primer.gc_content.to_f.to_s
puts "\nGCprimer: \n" + gc_primer.to_s
puts "\nLength of the lowest GC content primer: \n" + primer.length.to_s
puts "\nArea under the GC curve and above 65% threshold: \n" + auc_gc.to_s
puts "\nValue of k: \n" + k.to_s
puts "\nRatio_GC * AUC_GC: \n" + norm_auc.to_s
puts "\nNumber of GC windows with values above 65% divided by length of the PCR template: \n" + ratio_gc.to_s
puts "\nValue of exponent: \n" + exponent.to_s
