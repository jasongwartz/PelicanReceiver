# update location
import subprocess, os, datetime

def location(location):
	# Edits the pelicanconf.py file with the new location
	dir = os.path.dirname(os.path.realpath(__file__))
	with open(os.path.join(dir, "../pelicanconf.py"), "r") as conf:
		pelican = conf.readlines()
		for line in pelican:
			if 'LOCATION =' in line:
				pelican[pelican.index(line)] = 'LOCATION = "%s"\n' % location
	
	dir = os.path.dirname(os.path.realpath(__file__))

	with open(os.path.join(dir, "../pelicanconf.py"), "w") as conf:
		conf.writelines(pelican)
	update_location_history(location)
	return update_pelican()

def update_location_history(location):
	dir = os.path.dirname(os.path.realpath(__file__))

	with open(os.path.join(dir, "../content/pages/locations.md"), "a") as fp:
		fp.write(str("\n -    " + str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")) \
			 + " - " + "[%s](http://maps.google.com/maps?q=%s)" % (location, location)))
	# &&& Future - add to top of list instead of bottom?

def post(title, body, mdimage=None):
	dir = os.path.dirname(os.path.realpath(__file__))

	# Builds the markdown of the new post
	today = str(datetime.date.today())

	with open(os.path.join(dir, "../content/%s.md") % today, 'w') as fp:
		fp.write("Title: %s" % title)
		fp.write("\nDate: %s" % today)
		# &&& Future - add author?
		fp.write('\n\n\n')
		if mdimage: fp.write(mdimage); fp.write('\n\n\n')
		fp.write(body)

	return update_pelican()


def update_pelican():
	directory = os.path.dirname(os.path.realpath(__file__))

	bash_call = "%s/update.sh" % directory
    
	bash_script = subprocess.check_output(bash_call)
	if "Done" in bash_script:
		return True



