from pathlib import Path
import json
import ipywidgets
from traitlets import Unicode, List


with (Path(__file__).parent / 'package.json').open('rt') as fh:
	npm_package = json.load(fh)


@ipywidgets.register
class PyforestWidget(ipywidgets.DOMWidget):
	_view_module = Unicode(npm_package['name']).tag(sync=True)
	_view_name = Unicode('PyforestWidget').tag(sync=True)
	_view_module_version = Unicode('^' + npm_package['version']).tag(sync=True)
	
	_model_module = Unicode(npm_package['name']).tag(sync=True)
	_model_name = Unicode('PyforestWidgetModel').tag(sync=True)
	_model_module_version = Unicode('^' + npm_package['version']).tag(sync=True)
	
	imports = List(Unicode()).tag(sync=True)
