# Successive Codon rpteat Visualisation Tool
# A novel tool to allow the graphical visualisation of
# successive codon rpteats with a DNA sequence
# (C) 2014, Ismail Uddin, ismail.sameeuddin@gmail.com

import sys

def parse_FASTA(filename):
    """Parse all entries in FASTA file into a dictionary"""

    import collections

    file = open(filename, 'r')
    entry_id = ''
    sequence = ''
    entries = collections.OrderedDict()
    for line in file:
        if line[0] == '>':
            sequence = ''
            entry_id = ''
            s = line[1:].rstrip()
            entry_id += s
        elif line[0] != '>':
            d = line.rstrip().upper()
            sequence += d
            entries[entry_id] = sequence
        elif line == '':
            file.close()
    return entries

# 1st argument : Path for .FASTA file encoding DNA sequence
# 2nd argument : Sequence ID / number of sequence in .FASTA file (0, 1, etc.)
# 3rd argument : 'matplotlib' to use Matplotlib plotting interface
#                'plotly' to use Internet-based Plot.ly plotting interface

fasta = sys.argv[1]					# Path for .FASTA file
seq_id = int(sys.argv[2])			# Sequence ID
fasta_dict = parse_FASTA(fasta)		# Dictionary from parsed .FASTA file
headers = fasta_dict.keys()			# Headers from .FASTA file
sequences = fasta_dict.values()		# Sequences from .FASTA file
seq = sequences[seq_id]				# String for specified sequence



codons = []			# List with codons of sequence
codons_fs = []		# -3 frameshift of codon list 'codons'
cdn_id = []			# List with codon numbers
rpt = []			# List: If successive codon is a rpteat, 1 is appended
					# Otherwise, 0 is appended

end = len(seq[0:]) - (len(seq[0:]) % 3) - 1

for i in range(0, end, 3):
	codons.append(seq[i:i+3])

for i in range(0, end, 3):
	codons_fs.append(seq[i:i+3])

codons_fs.pop(0)

# Loop to look for successive codon rpteats
for i in range(0, len(codons_fs), 1):
	cdn_id.append(i)
	if codons[i] == codons_fs[i]:
		rpt.append(1)
	else:
		rpt.append(0)

# .CSV file created with three columns
# Codon, Codon number, rpteat
# rpteat value is either 0 or 1
file = open('%s_codon_repeats.CSV' % headers[seq_id], 'w')
file.write('Codon, ID, Successive repeat \n')
for i in range(0, len(codons_fs), 1):
	file.write('%s, %s, %s \n' % (codons[i], cdn_id[i], rpt[i]))
file.close()

rp_cdn = []

for i in range(0, len(codons_fs), 1):
	if rpt[i] == 1:
		rp_cdn.append(i)

# Select use of either Matplotlib or Plot.ly module for
# plotting data.
# Matplotlib: Works offline / no internet connection required
# Plot.ly: Requires internet / graphs can be shared online

if sys.argv[3] == 'matplotlib':
	import matplotlib.pyplot as plt
	plt.xkcd()


	X = cdn_id
	Y = rpt
	plt.xlabel('Codon number')
	plt.ylabel('Repeat of codon at successive position')
	plt.title('%s succesve codon repeats visualisation' % (headers[seq_id]))
	for i in range(0, len(codons_fs), 1):
		if rpt[i] == 1:
			plt.text(i,0.5,"%s, %.0f" % (codons[i], i), rotation=90, position=(i+2,0.5))
	plt.plot(X,Y)
	plt.show()

else:

	# Use of plot.ly API to produce a scatter graph which is
	# uploaded online as a public graph to plot.ly servers.
	# This allows a scrolling / panning graph for very large
	# sequences which is more cumbersome to produce in MS Excel.

	import plotly.plotly as py
	from plotly.graph_objs import Figure, Data, Bar, Font, XAxis, Layout, Annotation, Annotations

	# Enter username and API key credentials for access to
	# plot.ly servers. Credentials are provided free of charge
	# from http://plot.ly/ upon registration

	#           username     API key
	py.sign_in('<<USERNAME>>', '<<API KEY>>')

	def make_annotation(x_in,y_in):
		x_offset = +0.05
		y_offset = -2.2
		return Annotation(text=str(y_in),
			xref='x',
			yref='y',
			x=x_in+x_offset,
			showarrow = False,
			font = Font(color='#262626', size = 13))

	label_list = zip(rp_cdn, codons)
	my_annotations = Annotations([make_annotation(xx,yy) for xx,yy in label_list])

	trace1 = Bar(x=cdn_id, y=rpt)

	my_data = Data([trace1])
	my_title = "%s Successive Codon repeat Figure" % headers[seq_id]
	my_layout = Layout(title=my_title,
	                   xaxis=XAxis(title='Codon number'),
	                   annotations = my_annotations)
	my_fig = Figure(data=my_data, layout=my_layout)
	py.plot(my_fig)
