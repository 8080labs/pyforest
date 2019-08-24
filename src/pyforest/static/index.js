define(['base/js/namespace'], function(Jupyter) {
	function load_ipython_extension() {
		window.update_imports_cell = update_imports_cell;
	}
	
	function update_imports_cell(import_str) {
		var sep = '# ^^^ pyforest imports ^^^';
		var doc = Jupyter.notebook.get_cell(0).code_mirror.getDoc();
		var s = doc.getValue();
		var parts = s.split(sep);
		if (parts.length > 1) {
			parts = parts.splice(1);
		}
		doc.setValue(import_str + '\n' + sep + '\n' + parts.join('\n').trim('\n'));
	}
	
	return {
		load_ipython_extension: load_ipython_extension
	};
});
