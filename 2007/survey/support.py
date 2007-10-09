import sys
import plot

max_width = 200

src = 'AllResults.csv'

def plot_and_save(title, data):
	surface, max_key_width = plot.plot(title, data)
	png = '%s.png' % title.replace('/', '_').replace(' ', '_').replace('?', '')
	surface.write_to_png('charts/' + png)

	padding = max(0, max_width - max_key_width)

	file('charts/template.html', 'a').write("""
	<h3>%s</h3>

	<p>
	 <img style='padding-left: %d' src='%s' width='%d' height='%d' alt='%s'/>
	</p>
	""" % (title, padding, png.replace("'", "&apos;"), surface.get_width(), surface.get_height(), title.replace("'", "&apos;")))
